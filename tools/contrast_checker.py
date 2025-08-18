#!/usr/bin/env python3
"""
Script para verificar contraste de colores en temas CustomTkinter
Evalúa cumplimiento WCAG 2.1 AA y genera URLs de verificación
"""

import json
from typing import Dict, List, Tuple
from dataclasses import dataclass


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
    # Maneja colores con nombre como 'gray10', 'white', etc.
    named_colors: Dict[str, str] = {
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

    hex_color = named_colors.get(hex_color, hex_color)

    # Limpia el color hex
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])

    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calcula la luminancia relativa según WCAG 2.1"""

    def gamma_correct(value: float) -> float:
        value = value / 255.0
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    r_linear = gamma_correct(r)
    g_linear = gamma_correct(g)
    b_linear = gamma_correct(b)

    return 0.2126 * r_linear + 0.7152 * g_linear + 0.0722 * b_linear


def calculate_contrast_ratio(fg_color: str, bg_color: str) -> float:
    """Calcula el ratio de contraste entre dos colores"""
    try:
        fg_rgb = hex_to_rgb(fg_color)
        bg_rgb = hex_to_rgb(bg_color)

        fg_luminance = calculate_luminance(fg_rgb)
        bg_luminance = calculate_luminance(bg_rgb)

        lighter = max(fg_luminance, bg_luminance)
        darker = min(fg_luminance, bg_luminance)

        return (lighter + 0.05) / (darker + 0.05)
    except (ValueError, KeyError, IndexError):
        return 0.0


def generate_webaim_url(fg_color: str, bg_color: str) -> str:
    """Genera URL para WebAIM Contrast Checker"""
    fg_clean = fg_color.lstrip("#")
    bg_clean = bg_color.lstrip("#")

    # Para colores con nombre, usa conversión
    named_colors = {
        "white": "ffffff",
        "gray10": "1a1a1a",
        "gray14": "242424",
        "gray17": "2b2b2b",
        "gray20": "333333",
        "gray36": "5c5c5c",
        "gray40": "666666",
        "gray41": "696969",
        "gray45": "737373",
        "gray50": "808080",
        "gray52": "858585",
        "gray53": "878787",
        "gray55": "8c8c8c",
        "gray60": "999999",
        "gray62": "9e9e9e",
        "gray65": "a6a6a6",
        "gray70": "b3b3b3",
        "gray74": "bdbdbd",
        "gray75": "bfbfbf",
        "gray78": "c7c7c7",
        "gray81": "cfcfcf",
        "gray86": "dbdbdb",
        "gray90": "e6e6e6",
        "gray92": "ebebeb",
        "gray100": "ffffff",
        "transparent": "ffffff",
    }

    fg_clean = named_colors.get(fg_color, fg_clean)
    bg_clean = named_colors.get(bg_color, bg_clean)

    return f"https://webaim.org/resources/contrastchecker/?fcolor={fg_clean}&bcolor={bg_clean}"


def extract_color_pairs(theme_data: Dict) -> List[ContrastResult]:
    """Extrae pares de colores relevantes del tema"""
    results = []

    # Componentes con texto que necesitan verificación
    text_components = {
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

    for component, color_keys in text_components.items():
        if component in theme_data:
            comp_data = theme_data[component]

            # Extrae colores de texto y fondo
            text_colors = comp_data.get(color_keys[0], [])
            bg_colors = comp_data.get(color_keys[1], [])

            # Maneja casos donde fg_color es transparente
            if bg_colors == "transparent":
                # Usa el color de fondo del contenedor padre (CTk o CTkFrame)
                if "CTkFrame" in theme_data:
                    bg_colors = theme_data["CTkFrame"].get(
                        "fg_color", ["#ffffff", "#000000"]
                    )
                else:
                    bg_colors = ["#ffffff", "#000000"]  # Fallback

            # Procesa ambos modos (claro/oscuro)
            modes = ["light", "dark"]
            for i, mode in enumerate(modes):
                if isinstance(text_colors, list) and len(text_colors) > i:
                    text_color = text_colors[i]
                elif isinstance(text_colors, str):
                    text_color = text_colors
                else:
                    continue

                if isinstance(bg_colors, list) and len(bg_colors) > i:
                    bg_color = bg_colors[i]
                elif isinstance(bg_colors, str):
                    bg_color = bg_colors
                else:
                    continue

                # Calcula contraste
                ratio = calculate_contrast_ratio(text_color, bg_color)
                webaim_url = generate_webaim_url(text_color, bg_color)

                result = ContrastResult(
                    foreground=text_color,
                    background=bg_color,
                    component=component,
                    mode=mode,
                    ratio=ratio,
                    wcag_aa_normal=ratio >= 4.5,
                    wcag_aa_large=ratio >= 3.0,
                    webaim_url=webaim_url,
                )
                results.append(result)

    return results


def load_theme(file_path: str) -> Dict:
    """Carga un archivo de tema JSON"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_results(results: List[ContrastResult], theme_name: str):
    """Imprime resultados de manera formateada"""
    print(f"\n{'=' * 80}")
    print(f"ANÁLISIS DE CONTRASTE - TEMA: {theme_name.upper()}")
    print(f"{'=' * 80}")

    failed_normal = []
    failed_large = []

    for result in results:
        status_normal = "PASA" if result.wcag_aa_normal else "FALLA"
        status_large = "PASA" if result.wcag_aa_large else "FALLA"

        print(f"\n{result.component} ({result.mode})")
        print(f"  Texto: {result.foreground} | Fondo: {result.background}")
        print(f"  Ratio: {result.ratio:.2f}:1")
        print(f"  WCAG AA Normal (4.5:1): {status_normal}")
        print(f"  WCAG AA Large (3:1): {status_large}")
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

    if failed_normal:
        print("\nComponentes que fallan WCAG AA Normal:")
        for result in failed_normal:
            print(f"  - {result.component} ({result.mode}): {result.ratio:.2f}:1")

    if failed_large:
        print("\nComponentes que fallan WCAG AA Large:")
        for result in failed_large:
            print(f"  - {result.component} ({result.mode}): {result.ratio:.2f}:1")


def main():
    """Función principal"""
    # Rutas de los temas
    theme_paths: Dict[str, str] = {
        "Blue": "docs/Temas_ejemplo/Blue.json",
        "Oceanix": "docs/Temas_ejemplo/Oceanix.json",
    }

    for theme_name, theme_path in theme_paths.items():
        try:
            # Carga tema
            theme_data = load_theme(theme_path)

            # Analiza contraste
            results = extract_color_pairs(theme_data)

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
