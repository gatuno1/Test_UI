#!/usr/bin/env python3
"""
Script unificado para verificar contraste de colores en temas CustomTkinter
Modo normal: Cálculos WCAG básicos (AA Normal/Large)
Modo avanzado: Cálculos precisos con colorspacious (AAA + Delta E)
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from enum import StrEnum
from typing import Dict, List, Self, Tuple

from rich import traceback
from rich.console import Console
from rich_argparse import ArgumentDefaultsRichHelpFormatter

# Import condicional para colorspacious
try:
    import colorspacious

    COLORSPACIOUS_AVAILABLE = True
except ImportError:
    COLORSPACIOUS_AVAILABLE = False

# Inicializar componentes Rich
traceback.install(show_locals=True, word_wrap=True)
consola = Console(soft_wrap=True)
consola_advertencia = Console(soft_wrap=True, style="orange1")
consola_error = Console(stderr=True, soft_wrap=True, style="red")

# Constantes de colores con nombres
NAMED_COLORS: Dict[str, str] = {
    "white": "#ffffff",
    "gray10": "#1a1a1a",
    "gray14": "#242424",
    "gray17": "#2b2b2b",
    "gray20": "#333333",
    "gray36": "#5c5c5c",
    "gray40": "#666666",
    "gray41": "#696969",
    "gray45": "#737373",
    "gray50": "#808080",
    "gray52": "#858585",
    "gray53": "#878787",
    "gray55": "#8c8c8c",
    "gray60": "#999999",
    "gray62": "#9e9e9e",
    "gray65": "#a6a6a6",
    "gray70": "#b3b3b3",
    "gray74": "#bdbdbd",
    "gray75": "#bfbfbf",
    "gray78": "#c7c7c7",
    "gray81": "#cfcfcf",
    "gray86": "#dbdbdb",
    "gray90": "#e6e6e6",
    "gray92": "#ebebeb",
    "gray100": "#ffffff",
    "transparent": "#ffffff",  # Asume fondo blanco para transparente
}

# Constantes WCAG básicas
WCAG_GAMMA_THRESHOLD: float = 0.03928
WCAG_GAMMA_DIVISOR: float = 12.92
WCAG_GAMMA_OFFSET: float = 0.055
WCAG_GAMMA_BASE: float = 1.055
WCAG_GAMMA_EXPONENT: float = 2.4
WCAG_LUMINANCE_R: float = 0.2126
WCAG_LUMINANCE_G: float = 0.7152
WCAG_LUMINANCE_B: float = 0.0722
WCAG_CONTRAST_OFFSET: float = 0.05
WCAG_AA_NORMAL_RATIO: float = 4.5
WCAG_AA_LARGE_RATIO: float = 3.0

# Constantes WCAG avanzadas
WCAG_AAA_NORMAL_RATIO: float = 7.0
WCAG_AAA_LARGE_RATIO: float = 4.5

# Constantes de normalización (para modo avanzado)
RGB_NORMALIZER: float = 255.0
XYZ_NORMALIZER: float = 100.0

# Constante Delta E
DELTA_E_THRESHOLD: float = 3.0

# Componentes con texto que necesitan verificación
TEXT_COMPONENTS: Dict[str, List[str]] = {
    "CTkLabel": ["text_color", "fg_color"],
    "CTkButton": ["text_color", "fg_color"],
    "CTkEntry": ["text_color", "fg_color"],
    "CTkCheckBox": ["text_color", "fg_color"],
    "CTkRadioButton": ["text_color", "fg_color"],
    "CTkOptionMenu": ["text_color", "fg_color"],
    "CTkComboBox": ["text_color", "fg_color"],
    "CTkTextbox": ["text_color", "fg_color"],
    "DropdownMenu": ["text_color", "fg_color"],
}

# Colores de fallback
FALLBACK_COLORS: List[str] = ["#ffffff", "#000000"]

# Archivo de configuración de temas por defecto
DEFAULT_THEMES_CONFIG = "themes_config.json"


class ModoAnalisis(StrEnum):
    """Enumeración para los modos de análisis"""

    def __new__(cls, value: str, description: str) -> Self:
        """Crea una nueva instancia de ModoAnalisis"""
        obj: Self = str.__new__(cls, value.strip())
        obj._value_ = value.strip()
        obj.__doc__ = description.strip()
        return obj

    NORMAL = (
        "normal",
        "Análisis WCAG básico (AA Normal/Large solamente)"
    )
    AVANZADO = (
        "avanzado",
        "Análisis avanzado con colorspacious (AAA + Delta E)"
    )

    @classmethod
    def from_string(cls, value: str) -> Self:
        """Convierte string a ModoAnalisis"""
        try:
            return next(
                modo for modo in cls
                if modo.value.lower() == value.strip().lower()
            )
        except StopIteration as e:
            modos_permitidos: str = ', '.join(
                [f"'{modo.value}'" for modo in cls]
            )
            raise ValueError(
                f"Modo de análisis inválido: '{value}'. "
                f"Solo se permiten: {modos_permitidos}."
            ) from e


class ThemeMode(StrEnum):
    """Enumeración para los modos de tema"""

    LIGHT = "light"
    DARK = "dark"


@dataclass
class ContrastResult:
    """Resultado de verificación de contraste"""

    foreground: str
    background: str
    component: str
    mode: str
    ratio: float
    wcag_aa_normal: bool
    wcag_aa_large: bool
    webaim_url: str

    # Campos opcionales para modo avanzado
    wcag_aaa_normal: bool = False
    wcag_aaa_large: bool = False
    lab_delta_e: float = 0.0


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convierte color hex a RGB"""
    hex_color = NAMED_COLORS.get(hex_color, hex_color)

    # Limpia el color hex
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])

    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


