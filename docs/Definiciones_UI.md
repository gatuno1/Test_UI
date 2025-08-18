# Definiciones UI Pendientes

Este documento presenta una lista ordenada de todas las definiciones pendientes marcadas con "TASK:" en el documento de especificaciones UI. Estas definiciones deben completarse para cada framework de UI que se implemente.

***

## A. Lista de Definiciones Pendientes por Elemento Gráfico

### 1. Definiciones de Tema Visual

Estas definiciones son compartidas por múltiples elementos y deben definirse una sola vez por tema:

   1. **Paleta de colores principal y secundaria**
      - Definir colores para fondo, texto, bordes y estados (hover, activo, deshabilitado)
      - Definir color primario para tema claro y oscuro
      - Definir color de hover para tema claro y oscuro (derivado del primario)
      - Definir color de fondo principal para tema claro y oscuro
      - Definir colores de borde para tema claro y oscuro
      - Definir colores de alerta/error para tema claro y oscuro
      - Definir colores de advertencia para tema claro y oscuro
      - Definir colores de información para tema claro y oscuro

   2. **Estilos de iconos**
      - Definir estilo: línea, relleno
      - Definir tamaño mínimo y máximo para íconos
      - Definir tamaño pequeño para íconos (ej: 16x16px)
      - Definir tamaño mediano para íconos (ej: 24x24px)
      - Definir tamaño grande para íconos (ej: 32x32px)

   3. **Tipografía principal y secundaria**
      - Definir familia principal para cada OS (Windows: "Roboto", macOS: "SF Display", Linux: "Roboto")
      - Definir tamaños de fuente, negritas y cursivas
      - Definir tamaño base de fuente (ej: 13px)
      - Definir peso de fuente normal y negrita
      - Definir color de texto normal para tema claro y oscuro
      - Definir color de texto deshabilitado para tema claro y oscuro
      - Definir color de texto placeholder

   4. **Espaciado mínimo**
      - Definir espaciado pequeño, mediano y grande para padding/margins
      - Definir espaciado entre elementos, márgenes y rellenos
      - Definir espaciado entre elementos (border_spacing)

   5. **Radio de esquinas estándar**
      - Definir radio base para elementos rectangulares (ej: 6px)
      - Definir radio para elementos circulares (1000px para efecto circular completo)

   6. **Grosor de bordes estándar**
      - Definir grosor de borde normal (ej: 1-2px)
      - Definir grosor de borde para elementos enfatizados (ej: 3px)

### 2. Elementos Básicos de Interfaz

   1. **Ventana**
      - Definir color de fondo
      - Definir color de borde y espaciado interno

   2. **Etiquetas**
      - Definir color de texto y alineación por defecto

   3. **Campos de texto**
      - Definir color de fondo y color de texto para estados editable/no editable
      - Definir color de borde para estados normal/hover/clic/foco/edición
      - Definir estilo de control emergente de validación

   4. **Control emergente para mensajes**
      - Definir ícono por estado (error/advertencia/información)
      - Definir color de fondo, color de texto
      - Definir estilo del borde del mensaje emergente
      - Definir ícono del botón de cierre

   5. **Botones**
      - Definir borde, tamaño y color de texto
      - Definir colores de fondo para estados normal/hover/clic
      - Definir estilo de etiqueta emergente descriptiva

   6. **Barra de desplazamiento**
      - Definir color, grosor y estilo de la barra
      - Definir colores para estados normal/hover/clic/arrastrar

   7. **Indicador de plegado**
      - Definir color, tamaño y estilo del icono
      - Definir colores para estados normal/hover/clic

   8. **Paneles**
      - Definir color de fondo, color de borde y espaciado interno

### 3. Elementos Complejos de Datos

   1. **Tablas**
      - Definir color de fondo de celdas, color de texto, color de bordes
      - Definir estilo de encabezado
      - Definir colores alternados para filas
      - Definir colores para estados seleccionada/hover de filas
      - Definir color de fondo para espacio extra de íconos

   2. **Botón de inserción de fila**
      - Definir color, tamaño y estilo del ícono de inserción
      - Definir colores para estados normal/hover/activación

   3. **Botón de eliminación de fila**
      - Definir color, tamaño y estilo del ícono de eliminación
      - Definir colores para estados normal/hover/activación
      - Definir estilo del cuadro de diálogo de confirmación

