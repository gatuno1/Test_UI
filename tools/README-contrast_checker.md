# Herramientas de Verificación de Contraste

Este directorio contiene dos herramientas especializadas para analizar el contraste de colores en temas CustomTkinter, asegurando el cumplimiento de las pautas de accesibilidad WCAG 2.1.

## Archivos Disponibles

- `contrast_checker.py` - Verificador básico de contraste WCAG
- `contrast_checker_colorspacious.py` - Verificador avanzado con análisis colorimétrico

## contrast_checker.py

### Descripción Básica

Herramienta básica para verificar el contraste de colores en temas CustomTkinter según las pautas WCAG 2.1. Implementa el algoritmo estándar de cálculo de luminancia relativa y ratio de contraste.

### Funcionalidades

- Cálculo de ratio de contraste según WCAG 2.1
- Verificación de cumplimiento WCAG AA (4.5:1 normal, 3:1 texto grande)
- Soporte para colores hex y nombres de colores CSS
- Generación automática de URLs de verificación WebAIM
- Análisis de todos los componentes de texto en temas CustomTkinter

### Componentes Analizados

El programa extrae y analiza automáticamente estos componentes de los archivos JSON de temas:

- `CTkLabel` - Etiquetas de texto
- `CTkButton` - Botones con texto
- `CTkEntry` - Campos de entrada de texto
- `CTkCheckBox` - Casillas de verificación
- `CTkRadioButton` - Botones de radio
- `CTkOptionMenu` - Menús desplegables
- `CTkComboBox` - Cajas combinadas
- `CTkTextbox` - Áreas de texto
- `DropdownMenu` - Menús desplegables personalizados

### Datos Extraídos de los Temas

Para cada componente, el programa lee:

```json
{
  "CTkEntry": {
    "fg_color": ["#375774", "#173145"],
    "text_color": ["white", "#ffffff"],
    "placeholder_text_color": ["#718ead", "#5c9ec9"]
  }
}
```

Donde:

- `fg_color`: Color de fondo [modo claro, modo oscuro]
- `text_color`: Color de texto [modo claro, modo oscuro]
- `placeholder_text_color`: Color placeholder [modo claro, modo oscuro]

### Uso Básico

```bash
python tools/contrast_checker.py
```

### Salida Típica

```text
================================================================================
ANÁLISIS DE CONTRASTE - TEMA: OCEANIX
================================================================================

CTkEntry (light)
  Texto: white | Fondo: #375774
  Ratio: 4.52:1
  WCAG AA Normal (4.5:1): PASA
  WCAG AA Large (3:1): PASA
  WebAIM URL: https://webaim.org/resources/contrastchecker/?fcolor=ffffff&bcolor=375774
```

## contrast_checker_colorspacious.py

### Descripción Avanzada

Herramienta avanzada que utiliza la librería `colorspacious` para análisis colorimétrico preciso. Proporciona cálculos más exactos usando espacios de color CIE XYZ y LAB.

### Funcionalidades Adicionales

- Cálculo de contraste usando espacios de color CIE XYZ
- Análisis Delta E en espacio LAB para diferencias perceptuales
- Verificación WCAG AAA (7:1 normal, 4.5:1 texto grande)
- Estadísticas de diferencias perceptuales promedio
- Análisis colorimétrico científicamente preciso

### Dependencias

```bash
pip install colorspacious
```

### Uso Avanzado

```bash
python tools/contrast_checker_colorspacious.py
```

### Salida Extendida

```text
================================================================================
ANÁLISIS AVANZADO DE CONTRASTE - TEMA: OCEANIX
Usando colorspacious para cálculos precisos
================================================================================

CTkEntry (light)
  Texto: white | Fondo: #375774
  Ratio: 4.52:1
  Delta E (LAB): 67.8
  WCAG AA Normal (4.5:1): PASA
  WCAG AA Large (3:1): PASA
  WCAG AAA Normal (7:1): FALLA
  WCAG AAA Large (4.5:1): PASA
  WebAIM URL: https://webaim.org/resources/contrastchecker/?fcolor=ffffff&bcolor=375774

========================================
RESUMEN DETALLADO
========================================
Total componentes analizados: 18
Fallan WCAG AA Normal: 2
Fallan WCAG AA Large: 0
Fallan WCAG AAA Normal: 12
Fallan WCAG AAA Large: 4
Delta E promedio: 45.3
(Delta E > 3.0 indica diferencia perceptualmente notable)
```

## Utilidad de los Vínculos WebAIM

Los URLs generados automáticamente para WebAIM Contrast Checker proporcionan:

### Verificación Visual Instantánea

- **Vista previa en tiempo real** del contraste entre colores
- **Simulación de texto** en diferentes tamaños y pesos
- **Resultados WCAG** claramente marcados (AA/AAA)

### Análisis Interactivo

- **Ajuste de colores** en tiempo real para mejorar contraste
- **Simulación de daltonismo** para verificar accesibilidad
- **Recomendaciones automáticas** de colores alternativos

### Ejemplo de Uso del Vínculo

<https://webaim.org/resources/contrastchecker/?fcolor=718ead&bcolor=375774>

Este vínculo permite:

1. Ver exactamente cómo se ve el texto `#718ead` sobre fondo `#375774`
2. Verificar si cumple WCAG AA/AAA
3. Ajustar colores si es necesario
4. Obtener alternativas que mejoren el contraste

## Interpretación de Resultados

### Ratios de Contraste WCAG

- **WCAG AA Normal**: ≥ 4.5:1 (texto normal)
- **WCAG AA Large**: ≥ 3:1 (texto grande ≥18pt o ≥14pt en negrita)
- **WCAG AAA Normal**: ≥ 7:1 (nivel máximo de accesibilidad)
- **WCAG AAA Large**: ≥ 4.5:1 (texto grande nivel AAA)

### Delta E (Solo en versión colorspacious)

- **< 1.0**: Diferencia imperceptible
- **1.0-3.0**: Diferencia apenas perceptible
- **3.0-6.0**: Diferencia claramente perceptible
- **> 6.0**: Diferencia muy notable

### Recomendaciones de Uso

1. **WCAG AA** es el estándar mínimo legal en muchas jurisdicciones
2. **WCAG AAA** proporciona accesibilidad superior para usuarios con discapacidades visuales
3. **Delta E > 3.0** asegura que los colores sean perceptualmente diferentes
4. Use los vínculos WebAIM para ajustes visuales y verificación manual

## Archivos de Temas Soportados

Ambas herramientas analizan archivos JSON de temas CustomTkinter ubicados en:

- `docs/Temas_ejemplo/Blue.json`
- `docs/Temas_ejemplo/Oceanix.json`

Para agregar nuevos temas, modifique la variable `theme_paths` en la función `main()` de cualquiera de los scripts.
