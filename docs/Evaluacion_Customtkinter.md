# Evaluación de CustomTkinter frente a las Especificaciones de UI

## Resumen de fortalezas y limitaciones de CustomTkinter

### Fortalezas principales

- **Personalización visual**

  - **Temas JSON**: permite definir completamente la apariencia de los widgets, incluyendo colores, bordes, radios de esquina y variantes claro/oscuro.
  - **Colores por modo**: todos los colores aceptan tuplas (modo claro, modo oscuro), facilitando la adaptación dinámica.
  - **Fuentes globales**: la clase `CTkFont` permite definir una fuente común a múltiples widgets y modificarla en tiempo real.

- **Escalado y adaptabilidad visual**

  - **Soporte para DPI alto y zoom**: mediante `set_widget_scaling()` y `set_window_scaling()` se puede escalar la interfaz hasta 200% sin distorsión.
  - **Control manual o automático del DPI**, con opción de desactivarlo para ajustes específicos.

- **Diseño responsivo**

  - **Sistema de rejilla (`grid`) con pesos y sticky**: permite crear interfaces que se adaptan al redimensionamiento de la ventana.
  - **`CTkScrollableFrame`**: habilita barras de desplazamiento cuando el contenido excede el espacio disponible.
  - **Frames anidados**: permiten estructurar paneles como sidebar + contenido, con visibilidad controlada dinámicamente.

### Limitaciones y carencias

- **Accesibilidad avanzada**

  - **Sin soporte nativo para lectores de pantalla** (NVDA, VoiceOver): widgets personalizados no exponen semántica ni roles ARIA.
  - **No hay indicadores visuales automáticos de foco**: debe implementarse manualmente.
  - **No hay etiquetas accesibles ni validaciones integradas accesibles**: mensajes emergentes deben crearse usando `Toplevel` u otras herramientas complementarias.

- **Navegación por teclado**

  - **Soporte parcial**: widgets reciben foco y responden a teclas Enter/Espacio, pero no tienen navegación avanzada ni atajos configurables por defecto.

- **Requiere lógica adicional**

  Se **necesita codificación explícita** para:

  - Añadir tooltips accesibles.
  - Gestionar errores o validaciones con foco y lectura.
  - Reflejar cambios visuales accesibles más allá del color (como sombras, íconos, etc.).

***

## 1. Personalización de temas

CustomTkinter permite definir completamente los temas visuales mediante archivos JSON. Cada widget acepta parámetros de color (`fg_color`, `bg_color`, `border_color`, etc.), y todos estos pueden especificarse como tuplas para modos claro y oscuro.

Se puede cargar un tema personalizado con:

```python
customtkinter.set_default_color_theme("Blue.json")
```

Esto aplica automáticamente la paleta definida en el JSON para todos los widgets. Los temas también permiten configurar bordes (`border_width`), esquinas (`corner_radius`) y colores de hover (`hover_color`).

