# Evaluación de temas de color Oceanix y Blue para CustomTkinter

## Introducción

Este informe se enmarca en el proyecto de evaluación de **CustomTkinter** para la creación de interfaces gráficas accesibles y responsivas. Se revisaron las especificaciones de interfaz para determinar si los temas de color nativos de la librería permiten cumplir con los requisitos de accesibilidad, personalización y diseño responsivo definidos en el documento de especificaciones. Para ello se analizaron dos temas proporcionados por la comunidad: **Oceanix** y **Blue**. Se revisaron sus archivos JSON de configuración, así como capturas de pantallas de aplicaciones simples y complejas en sus variantes de modo claro y oscuro.

## Observaciones generales

* Ambos temas presentan un diseño coherente y moderno con esquinas redondeadas y bordes definidos en la mayoría de los widgets. En el tema **Oceanix**, los contenedores (`CTkFrame`) usan un radio de esquina de 10 px y los botones (`CTkButton`) 6 px, con bordes visibles. En el tema **Blue**, las esquinas y bordes son similares: marcos con radio 6 px y botones con bordes claramente definidos. Estas características ayudan a que los elementos sean identificables y cumplen con la recomendación de bordes definidos y tamaño mínimo.

* Los archivos JSON de ambos temas asignan pares de colores para cada widget, uno para modo claro y otro para modo oscuro. Por ejemplo, el botón de Oceanix define un color de fondo azul oscuro para el modo claro y un azul más oscuro para el modo oscuro, mientras que el botón de Blue usa un azul brillante para claro y un azul más oscuro para oscuro. CustomTkinter selecciona automáticamente el color apropiado según el modo de apariencia del sistema, lo que facilita la creación de modos claro y oscuro coherentes.

* Ninguno de los temas implementa por sí mismo funciones de accesibilidad como etiquetas ARIA, roles semánticos o mensajes de error programáticos. Estas características deben implementarse en la lógica de la aplicación y, por tanto, forman parte de futuras fases del proyecto.

## Análisis del tema Oceanix

### Oceanix - Contraste y legibilidad

El tema **Oceanix** utiliza fondos en tonos azul oscuro y verde con texto blanco en casi todos los widgets. Este contraste elevado satisface el requisito de 4,5 : 1 establecido por las WCAG 2.1 para texto normal. No obstante, la variante en modo claro es muy similar al modo oscuro; apenas se aclaran algunos paneles, de modo que usuarios que requieran un fondo claro pueden no notar la diferencia. Además, los estados deshabilitados emplean textos grises claros que reducen el contraste con el fondo oscuro.

### Oceanix - Bordes y formas

Los contenedores (`CTkFrame`) presentan esquinas de 10 px y los botones (`CTkButton`) y campos de texto (`CTkEntry`) tienen un radio de 6 px y bordes de 1 o 2 px. Este diseño cumple con las pautas de tener un borde definido y ayuda a distinguir los controles en la interfaz.

### Oceanix - Tamaño de controles y escalado

En las capturas de pantalla se observa que los mandos de `CTkSlider` y las barras de desplazamiento (`CTkScrollbar`) son pequeños. Las especificaciones exigen un área de toque mínima de 44×44 px para elementos interactivos, por lo que sería necesario aumentar el tamaño de estos componentes mediante parámetros específicos como `button_length`, `width`, `height`, `checkbox_width`, `checkbox_height`, `radiobutton_width`, `radiobutton_height`, y `switch_width`, `switch_height` disponibles en CustomTkinter.

**Corrección importante sobre escalado**: Contrario a la observación inicial, CustomTkinter **sí soporta escalado completo hasta 200%** mediante `customtkinter.set_widget_scaling(2.0)` y `customtkinter.set_window_scaling(2.0)`, cumpliendo plenamente con los requisitos de accesibilidad. El framework también permite desactivar la detección automática de DPI para control manual completo del escalado.

### Oceanix - Indicadores de estado

