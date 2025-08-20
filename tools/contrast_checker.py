#!/usr/bin/env python3
"""
Script para verificar contraste de colores en temas CustomTkinter
Evalúa cumplimiento WCAG 2.1 AA y genera URLs de verificación
"""

import json
import os
from dataclasses import dataclass
from enum import StrEnum
from typing import Dict, List, Tuple

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

# Constantes WCAG
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

# Archivo de configuración de temas
THEMES_CONFIG_FILE = "themes_config.json"


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


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convierte color hex a RGB"""
    hex_color = NAMED_COLORS.get(hex_color, hex_color)

    # Limpia el color hex
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])

    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calcula la luminancia relativa según WCAG 2.1"""

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


def calculate_contrast_ratio(fg_color: str, bg_color: str) -> float:
    """Calcula el ratio de contraste entre dos colores"""
    try:
        fg_rgb = hex_to_rgb(fg_color)
        bg_rgb = hex_to_rgb(bg_color)

        fg_luminance: float = calculate_luminance(fg_rgb)
        bg_luminance: float = calculate_luminance(bg_rgb)

        lighter: float = max(fg_luminance, bg_luminance)
        darker: float = min(fg_luminance, bg_luminance)

        return (lighter + WCAG_CONTRAST_OFFSET) / (darker + WCAG_CONTRAST_OFFSET)
    except (ValueError, KeyError, IndexError):
        return 0.0


def generate_webaim_url(fg_color: str, bg_color: str) -> str:
    """Genera URL para WebAIM Contrast Checker"""
    fg_clean: str = fg_color.lstrip("#")
    bg_clean: str = bg_color.lstrip("#")

    # Convierte colores con nombre a hex sin #
    named_colors_hex = {k: v.lstrip("#") for k, v in NAMED_COLORS.items()}

    fg_clean = named_colors_hex.get(fg_color, fg_clean)
    bg_clean = named_colors_hex.get(bg_color, bg_clean)

    return f"https://webaim.org/resources/contrastchecker/?fcolor={fg_clean}&bcolor={bg_clean}"


def extract_color_pairs(theme_data: Dict) -> List[ContrastResult]:
    """Extrae pares de colores relevantes del tema"""
    results = []

    for component, color_keys in TEXT_COMPONENTS.items():
        if component in theme_data:
            _process_component(theme_data, component, color_keys, results)

    return results


def _process_component(
    theme_data: Dict,
    component: str,
    color_keys: List[str],
    results: List[ContrastResult],
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
            bg_colors: List[str] = FALLBACK_COLORS  # Fallback

    # Procesa ambos modos (claro/oscuro)
    for i, mode in enumerate(ThemeMode):
        text_color: str = _get_color_for_mode(text_colors, i)
        bg_color: str = _get_color_for_mode(bg_colors, i)
        if text_color and bg_color:
            result: ContrastResult = _create_contrast_result(
                component, mode, text_color, bg_color
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
    component: str, mode: str, text_color: str, bg_color: str
) -> ContrastResult:
    """Crea un resultado de contraste para los colores dados"""
    ratio: float = calculate_contrast_ratio(text_color, bg_color)
    webaim_url: str = generate_webaim_url(text_color, bg_color)

    return ContrastResult(
        foreground=text_color,
        background=bg_color,
        component=component,
        mode=mode,
        ratio=ratio,
        wcag_aa_normal=ratio >= WCAG_AA_NORMAL_RATIO,
        wcag_aa_large=ratio >= WCAG_AA_LARGE_RATIO,
        webaim_url=webaim_url,
    )


def load_theme(file_path: str) -> Dict:
    """Carga un archivo de tema JSON"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_results(results: List[ContrastResult], theme_name: str):
    """Imprime resultados de manera formateada"""
    print(f"\n{'=' * 80}")
    print(f"ANÁLISIS DE CONTRASTE - TEMA: {theme_name.upper()}")
    print(f"{'=' * 80}")

    failed_normal: list[ContrastResult] = []
    failed_large: list[ContrastResult] = []

    for result in results:
        status_normal: str = "PASA" if result.wcag_aa_normal else "FALLA"
        status_large: str = "PASA" if result.wcag_aa_large else "FALLA"

        print(f"\n{result.component} ({result.mode})")
        print(f"  Texto: {result.foreground} | Fondo: {result.background}")
        print(f"  Ratio: {result.ratio:.2f}:1")
        print(f"  WCAG AA Normal ({WCAG_AA_NORMAL_RATIO}:1): {status_normal}")
        print(f"  WCAG AA Large ({WCAG_AA_LARGE_RATIO}:1): {status_large}")
        print(f"  WebAIM URL: {result.webaim_url}")

        if not result.wcag_aa_normal:
            failed_normal.append(result)
        if not result.wcag_aa_large:
            failed_large.append(result)

    # Resumen
    print(f"\n{'=' * 40}")
    print("RESUMEN")
    print(f"{'=' * 40}")
    print(f"Total componentes analizados: {len(results)}")
    print(f"Fallan WCAG AA Normal: {len(failed_normal)}")
    print(f"Fallan WCAG AA Large: {len(failed_large)}")

    _print_failed_components("WCAG AA Normal", failed_normal)
    _print_failed_components("WCAG AA Large", failed_large)


def _print_failed_components(
    test_name: str, failed_results: List[ContrastResult]
) -> None:
    """Imprime componentes que fallan una prueba específica"""
    if failed_results:
        print(f"\nComponentes que fallan {test_name}:")
        for result in failed_results:
            print(f"  - {result.component} ({result.mode}): {result.ratio:.2f}:1")


def load_themes_config() -> Dict[str, str]:
    """Carga la configuración de temas desde el archivo JSON"""
    config_path: str = os.path.join(os.path.dirname(__file__), THEMES_CONFIG_FILE)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("themes", {})

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de configuración {config_path}")
        return {}
    except json.JSONDecodeError as e:
        print(
            f"Error: El archivo de configuración {config_path} no es un JSON válido: {e}"
        )
        return {}
    except (OSError, KeyError) as e:
        print(f"Error cargando configuración de temas: {e}")
        return {}


def main():
    """Función principal"""
    theme_paths: dict = load_themes_config()

    if not theme_paths:
        print("No se pudieron cargar los temas. Verificar configuración.")
        return

    for theme_name, theme_path in theme_paths.items():
        try:
            # Carga tema
            theme_data: dict = load_theme(theme_path)

            # Analiza contraste
            results: List[ContrastResult] = extract_color_pairs(theme_data)

            # Imprime resultados
            print_results(results, theme_name)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {theme_path}")
        except json.JSONDecodeError:
            print(f"Error: El archivo {theme_path} no es un JSON válido")
        except (OSError, KeyError) as e:
            print(f"Error procesando {theme_name}: {e}")


if __name__ == "__main__":
    main()