## Resumen Definiciones Pendientes

**Total de definiciones pendientes:** 14 elementos gráficos (6 definiciones de tema + 8 específicos)
**Referencia:** Extraído de `docs/Especificaciones_UI.md`
**Uso:** Estas definiciones deben completarse al implementar cada framework UI para asegurar consistencia visual entre todas las implementaciones.

## Notas para Implementación

- **Priorizar definiciones de tema**: Establecer primero las 6 definiciones de tema visual para maximizar reutilización
- **Reutilización**: Los elementos específicos deben referenciar las definiciones de tema siempre que sea posible
- **Capacidades por framework**: Cada framework puede tener capacidades nativas diferentes para estos elementos
- **Desarrollo personalizado**: Algunas definiciones pueden requerir desarrollo personalizado según el framework
- **Archivo de configuración**: Se recomienda crear un archivo de constantes/tema para cada framework con estas definiciones
- **Ejemplo de estructura**: Ver archivos de ejemplo en `docs/Temas_ejemplo/` (Blue.json, Oceanix.json) como referencia de organización
- **Framework específico**: Completar detalles según el framework elegido para implementación

***

## B. Elementos Ya Definidos en Temas CustomTkinter

Esta sección presenta los elementos que **YA están definidos** en los temas Oceanix y Blue analizados, basándose en sus archivos JSON de configuración y el análisis detallado en el archivo ["Analisis_temas_CustomTkinter.md"](Analisis_temas_CustomTkinter.md)

Estos elementos pueden utilizarse como base para la implementación, aunque algunos requieren ajustes según las observaciones del análisis.

### 1. Definiciones de Tema Visual (Ya Definidas)

#### **Paleta de colores principal y secundaria**

- **Oceanix**: Usa tonos azul oscuro y verde con pares de colores para modo claro/oscuro
  - Color primario: `["#244461", "#0b2539"]` (botones)
  - Color de hover: `["#375774", "#142e42"]` (botones hover)
  - Color de fondo principal: `["#3b5068", "#3e5365"]` (ventana principal)
  - Colores de borde: `["#5c7998", "#456582"]` (marcos)
- **Blue**: Contraste marcado entre modos con azul brillante como acento
  - Color primario: `["#3B8ED0", "#1F6AA5"]` (botones)
  - Color de hover: `["#36719F", "#144870"]` (botones hover)
  - Color de fondo principal: `["gray92", "gray14"]` (ventana principal)
  - Colores de borde: `["gray65", "gray28"]` (marcos)

#### **Tipografía principal**

- **Ambos temas** definen familias por OS:
  - Windows: "Roboto", tamaño 13px, peso normal
  - macOS: "SF Display", tamaño 13px, peso normal
  - Linux: "Roboto", tamaño 13px, peso normal
- **Colores de texto definidos**:
  - Oceanix: `["white", "#ffffff"]` (normal), `["#aebdcb", "#8396a6"]` (deshabilitado)
  - Blue: `["gray10", "#DCE4EE"]` (normal), `["gray60", "gray45"]` (deshabilitado)
  - Placeholder: Oceanix `["#718ead", "#5c9ec9"]`, Blue `["gray52", "gray62"]`

#### **Radio de esquinas estándar**

- **Oceanix**: Marcos 10px, botones/campos 6px, elementos circulares 1000px
- **Blue**: Marcos 6px, botones/campos 6px, elementos circulares 1000px

#### **Grosor de bordes estándar**

- **Oceanix**: Botones 2px, campos de texto 1px, marcos 0px
- **Blue**: Campos de texto 2px, botones 0px, marcos 0px

#### **Espaciado definido parcialmente** ⚠️

- **Ambos temas** definen `border_spacing: 4` para scrollbars
- **Falta definir**: espaciado pequeño/mediano/grande para padding/margins generales