def calculate_luminance_basic(rgb: Tuple[int, int, int]) -> float:
    """Calcula la luminancia relativa según WCAG 2.1 (modo básico)"""

    def gamma_correct(value: float) -> float:
        value = value / 255.0
        return (
            value / WCAG_GAMMA_DIVISOR
            if value <= WCAG_GAMMA_THRESHOLD
            else ((value + WCAG_GAMMA_OFFSET) / WCAG_GAMMA_BASE) ** WCAG_GAMMA_EXPONENT
        )

    r, g, b = rgb
    r_linear: float = gamma_correct(r)
    g_linear: float = gamma_correct(g)
    b_linear: float = gamma_correct(b)

    return (
        WCAG_LUMINANCE_R * r_linear
        + WCAG_LUMINANCE_G * g_linear
        + WCAG_LUMINANCE_B * b_linear
    )


def calculate_contrast_ratio_basic(fg_color: str, bg_color: str) -> float:
    """Calcula el ratio de contraste entre dos colores (modo básico)"""
    try:
        fg_rgb = hex_to_rgb(fg_color)
        bg_rgb = hex_to_rgb(bg_color)

        fg_luminance: float = calculate_luminance_basic(fg_rgb)
        bg_luminance: float = calculate_luminance_basic(bg_rgb)

        lighter: float = max(fg_luminance, bg_luminance)
        darker: float = min(fg_luminance, bg_luminance)

        return (lighter + WCAG_CONTRAST_OFFSET) / (darker + WCAG_CONTRAST_OFFSET)

    except (ValueError, KeyError, IndexError):
        return 0.0