> **Fuente**: [CustomTkinter - Color and Themes](https://customtkinter.tomschimansky.com/documentation/color/#:~:text=All%20colors%20of%20the%20widgets,a%20widget%20is%20called%20fg_color)
> **Fuente**: [CustomTkinter - Cargar archivo de tema](https://customtkinter.tomschimansky.com/documentation/color/#:~:text=A%20theme%20is%20described%20by,method)

Para los textos deshabilitados, los temas pueden definir `text_color_disabled` y otros atributos como `border_color_disabled`. En los temas revisados, esto se usa para asegurar una diferenciación visual clara en estados inactivos.

El único punto a reforzar es la falta de un indicador visual evidente del foco de teclado (ej. al navegar con Tab). No hay soporte nativo para estilos de foco visual, aunque se puede manejar por eventos manualmente.

## 2. Modo de apariencia

CustomTkinter permite alternar entre modo claro, oscuro y automático mediante:

```python
customtkinter.set_appearance_mode("light")  # "dark" o "system"
```

El modo "system" ajusta automáticamente la apariencia según la configuración del sistema operativo (excepto en Linux, donde siempre usará claro).

> **Fuente**: [CustomTkinter - Appearance Mode](https://customtkinter.tomschimansky.com/documentation/appearancemode/#:~:text=The%20appearance%20mode%20decides%2C%20which,time%20with%20the%20following%20command)

Los temas están diseñados para reaccionar correctamente a este ajuste, gracias al uso de tuplas de colores que definen visuales para ambos modos.

## 3. Escalado y zoom

CustomTkinter ofrece soporte completo para escalado tanto automático como programático. Para cumplir con los requerimientos de accesibilidad de zoom hasta 200%, se puede usar:

```python
customtkinter.set_widget_scaling(2.0)
customtkinter.set_window_scaling(2.0)
```

Esto ajusta tanto los controles como las fuentes. También se puede desactivar la detección automática de DPI si se desea controlar completamente el escalado manualmente.

> **Fuente**: [CustomTkinter - Scaling](https://customtkinter.tomschimansky.com/documentation/scaling/#:~:text=HighDPI%20support)

## 4. Tipografía (`CTkFont`)

CustomTkinter utiliza `CTkFont`, una clase que permite definir fuentes reutilizables y modificables. Estas fuentes pueden aplicarse a varios widgets y modificarse dinámicamente para cambiar tamaño, peso o familia de letra:

```python
font = customtkinter.CTkFont(family="Arial", size=14)
label = customtkinter.CTkLabel(master, text="Ejemplo", font=font)
font.configure(size=18)  # se actualiza en tiempo real
```

> **Fuente**: [CustomTkinter - CTkFont](https://customtkinter.tomschimansky.com/documentation/utility-classes/font/#:~:text=There%20are%20two%20methods%20in,a%20tuple%20of%20the%20form)

Los temas como Blue o Oceanix también definen fuentes base (por ejemplo, Roboto para Windows), lo que garantiza consistencia tipográfica.

## 5. Tamaño de controles

Todos los widgets permiten definir explícitamente sus dimensiones. Además, widgets como sliders, scrollbars, switches, checkboxes y radio buttons ofrecen parámetros específicos para agrandar componentes internos:

- `CTkSlider`: `button_length`, `width`, `height`
- `CTkScrollbar`: `width`, `height`, `minimum_pixel_length`
- `CTkCheckBox`: `checkbox_width`, `checkbox_height`
- `CTkRadioButton`: `radiobutton_width`, `radiobutton_height`
- `CTkSwitch`: `switch_width`, `switch_height`

Esto permite cumplir con el requisito de área mínima de 44×44 px para controles táctiles.

> **Fuente**: Documentación general de widgets — ver ejemplos en [CustomTkinter Components](https://customtkinter.tomschimansky.com/documentation/)

## 6. Diseño responsivo (`grid`, scrollbars, colapsables)

CustomTkinter utiliza el sistema de geometría `grid` de Tkinter, que permite distribuir widgets en filas y columnas con pesos (`weight`). Esto posibilita que los elementos crezcan o se contraigan al cambiar el tamaño de ventana.

```python
root.grid_columnconfigure(0, weight=1)
frame.grid(row=0, column=0, sticky="nsew")
```

También existen: `grid_rowconfigure`, `grid_columnconfigure` y `sticky="nsew"`.

> **Fuente**: [CustomTkinter - Grid System](https://customtkinter.tomschimansky.com/tutorial/grid-system/#:~:text=Grid%20geometry%20manager)

Para contenido extenso, se puede usar `CTkScrollableFrame`, que agrega automáticamente scrollbars cuando el contenido excede el espacio disponible.

> **Fuente**: [CustomTkinter - Scrollable Frames](https://customtkinter.tomschimansky.com/tutorial/scrollable-frames/#:~:text=Scrollable%20frame)

Aunque no existen widgets colapsables integrados (como acordeones), se puede simular este comportamiento usando `frame.grid_remove()` y `frame.grid()` para mostrar/ocultar secciones.

## 7. Accesibilidad

CustomTkinter permite:

- Navegación por teclado (los controles reciben foco y pueden activarse con Enter o Espacio), para widgets como `CTkEntry`, `CTkButton`, `CTkCheckBox`, `CTkRadioButton`.
- Estados diferenciados (hover, foco, deshabilitado) con colores configurables.
- Texto de controles deshabilitados en colores atenuados para evitar confusión.

No obstante:

- No se incluye por defecto un indicador visual de foco.
- No existe soporte directo para lectores de pantalla ni etiquetas ARIA.
- La accesibilidad para usuarios con discapacidad visual total dependerá de soluciones externas.

## 8. Recursos adicionales y buenas prácticas

### Accesibilidad y lectores de pantalla

- Tkinter no ofrece soporte nativo para screen readers. CustomTkinter hereda esta limitación, ya que muchos de sus widgets están construidos con `Canvas` o sin semántica accesible.
- Lectores como NVDA o VoiceOver no pueden leer correctamente widgets personalizados.
- Se recomienda agregar:

  - Tooltips descriptivos accesibles.
  - Atajos de teclado (`Alt+Tecla`) para navegación.
  - Ventanas auxiliares (`tk.Toplevel`) con contenido textual legible.

**Fuentes**:

- [Accesibilidad en Tkinter (Tom Talks Python - Medium)](https://medium.com/tomtalkspython/accessibility-in-tkinter-making-your-gui-apps-inclusive-e3ce18e5d35a)
- [CustomTkinter Accessibility Discussion (MochiResearch)](https://mochiresearch.com/2023/11/08/creating-graphical-user-interfaces-with-customtkinter-an-in-depth-guide/)

### Layout responsivo y buenas prácticas

- CustomTkinter permite diseño responsivo mediante:

  - `grid_columnconfigure()` y `grid_rowconfigure()` con pesos (`weight`).
  - `sticky="nsew"` para que los widgets se expandan.
  - Composición de `CTkFrame` anidados.
- Se recomienda estructurar vistas con sidebar + contenido central.

**Fuentes**:

- [Grid System - Documentación oficial](https://customtkinter.tomschimansky.com/tutorial/grid-system/)
- [Scrollable Frames - Documentación oficial](https://customtkinter.tomschimansky.com/tutorial/scrollable-frames/)
- [CustomTkinter tutorial completo (LinkedIn)](https://www.linkedin.com/pulse/customtkinter-complete-tutorial-nuno-bispo-wuehe)

### Buenas prácticas generales

- Usar etiquetas claras y descriptivas (`CTkLabel`).
- Agregar tooltips o ayuda contextual.
- Implementar navegación por teclado robusta.
- Asegurar alto contraste de colores.

**Fuentes**:

- [TomTalksPython - Accesibilidad básica en GUIs](https://medium.com/tomtalkspython/accessibility-in-tkinter-making-your-gui-apps-inclusive-e3ce18e5d35a)
- [Reddit: Coding for screen readers](https://www.reddit.com/r/accessibility/comments/1hd5wuq/where_can_i_learn_to_code_for_a_screenreader/)

## 9. Análisis de los temas Oceanix y Blue

Ver documento consolidado ["Análisis temas CustomTkinter"](Analisis_temas_CustomTkinter.md) para detalles específicos sobre esquinas, bordes, contraste, estados y escalado de widgets en ambos temas. Se recomienda revisar especialmente las secciones de contraste, foco y tamaño mínimo de controles.

## Conclusión general

CustomTkinter cumple con los requerimientos técnicos de personalización, responsividad, escalabilidad y flexibilidad visual, pero requiere refuerzos manuales en el área de accesibilidad avanzada. Los temas Oceanix y Blue son una base sólida pero requieren ajustes en contraste, foco visual y tamaños mínimos para un cumplimiento real de estándares de accesibilidad.