El tema Oceanix cambia ligeramente el color de fondo o de borde para indicar los estados de hover, foco y selección, pero estas variaciones son sutiles y podrían pasar desapercibidas. La especificación requiere que los estados sean claramente distinguibles y que sus cambios se comuniquen a las tecnologías asistivas.

**Capacidades de CustomTkinter**: El framework permite navegación por teclado (los controles reciben foco y pueden activarse con Enter o Espacio) para widgets como `CTkEntry`, `CTkButton`, `CTkCheckBox`, `CTkRadioButton`. Sin embargo, no incluye por defecto un indicador visual de foco, aunque esto puede manejarse manualmente mediante eventos. Se recomienda incrementar la diferencia de tono o añadir sombras y bordes más gruesos para resaltar los estados.

### Oceanix - Cambios sugeridos

1. **Crear una variante de modo claro real**: definir una paleta de colores con fondos claros y textos oscuros para ofrecer una opción de alto contraste claro, manteniendo la coherencia estética de Oceanix.
2. **Aumentar el tamaño de mandos y scrollbars**: utilizar los parámetros específicos de CustomTkinter como `button_length`, `width`, `height`, `minimum_pixel_length` para sliders y scrollbars, y `checkbox_width`, `radiobutton_width`, `switch_width` para otros controles, alcanzando el área de 44×44 px requerida.
3. **Refinar colores de estados deshabilitados**: utilizar los atributos `text_color_disabled`, `border_color_disabled` disponibles en los temas para mejorar el contraste adecuado.
4. **Implementar indicadores de foco visual**: desarrollar manejo manual de eventos para mostrar indicadores visuales de foco, ya que CustomTkinter no los incluye por defecto.
5. **Aprovechar las capacidades de escalado**: utilizar `customtkinter.set_widget_scaling()` y `customtkinter.set_window_scaling()` para soportar zoom hasta 200% según los requisitos de accesibilidad.

## Análisis del tema Blue

### Blue - Contraste y legibilidad

El tema **Blue** presenta un contraste nítido entre el modo oscuro y el modo claro: en el modo oscuro se utilizan fondos negros con acentos azules brillantes, mientras que en el modo claro se emplea un fondo gris muy claro con texto oscuro. Esta diferencia marcada resulta adecuada para usuarios con distintas preferencias de contraste. Sin embargo, los campos de entrada (`CTkEntry`) muestran texto gris medio sobre un fondo gris, especialmente en la variante oscura; esto puede no cumplir el contraste mínimo y conviene oscurecer el texto o aclarar el fondo. Los elementos deshabilitados usan textos grises muy claros que también reducen la legibilidad.

### Blue - Bordes y formas

Los widgets mantienen un radio de esquina moderado (6 px) y bordes visibles, similar a Oceanix, lo que facilita la identificación de los controles. El color azul se utiliza de manera consistente como acento para botones, radio‑botones y cuadros de selección, generando una estética uniforme.

### Blue - Tamaño de controles y escalado

Los mandos de sliders, scrollbars y flechas de menús son pequeños y requieren ampliación para cumplir la área mínima de toque mediante los parámetros específicos que ofrece CustomTkinter para cada widget (`button_length`, `width`, `height`, `minimum_pixel_length`, etc.).

CustomTkinter soporta escalado completo hasta 200% mediante `customtkinter.set_widget_scaling(2.0)` y `customtkinter.set_window_scaling(2.0)`, cumpliendo plenamente con los requisitos de accesibilidad. El framework también incluye detección automática de DPI y permite control manual del escalado.

### Blue - Indicadores de estado

El tema Blue indica la selección mediante un azul brillante, mientras que los elementos inactivos se muestran en gris. No obstante, la diferencia entre el estado normal y el hover es poco perceptible en algunos controles (por ejemplo, menús y botones), y la especificación requiere que el estado de hover se diferencie claramente. También es importante ofrecer indicadores no cromáticos (sombras, subrayados) para usuarios con daltonismo.

### Blue - Cambios sugeridos