def rgb_to_xyz(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """Convierte RGB a XYZ usando colorspacious (modo avanzado)"""
    if not COLORSPACIOUS_AVAILABLE:
        return (0.0, 0.0, 0.0)

    # Normaliza RGB a 0-1
    rgb_normalized = tuple(c / RGB_NORMALIZER for c in rgb)

    # Convierte a XYZ usando colorspacious
    xyz = colorspacious.cspace_convert(rgb_normalized, "sRGB1", "XYZ100")
    return tuple(xyz)


def calculate_contrast_ratio_avanzado(fg_color: str, bg_color: str) -> float:
    """Calcula el ratio de contraste usando colorspacious para mayor precisión"""
    if not COLORSPACIOUS_AVAILABLE:
        return calculate_contrast_ratio_basic(fg_color, bg_color)

    try:
        fg_rgb = hex_to_rgb(fg_color)
        bg_rgb = hex_to_rgb(bg_color)

        # Convierte a espacio de color CIE XYZ
        fg_xyz = rgb_to_xyz(fg_rgb)
        bg_xyz = rgb_to_xyz(bg_rgb)

        # Calcula luminancia Y (segundo componente de XYZ)
        fg_luminance: float = fg_xyz[1] / XYZ_NORMALIZER  # Normaliza de 0-100 a 0-1
        bg_luminance: float = bg_xyz[1] / XYZ_NORMALIZER

        # Calcula ratio de contraste según WCAG 2.1
        lighter: float = max(fg_luminance, bg_luminance)
        darker: float = min(fg_luminance, bg_luminance)

        return (lighter + WCAG_CONTRAST_OFFSET) / (darker + WCAG_CONTRAST_OFFSET)

    except (ValueError, KeyError, IndexError):
        return 0.0


def calculate_color_difference(fg_color: str, bg_color: str) -> float:
    """Calcula la diferencia de color usando Delta E en espacio LAB"""
    if not COLORSPACIOUS_AVAILABLE:
        return 0.0

    try:
        fg_rgb = hex_to_rgb(fg_color)
        bg_rgb = hex_to_rgb(bg_color)

        # Normaliza RGB a 0-1
        fg_normalized = tuple(c / RGB_NORMALIZER for c in fg_rgb)
        bg_normalized = tuple(c / RGB_NORMALIZER for c in bg_rgb)

        # Convierte a LAB
        fg_lab = colorspacious.cspace_convert(fg_normalized, "sRGB1", "CIELab")
        bg_lab = colorspacious.cspace_convert(bg_normalized, "sRGB1", "CIELab")

        # Calcula Delta E (diferencia perceptual)
        delta_e = colorspacious.deltaE(fg_lab, bg_lab, input_space="CIELab")
        return delta_e

    except (ValueError, KeyError, IndexError):
        return 0.0


def calculate_contrast_ratio(fg_color: str, bg_color: str, mode: ModoAnalisis) -> float:
    """Calcula el ratio de contraste según el modo especificado"""
    if mode == ModoAnalisis.AVANZADO:
        return calculate_contrast_ratio_avanzado(fg_color, bg_color)
    return calculate_contrast_ratio_basic(fg_color, bg_color)


def generate_webaim_url(fg_color: str, bg_color: str) -> str:
    """Genera URL para WebAIM Contrast Checker"""
    fg_clean: str = fg_color.lstrip("#")
    bg_clean: str = bg_color.lstrip("#")

    # Convierte colores con nombre a hex sin #
    named_colors_hex: dict = {k: v.lstrip("#") for k, v in NAMED_COLORS.items()}

    fg_clean = named_colors_hex.get(fg_color, fg_clean)
    bg_clean = named_colors_hex.get(bg_color, bg_clean)

    return f"https://webaim.org/resources/contrastchecker/?fcolor={fg_clean}&bcolor={bg_clean}"


def parse_arguments() -> argparse.Namespace:
    """Configura y parsea argumentos de línea de comandos"""
    parser = argparse.ArgumentParser(
        description=(
            "[bold italic]Verificador de accesibilidad WCAG de contraste , "
            "para temas CustomTkinter[/]"
        ),
        formatter_class=ArgumentDefaultsRichHelpFormatter,
        add_help=True,
    )

    modos: List[str] = [
        f"`[green]{modo.value}[/]` - {modo.__doc__}"
        for modo in ModoAnalisis
    ]
    parser.add_argument(
        "-m", "--modo",
        choices=[modo.value for modo in ModoAnalisis],
        default=ModoAnalisis.NORMAL.value,
        help=(f"[u]Modos de análisis:[/] {', '.join(modos)}. [yellow]"),
    )

    parser.add_argument(
        "-c", "--config",
        default=DEFAULT_THEMES_CONFIG,
        help=("Archivo de configuración de temas [yellow]"),
    )

    return parser.parse_args()


def extract_color_pairs(theme_data: Dict, mode: ModoAnalisis) -> List[ContrastResult]:
    """Extrae pares de colores relevantes del tema"""
    results = []

    for component, color_keys in TEXT_COMPONENTS.items():
        if component in theme_data:
            _process_component(theme_data, component, color_keys, results, mode)

    return results


def _process_component(
    theme_data: Dict,
    component: str,
    color_keys: List[str],
    results: List[ContrastResult],
    mode: ModoAnalisis,
) -> None:
    """Procesa un componente específico y añade resultados a la lista"""
    comp_data = theme_data[component]

    # Extrae colores de texto y fondo
    text_colors = comp_data.get(color_keys[0], [])
    bg_colors = comp_data.get(color_keys[1], [])

    # Maneja casos donde fg_color es transparente
    if bg_colors == "transparent":
        # Usa el color de fondo del contenedor padre (CTk o CTkFrame)
        if "CTkFrame" in theme_data:
            bg_colors = theme_data["CTkFrame"].get("fg_color", FALLBACK_COLORS)
        else:
            bg_colors: list = FALLBACK_COLORS  # Fallback

    # Procesa ambos modos (claro/oscuro)
    for i, theme_mode in enumerate(ThemeMode):
        text_color: str = _get_color_for_mode(text_colors, i)
        bg_color: str = _get_color_for_mode(bg_colors, i)
        if text_color and bg_color:
            result: ContrastResult = _create_contrast_result(
                component, theme_mode, text_color, bg_color, mode
            )
            results.append(result)


def _get_color_for_mode(colors, mode_index: int) -> str:
    """Obtiene el color para el modo específico"""
    if isinstance(colors, list) and len(colors) > mode_index:
        return colors[mode_index]
    if isinstance(colors, str):
        return colors
    return ""


def _create_contrast_result(
    component: str,
    theme_mode: str,
    text_color: str,
    bg_color: str,
    analysis_mode: ModoAnalisis,
) -> ContrastResult:
    """Crea un resultado de contraste para los colores dados"""
    ratio: float = calculate_contrast_ratio(text_color, bg_color, analysis_mode)
    webaim_url: str = generate_webaim_url(text_color, bg_color)

    # Campos básicos
    result = ContrastResult(
        foreground=text_color,
        background=bg_color,
        component=component,
        mode=theme_mode,
        ratio=ratio,
        wcag_aa_normal=ratio >= WCAG_AA_NORMAL_RATIO,
        wcag_aa_large=ratio >= WCAG_AA_LARGE_RATIO,
        webaim_url=webaim_url,
    )

    # Campos adicionales para modo avanzado
    if analysis_mode == ModoAnalisis.AVANZADO:
        result.wcag_aaa_normal = ratio >= WCAG_AAA_NORMAL_RATIO
        result.wcag_aaa_large = ratio >= WCAG_AAA_LARGE_RATIO
        result.lab_delta_e = calculate_color_difference(text_color, bg_color)

    return result


def load_theme(file_path: str) -> Dict:
    """Carga un archivo de tema JSON con manejo de errores mejorado"""
    try:
        # Verificar si el archivo existe
        if not os.path.exists(file_path):
            print_error_message(f"El archivo de tema no existe: {file_path}")
            raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

        # Verificar si es un archivo (no un directorio)
        if not os.path.isfile(file_path):
            print_error_message(f"La ruta especificada no es un archivo: {file_path}")
            raise OSError(f"No es un archivo válido: {file_path}")

        # Verificar permisos de lectura
        if not os.access(file_path, os.R_OK):
            print_error_message(f"Sin permisos de lectura para el archivo: {file_path}")
            raise PermissionError(f"Sin permisos de lectura: {file_path}")

        # Verificar tamaño del archivo
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            print_error_message(f"El archivo de tema está vacío: {file_path}")
            raise ValueError(f"Archivo vacío: {file_path}")

        # Cargar y parsear el archivo JSON
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                theme_data = json.load(f)

            except json.JSONDecodeError as e:
                print_error_message(
                    f"JSON inválido en {file_path}: {e.msg} (línea {e.lineno}, columna {e.colno})"
                )
                raise

        # Verificar que el JSON no esté vacío
        if not theme_data:
            print_error_message(
                f"El archivo JSON está vacío o no contiene datos: {file_path}"
            )
            raise ValueError(f"JSON vacío: {file_path}")

        # Verificar estructura básica del tema
        if not isinstance(theme_data, dict):
            print_error_message(
                f"El tema debe ser un objeto JSON, no {type(theme_data).__name__}: {file_path}"
            )
            raise ValueError(f"Estructura de tema inválida: {file_path}")

        return theme_data

    except UnicodeDecodeError as e:
        print_error_message(f"Error de codificación en {file_path}: {e}")
        raise
    except OSError as e:
        print_error_message(f"Error del sistema al acceder a {file_path}: {e}")
        raise
    except Exception as e:
        print_error_message(f"Error inesperado al cargar {file_path}: {e}")
        raise


def load_themes_config(config_file: str = DEFAULT_THEMES_CONFIG) -> Dict[str, str]:
    """Carga la configuración de temas desde el archivo JSON especificado"""
    config_path: str = config_file
    # Si el archivo no es absoluto, lo busca en el directorio actual del script
    if not os.path.isabs(config_file):
        config_path = os.path.join(os.path.dirname(__file__), config_file)
    # Intenta cargar el archivo de configuración
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("themes", {})

    except FileNotFoundError:
        print_error_message(f"No se encontró el archivo de configuración {config_path}")
        return {}
    except json.JSONDecodeError as e:
        print_error_message(
            f"El archivo de configuración {config_path} no es un JSON válido: {e}"
        )
        return {}
    except (OSError, KeyError) as e:
        print_error_message(f"Error cargando configuración de temas: {e}")
        return {}


def print_success_message(message: str = "PASA") -> None:
    """Imprime mensaje de éxito con símbolo"""
    consola.print(f"✅ [green]{message}[/]")


def print_fail_msg(message: str = "FALLA") -> None:
    """Imprime mensaje de falla con símbolo"""
    consola.print(f"⛔ [red]{message}[/]")


def print_error_message(message: str) -> None:
    """Imprime mensaje de error con símbolo"""
    consola_advertencia.print(f"❌ {message}")


def print_warning_message(message: str) -> None:
    """Imprime mensaje de advertencia con símbolo"""
    consola_advertencia.print(f"⚠️ {message}")


def _print_failed_components(
    test_name: str, failed_results: List[ContrastResult]
) -> None:
    """Imprime componentes que fallan una prueba específica"""
    if failed_results:
        consola_advertencia.print(f"\nComponentes que fallan '{test_name}':")
        for result in failed_results:
            consola_advertencia.print(
                f"  * {result.component} ({result.mode}): "
                f"{result.ratio:.2f}:1"
            )


def print_results(
    results: List[ContrastResult], theme_name: str, mode: ModoAnalisis
) -> None:
    """Imprime resultados de manera formateada según el modo de análisis"""
    consola.print(f"\n{'=' * 80}")

    if mode == ModoAnalisis.AVANZADO:
        consola.print(f"ANÁLISIS AVANZADO DE CONTRASTE - TEMA: '{theme_name}'")
        if COLORSPACIOUS_AVAILABLE:
            consola.print("Usando biblioteca [b i]colorspacious[/] para cálculos precisos")
        else:
            print_warning_message(
                "Biblioteca [b i]colorspacious[/i] no disponible[/], usando cálculos básicos"
            )
    else:
        consola.print(f"ANÁLISIS DE CONTRASTE - TEMA: '{theme_name}'")

    consola.print(f"{'=' * 80}")

    # Inicializar contadores para modo básico
    failed_aa_normal = []
    failed_aa_large = []

    # Contadores adicionales para modo avanzado
    failed_aaa_normal = []
    failed_aaa_large = []

    for result in results:
        consola.print(f"\n[bold]{result.component} ({result.mode})[/]")
        consola.print(f"  Texto: [cyan]{result.foreground}[/]")
        consola.print(f"  Fondo: [cyan]{result.background}[/]")
        consola.print(f"  Ratio: {result.ratio:.2f}:1")
        # Estados WCAG AA (siempre se muestran)
        consola.print(f"  WCAG AA Normal ({WCAG_AA_NORMAL_RATIO}:1): ", end="")
        if result.wcag_aa_normal:
            print_success_message()
        else:
            print_fail_msg()
        consola.print(f"  WCAG AA Large ({WCAG_AA_LARGE_RATIO}:1):  ", end="")
        if result.wcag_aa_large:
            print_success_message()
        else:
            print_fail_msg()

        # Información adicional para modo avanzado
        if mode == ModoAnalisis.AVANZADO:
            consola.print(f"  WCAG AAA Normal ({WCAG_AAA_NORMAL_RATIO}:1):", end="")
            if result.wcag_aaa_normal:
                print_success_message()
            else:
                print_fail_msg()
            consola.print(f"  WCAG AAA Large ({WCAG_AAA_LARGE_RATIO}:1): ", end="")
            if result.wcag_aaa_large:
                print_success_message()
            else:
                print_fail_msg()
            consola.print(f"  Delta E (LAB): {result.lab_delta_e:.1f}")

        consola.print(f"  WebAIM URL: {result.webaim_url}")

        # Recolectar fallas
        if not result.wcag_aa_normal:
            failed_aa_normal.append(result)
        if not result.wcag_aa_large:
            failed_aa_large.append(result)

        if mode == ModoAnalisis.AVANZADO:
            if not result.wcag_aaa_normal:
                failed_aaa_normal.append(result)
            if not result.wcag_aaa_large:
                failed_aaa_large.append(result)

    # Resumen
    consola.print(f"\n{'=' * 40}")
    if mode == ModoAnalisis.AVANZADO:
        consola.print("RESUMEN DETALLADO")
    else:
        consola.print("RESUMEN")
    consola.print(f"{'=' * 40}")

    consola.print(f"Total componentes analizados: {len(results)}")
    consola.print(f"Fallan WCAG AA Normal: {len(failed_aa_normal)}")
    consola.print(f"Fallan WCAG AA Large: {len(failed_aa_large)}")

    if mode == ModoAnalisis.AVANZADO:
        consola.print(f"Fallan WCAG AAA Normal: {len(failed_aaa_normal)}")
        consola.print(f"Fallan WCAG AAA Large: {len(failed_aaa_large)}")

        # Análisis de diferencias perceptuales
        if results:
            avg_delta_e: float = sum(r.lab_delta_e for r in results) / len(results)
            consola.print(f"Delta E promedio: {avg_delta_e:.1f}")
            consola.print(
                f"(Delta E > {DELTA_E_THRESHOLD} indica diferencia perceptualmente notable)"
            )

    # Mostrar componentes que fallan usando la función helper
    _print_failed_components("WCAG AA Normal", failed_aa_normal)
    _print_failed_components("WCAG AA Large", failed_aa_large)

    if mode == ModoAnalisis.AVANZADO:
        _print_failed_components("WCAG AAA Normal", failed_aaa_normal)
        _print_failed_components("WCAG AAA Large", failed_aaa_large)


def main() -> int:
    """Función principal"""
    # Parsear argumentos de línea de comandos
    args = parse_arguments()

    # Convierte string a enum
    try:
        analysis_mode: ModoAnalisis = ModoAnalisis.from_string(str(args.modo))
    except ValueError as e:
        print_error_message(str(e))
        return 1

    # Validación para modo avanzado
    if analysis_mode == ModoAnalisis.AVANZADO and not COLORSPACIOUS_AVAILABLE:
        print_warning_message("La librería colorspacious no está instalada.")
        consola.print("Para instalar: pip install colorspacious")
        print_warning_message("Ejecutando en modo normal...")
        analysis_mode = ModoAnalisis.NORMAL

    # Mostrar información del modo seleccionado
    consola.print(f"Modo de análisis: {analysis_mode.value}")
    if analysis_mode == ModoAnalisis.AVANZADO and COLORSPACIOUS_AVAILABLE:
        consola.print("Funciones avanzadas habilitadas: WCAG AAA + Delta E")

    # Cargar configuración de temas
    theme_paths: dict = load_themes_config(args.config)

    if not theme_paths:
        print_error_message("No se pudieron cargar los temas. Verificar configuración.")
        return 1

    consola.print(f"Archivo de configuración: {args.config}")
    consola.print(f"Temas encontrados: {len(theme_paths)}")

    # Procesar cada tema
    for theme_name, theme_path in theme_paths.items():
        try:
            # Cargar tema
            theme_data: dict = load_theme(theme_path)

            # Analizar contraste
            results: List[ContrastResult] = extract_color_pairs(
                theme_data, analysis_mode
            )

            # Imprimir resultados
            print_results(results, theme_name, analysis_mode)

        except FileNotFoundError:
            print_error_message(f"No se encontró el archivo de tema {theme_path}")
        except json.JSONDecodeError:
            print_error_message(f"El archivo {theme_path} no es un JSON válido")
        except (OSError, KeyError) as e:
            print_error_message(f"Error procesando tema {theme_name}: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