### 2. Elementos Básicos de Interfaz (Ya Definidos)

#### **Ventana**

- **Color de fondo definido** en ambos temas:
  - Oceanix: `["#3b5068", "#3e5365"]`
  - Blue: `["gray92", "gray14"]`

#### **Etiquetas**

- **Colores de texto definidos**:
  - Oceanix: `["white", "#ffffff"]` (normal y deshabilitado)
  - Blue: `["gray10", "#DCE4EE"]` (normal y deshabilitado)
- **Alineación**: No especificada en JSON (por defecto izquierda)

#### **Campos de texto**

- **Colores de fondo y texto definidos**:
  - Oceanix: fondo `["#375774", "#173145"]`, texto `["white", "#ffffff"]`
  - Blue: fondo `["#F9F9FA", "#343638"]`, texto `["gray10", "#DCE4EE"]`
- **Colores de borde por estado**:
  - Oceanix: `["#5c7998", "#3f5d6c"]` (normal)
  - Blue: `["#979DA2", "#565B5E"]` (normal)
- **Placeholder definido** en ambos temas

#### **Botones**

- **Colores de fondo por estado definidos**:
  - Oceanix: normal `["#244461", "#0b2539"]`, hover `["#375774", "#142e42"]`
  - Blue: normal `["#3B8ED0", "#1F6AA5"]`, hover `["#36719F", "#144870"]`
- **Color de texto**:
  - Oceanix: `["white", "#ffffff"]`
  - Blue: `["#DCE4EE", "#DCE4EE"]`
- **Bordes y esquinas definidos**

#### **Barra de desplazamiento**

- **Colores por estado definidos**:
  - Oceanix: botón `["#173145", "#456582"]`, hover `["#2e4c68", "#22333F"]`
  - Blue: botón `["gray55", "gray41"]`, hover `["gray40", "gray53"]`
- **Estilo**: radio 1000px (circular), border_spacing 4px

#### **Paneles**

- **Colores de fondo definidos**:
  - Oceanix: `["#51667e", "#213844"]` (marcos)
  - Blue: `["gray86", "gray17"]` (marcos)
- **Radio de esquinas**: Oceanix 10px, Blue 6px
- **Espaciado interno**: No explícitamente definido

### 3. Elementos Complejos de Datos (Ya Definidos)

#### **Componentes de tabla disponibles**

- **CTkScrollableFrame** definido en ambos temas:
  - Oceanix: `label_fg_color: ["#5e7690", "#415668"]`
  - Blue: `label_fg_color: ["gray78", "gray23"]`
- **CTkTextbox** con scrollbar definido:
  - Colores de fondo, texto y scrollbar especificados

### 4. Elementos Adicionales Disponibles

#### **Controles de formulario definidos**

- **CTkCheckBox**: colores, bordes, estados hover
- **CTkRadioButton**: estilos circulares, estados seleccionado/no seleccionado
- **CTkSwitch**: colores de progreso y botón
- **CTkSlider**: botón deslizante, colores de progreso
- **CTkComboBox**: menús desplegables con estilos
- **CTkOptionMenu**: menús de opciones
- **CTkSegmentedButton**: botones segmentados

### Resumen de Cobertura

**Elementos completamente definidos**: 12 de 14 elementos principales
**Elementos parcialmente definidos**: 2 elementos (espaciado y algunos aspectos de tablas)
**Elementos no definidos**: Controles emergentes para mensajes, botones de inserción/eliminación de filas
**Referencia**: Extraído desde `docs/Analisis_temas_CustomTkinter.md`

### Observaciones para Implementación

1. **Base sólida**: Los temas proporcionan una base completa para la mayoría de elementos básicos
2. **Ajustes necesarios**: Según el análisis, ambos temas requieren ajustes en contraste, tamaños de controles y escalado
3. **Elementos faltantes**: Los controles emergentes y botones de tabla requieren desarrollo personalizado
4. **Consistencia**: Ambos temas mantienen consistencia en nomenclatura y estructura JSON
