# Definiciones UI Pendientes

Este documento presenta una lista ordenada de todas las definiciones pendientes marcadas con "TASK:" en el documento de especificaciones UI. Estas definiciones deben completarse para cada framework de UI que se implemente.

## Lista de Definiciones Pendientes por Elemento Gráfico

### 0. Definiciones Comunes de Tema

Estas definiciones son compartidas por múltiples elementos y deben definirse una sola vez por tema:

   1. **Familia de fuentes**
      - Definir familia principal para cada OS (Windows: "Roboto", macOS: "SF Display", Linux: "Roboto")
      - Definir tamaño base de fuente (ej: 13px)
      - Definir peso de fuente normal y negrita

   2. **Tamaños de íconos estándar**
      - Definir tamaño pequeño para íconos (ej: 16x16px)
      - Definir tamaño mediano para íconos (ej: 24x24px)
      - Definir tamaño grande para íconos (ej: 32x32px)

   3. **Colores de texto globales**
      - Definir color de texto normal para tema claro y oscuro (ej: "gray10"/"#DCE4EE")
      - Definir color de texto deshabilitado para tema claro y oscuro (ej: "gray60"/"gray45")
      - Definir color de texto placeholder (ej: "gray52"/"gray62")

   4. **Radio de esquinas estándar**
      - Definir radio base para elementos rectangulares (ej: 6px)
      - Definir radio para elementos circulares (1000px para efecto circular completo)

   5. **Grosor de bordes estándar**
      - Definir grosor de borde normal (ej: 1-2px)
      - Definir grosor de borde para elementos enfatizados (ej: 3px)

   6. **Espaciado estándar**
      - Definir espaciado pequeño, mediano y grande para padding/margins
      - Definir espaciado entre elementos (border_spacing)

   7. **Paleta de colores base**
      - Definir color primario para tema claro y oscuro (ej: "#3B8ED0"/"#1F6AA5")
      - Definir color de hover para tema claro y oscuro (derivado del primario)
      - Definir color de fondo principal para tema claro y oscuro
      - Definir colores de borde para tema claro y oscuro
      - Definir colores de alerta/error para tema claro y oscuro
      - Definir colores de advertencia para tema claro y oscuro
      - Definir colores de información para tema claro y oscuro
      - Definir colores alternados para filas de tabla (par/impar)

### 1. Elementos Básicos de Interfaz

   1. **Ventana**
      - Usar color de fondo principal del tema
      - Usar grosor y colores de borde estándar del tema
      - Usar espaciado estándar del tema para padding interno

   2. **Etiquetas**
      - Usar colores de texto globales del tema (normal/deshabilitado)
      - Definir alineación por defecto (izquierda, centro, derecha, justificado)
      - Usar familia y tamaño de fuente del tema

   3. **Campos de texto**
      - Definir colores de fondo específicos para estado editable vs no editable
      - Usar colores de texto globales y placeholder del tema
      - Usar radio de esquinas estándar del tema
      - Usar grosor de borde estándar, definir colores específicos por estado
      - Definir estilo de control emergente: posición relativa, ancho máximo/mínimo, sombra

   4. **Control emergente para mensajes**
      - Definir íconos específicos por tipo: error (⚠️), advertencia (⚠️), información (ℹ️)
      - Usar colores de texto globales del tema
      - Usar colores de alerta/advertencia/información del tema según tipo de mensaje
      - Usar radio de esquinas y grosor de borde estándar del tema
      - Definir estilo del botón de cierre: usar tamaño de ícono estándar, posición, usar colores de hover del tema

   5. **Botones**
      - Usar radio de esquinas y grosor de borde estándar del tema
      - Definir tamaño mínimo específico (ancho x alto en píxeles)
      - Usar familia/tamaño de fuente del tema
      - Usar colores primarios del tema para estados normal/hover/clic
      - Definir estilo de tooltip: posición, retardo de aparición

   6. **Barra de desplazamiento**
      - Definir color específico de la pista/track
      - Definir grosor específico (ancho para vertical, alto para horizontal)
      - Usar radio circular del tema para el thumb/deslizador
      - Definir colores específicos para thumb en estados normal/hover/clic/arrastrar

   7. **Indicador de plegado**
      - Usar colores primarios del tema para estados normal y hover/clic
      - Usar tamaño mediano de íconos del tema
      - Definir símbolos específicos: desplegado (▼), plegado (▶)
      - Definir efectos de transición entre estados

   8. **Paneles**
      - Usar colores de fondo del tema o definir variante específica
      - Usar radio de esquinas y grosor de borde estándar del tema
      - Usar espaciado estándar del tema para padding interno y entre elementos

### 2. Elementos Complejos de Datos

   1. **Tablas**
      - Usar colores alternados del tema para filas pares e impares
      - Usar colores de texto globales y familia/tamaño de fuente del tema
      - Usar grosor de borde estándar del tema, definir colores específicos para bordes
      - Definir estilo de encabezado: usar color de fondo específico, usar colores de texto globales, altura fija, usar fuente del tema en negrita
      - Usar colores primarios del tema para fila seleccionada y colores de hover del tema para fila en hover
      - Definir color específico para espacio reservado de íconos en bordes
      - Definir dimensiones mínimas específicas: altura de filas y ancho de columnas

   2. **Botón de inserción de fila**
      - Definir símbolo específico del ícono: "+" o "➕"
      - Usar colores primarios del tema para estados normal/hover/activación
      - Usar tamaño pequeño de íconos del tema
      - Usar radio de esquinas del tema, definir forma específica (circular/cuadrado)
      - Definir comportamiento específico: aparición solo en hover, retardo, transición

   3. **Botón de eliminación de fila**
      - Definir símbolo específico del ícono: "🗑", "✖" o "−"
      - Usar colores de alerta del tema para estados normal/hover/activación
      - Usar tamaño pequeño de íconos del tema
      - Usar radio de esquinas del tema para el contenedor
      - Definir cuadro de confirmación: dimensiones específicas, usar colores de fondo del tema, usar grosor de borde estándar
      - Usar familia/tamaño de fuente del tema para botones "Cancelar" y "Eliminar"
      - Definir comportamiento específico: aparición, foco inicial en "Cancelar"

## Resumen

**Total de definiciones pendientes:** 18 elementos gráficos (7 comunes + 11 específicos)
**Referencia:** Extraído de `docs/Especificaciones_UI.md`
**Uso:** Estas definiciones deben completarse al implementar cada framework UI para asegurar consistencia visual entre todas las implementaciones.

## Notas para Implementación

- **Priorizar definiciones comunes**: Establecer primero las 6 definiciones comunes de tema para maximizar reutilización
- **Reutilización**: Los elementos específicos deben referenciar las definiciones comunes siempre que sea posible
- **Capacidades por framework**: Cada framework puede tener capacidades nativas diferentes para estos elementos
- **Desarrollo personalizado**: Algunas definiciones pueden requerir desarrollo personalizado según el framework
- **Archivo de configuración**: Se recomienda crear un archivo de constantes/tema para cada framework con estas definiciones
- **Ejemplo de estructura**: Ver archivos de ejemplo en `docs/Temas_ejemplo/` (Blue.json, Oceanix.json) como referencia de organización