1. **Mejorar contraste en campos de entrada**: emplear texto negro u oscuro sobre fondo claro y blanco sobre fondo oscuro en los `CTkEntry`; reforzar el borde y el color al recibir foco.
2. **Refinar estados de hover y activo**: ajustar la paleta para que el cambio de tono sea más evidente o implementar manejo manual de eventos para añadir sombras/bordes que se activen al pasar el ratón.
3. **Aumentar el tamaño de controles pequeños**: utilizar los parámetros específicos de CustomTkinter (`button_length`, `width`, `height`, `checkbox_width`, etc.) para cumplir con el área mínima de toque.
4. **Aprovechar las capacidades de escalado nativas**: utilizar `customtkinter.set_widget_scaling()` y `customtkinter.set_window_scaling()` para habilitar zoom hasta 200% disponible en el framework.
5. **Implementar indicadores de foco visual**: desarrollar soluciones manuales para indicadores de foco, ya que no están incluidos por defecto en CustomTkinter.

## Tabla comparativa de ventajas y desventajas

| Tema | Ventajas | Desventajas |
|------|--------------------------|------------------------------|
| **Oceanix** | • Paleta coherente de tonos azul y verde<br>• Contraste alto en modo oscuro con texto blanco<br>• Bordes redondeados (6–10 px) y definidos<br>• Colores de acento consistentes para botones y sliders | • Modo claro apenas se diferencia del oscuro<br>• Textos deshabilitados de bajo contraste<br>• Mandos y barras de desplazamiento pequeños por defecto<br>• Diferencias sutiles entre estados normal/hover/selección |
| **Blue** | • Contraste marcado entre modos oscuro y claro<br>• Acento azul vivo que destaca estados seleccionados<br>• Bordes visibles y esquinas moderadas<br>• Paleta diferenciada para cada estado | • Contraste insuficiente en campos de texto y elementos deshabilitados<br>• Cambios de estado hover poco evidentes en algunos controles<br>• Mandos y scrollbars pequeños por defecto |

## Capacidades adicionales de CustomTkinter identificadas

Basándose en la evaluación técnica del framework, se identificaron capacidades importantes no consideradas en el análisis inicial:

### Tipografía avanzada

* **CTkFont**: Permite crear fuentes reutilizables y modificables dinámicamente
* **Configuración por OS**: Los temas definen fuentes específicas (Roboto para Windows, SF Display para macOS)
* **Escalado de fuentes**: Se ajustan automáticamente con el escalado de widgets

### Diseño responsivo

* **Sistema grid**: Utiliza el sistema de geometría `grid` de Tkinter con pesos (`weight`) para layouts responsivos
* **CTkScrollableFrame**: Agrega automáticamente scrollbars cuando el contenido excede el espacio
* **Paneles colapsables**: Aunque no nativos, se pueden implementar usando `grid_remove()` y `grid()`

### Personalización de temas

* **Carga de temas**: `customtkinter.set_default_color_theme("archivo.json")`
* **Modo de apariencia**: `customtkinter.set_appearance_mode("light"/"dark"/"system")`
* **Parámetros específicos**: Cada widget acepta parámetros detallados de color, borde, esquinas, etc.

## Conclusiones

Los temas **Oceanix** y **Blue** proporcionan una base estética atractiva para prototipos en CustomTkinter. Ambos emplean paletas coherentes y utilizan esquinas redondeadas y bordes definidos que cumplen con las pautas de diseño de la especificación.

* **Ambos temas** requieren ajustes en el tamaño de controles pequeños (fácilmente solucionable con parámetros específicos del framework) y mejora en los indicadores visuales de foco (requiere desarrollo manual).

* El tema **Oceanix** necesita desarrollar un modo claro real y mejorar el contraste de textos deshabilitados.

* El tema **Blue** requiere ajustar los colores de campos de entrada y estados deshabilitados, e incrementar la visibilidad del estado de hover.

**Conclusión general**: CustomTkinter demuestra ser un framework robusto que puede cumplir con la mayoría de los requisitos de accesibilidad y diseño responsivo definidos en las especificaciones, con las capacidades nativas necesarias ya disponibles. Los ajustes requeridos son principalmente de configuración y personalización de temas, no limitaciones fundamentales del framework.
