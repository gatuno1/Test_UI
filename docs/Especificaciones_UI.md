# Especificaciones interfaz de usuario

Este documento describe las especificaciones de la interfaz de usuario para el proyecto de demostración de diferentes frameworks de Python.
Se requiere comparar e implementar los siguientes:

- CustomTkinter
- Flet
- Kivy
- PySide6
- QtQuick
- Tkinter + ttk
- wxPython

## Introducción

Este documento presenta una propuesta genérica de especificaciones de interfaz de usuario que debe ser evaluada respecto a cada framework de Python. Es fundamental determinar si cada elemento de detalle descrito puede ser implementado de forma natural por cada plataforma o si requiere extensiones o modificaciones específicas para soportarlo adecuadamente.

La implementación de estas especificaciones puede variar significativamente entre frameworks. Algunos elementos pueden estar disponibles de manera nativa, mientras que otros requerirán desarrollo personalizado o el uso de librerías adicionales.

Se recomienda revisar cada especificación contra las capacidades nativas del framework objetivo antes de proceder con la implementación, identificando qué funcionalidades requieren desarrollo adicional y cuáles pueden aprovecharse directamente.

## 1. Diseño de elementos gráficos - Reglas generales

## 1.1. Pautas de Accesibilidad Universal

- **Conformidad con WCAG 2.1 nivel AA:**
  - **Perceptible:** Contraste de colores mínimo 4.5:1 para texto normal, 3:1 para texto grande (>18pt). Contenido no dependiente únicamente del color. Texto redimensionable hasta 200% sin pérdida de funcionalidad.
  - **Operable:** Navegación completa por teclado con orden lógico (`Tab`, `Shift+Tab`). Indicadores de foco visibles con borde de 2px. Sin contenido que cause convulsiones. Área mínima de toque 44x44px para elementos interactivos.
  - **Comprensible:** Texto legible y claro. Funcionalidad predecible. Mensajes de error claros y asociados semánticamente con elementos. Ayuda contextual en entrada de datos complejos.
  - **Robusto:** Compatible con tecnologías asistivas (lectores de pantalla, magnificadores). Código semánticamente correcto con roles y etiquetas ARIA apropiadas.

- **Soporte para tecnologías asistivas:**
  - Lectores de pantalla (NVDA, JAWS, Orca) con anuncios apropiados de cambios de estado y contenido.
  - Magnificadores de pantalla con contenido que se adapta al zoom.
  - Software de reconocimiento de voz con comandos accesibles.
  - Dispositivos de entrada alternativos (switch, eye-tracking).

- **Navegación por teclado universal:**
  - `Tab`/`Shift+Tab` para navegación directa/reversa entre elementos interactivos.
  - `Enter`/`Space` para activar botones y controles.
  - `Enter`/`F2` para editar contenido de controles.
  - Flechas (↑↓←→) para navegación dentro de componentes complejos (tablas, listas).
  - `Home`/`End` para ir al inicio/final de contenido.
  - `Escape` para cancelar acciones o cerrar diálogos.

- **Espaciado y dimensiones accesibles:**
  - Espaciado mínimo de 8px entre elementos interactivos adyacentes.
  - Márgenes de contenido mínimo de 16px desde bordes de contenedores.
  - Altura mínima de 32px para campos de texto y controles de formulario.
  - Área de toque mínima 44x44px con separación de 8px en interfaces táctiles.

- **Indicación de estados accesibles:**
  - Estados de foco, hover, activo y deshabilitado claramente diferenciados visual y programáticamente.
  - Cambios de estado anunciados a tecnologías asistivas.
  - Indicadores de validación accesibles tanto visual como programáticamente.

- TODO: Definir patrones de prueba de accesibilidad durante desarrollo.

## 1.2. Características Comunes de Elementos Gráficos

- **Características comunes:**
  - Todos los elementos gráficos deben tener un diseño consistente y seguir las pautas de estilo del tema visual definido.
  - Deben ser fácilmente identificables y accesibles para el usuario, con color de fondo y borde definido (salvo que se especifique lo contrario).
  - Deben tener tamaño mínimo y alto suficiente para mostrar su contenido, incluso si está vacío, considerando DPI y accesibilidad para pantallas táctiles, mouse y teclado.
  - Deben presentar contraste suficiente entre texto y fondo para garantizar la legibilidad.
  - Deben mantener espaciado adecuado entre sí para evitar solapamientos y mejorar la usabilidad, usando márgenes y rellenos (padding) adecuados. *Nota de implementación:* Utilizar un *Layout manager* nativo del framework para la distribución, alineación y espaciado.
  - Deben mostrar un estado visual claro para indicar si están activos, seleccionados o deshabilitados.
  - Deben ser responsivos, adaptándose al tamaño de la ventana, contenido visible y a la interacción del usuario (hover, clic, selección, etc.). Por defecto, todos los elementos gráficos cambian color de fondo y/o borde al hacer hover, clic o estar seleccionados, salvo que se especifique lo contrario.
  - No deben responder a arrastre, salvo que se especifique lo contrario.
  - El redimensionamiento manual está deshabilitado por defecto, y solo si se especifica se habilita, mostrando borde de selección o indicador visual para arrastrar, cambiando color al hacer hover o arrastrar.
  - Elementos interactivos como botones o campos de texto deben tener tamaño mínimo para facilitar la interacción.
  - Elementos con validación o *parse* de datos deben mostrar el "Control emergente para mensajes", y no en cuadros de diálogos.
    - En este control emergente, se debe mostrar un mensaje de error específico.
    - El usuario debe poder corregir el valor sin perder el foco del campo con validaciones.
  - Todos los elementos gráficos deben tener atributo de visibilidad (`True` por defecto, `False` para ocultar), y si están ocultos no ocupan espacio ni son interactivos.
  - Todos los elementos gráficos deben tener atributo de habilitación (`True` por defecto, `False` para deshabilitar), mostrando estado visual claro si no están disponibles.
  - Todos los elementos gráficos deben tener atributo de anclaje (`None` por defecto), que puede modificarse para anclar a un borde o a otro elemento, manteniendo posición relativa al redimensionar.
  - Elementos pueden tener atributo para ser seleccionados por teclado (`False` por defecto, `True` para permitir foco y navegación con `Tab`), mostrando estado visual claro al recibir foco.
    - Se debe implementar navegación por teclado, con teclas y acciones específicas según el tipo de elemento.
    - Cuando el elemento gráfico contiene otros que también pueden ser seleccionados por teclado, la la especificación debe indicar el orden o lógica de navegación entre ellos.
  - TASK: Completar detalles según el framework elegido.

- **Tema visual:**
  - Bordes del elemento gráfico:
    - Color: Activo, deshabilitado, resaltado.
    - Grosor
    - Permite bordes redondeados: Verdadero/Falso.
    - Radio Bordes redondeados: En caso de soportarse.
  - Los iconos existen en 3 tamaños: pequeño, mediano y grande.
  - TASK: Completar detalles según el framework elegido:
    - Definir paleta de colores principal y secundaria para fondo, texto, bordes y estados (activo, deshabilitado, resaltado).
    - Definir estilos de iconos: línea, relleno, tamaños en píxeles para cada tamaño.
    - Definir tipografía principal y secundaria, tamaños de fuente, negritas y cursivas.
    - Definir espaciado mínimo entre elementos, márgenes y rellenos.

- **Ventana:**
  - Tamaño mínimo de ventana: 800x600 píxeles.
  - Al inicializarse debe estar en estado maximizado por defecto.
  - Permite redimensionamiento por parte del usuario.
  - Muestra barra de desplazamiento vertical u horizontal si el contenido excede el área visible.
  - No cambia color de fondo o bordes al hacer hover, clic o arrastrar en el espacio vacío de la ventana.
  - Se debe implementar soporte para zoom de ventana, sin pérdida de funcionalidad hasta 200%.
  - TASK: Falta definir color de fondo, color de borde y espaciado interno.

- **Etiquetas:**
  - Tamaño de fuente por defecto igual al texto normal, con alineación a la izquierda por defecto.
  - Sin borde ni color de fondo distintivo, no cambian de color al hacer hover o clic, salvo que se especifique lo contrario.
  - La alineación puede ser a la izquierda, derecha o centrada.
  - Permiten ajuste de palabras (wordwrap) y multi-línea si es necesario.
  - No son interactivos ni seleccionables, salvo que se especifique lo contrario.
  - Para el lector de pantalla, considerar etiqueta ARIA que diga "{Nombre de la etiqueta}" para indicar que es una etiqueta informativa.
  - TASK: Falta definir color de texto y alineación por defecto.

- **Botones:**
  - Color de fondo cambia al hacer hover o clic.
  - Texto centrado por defecto, puede alinearse según se requiera.
  - Solo se usan botones con texto descriptivo, o con íconos si son acciones simples.
  - Al hacer hover, se muestra una etiqueta emergente con descripción alternativa de la acción del botón.
  - Para el lector de pantalla, considerar etiqueta ARIA que diga "Botón {Nombre del botón}" para indicar que es un botón interactivo.
  - TASK: Falta definir borde, tamaño y color de texto, colores de fondo para estados normal/hover/clic, y estilo de etiqueta emergente descriptiva.

- **Campos de texto:**
  - Texto alineado según se requiera, izquierda por defecto.
  - Permiten ajuste de palabras (wordwrap) y texto multi-línea si es necesario.
  - Si es editable, el usuario puede modificar el texto; si no, solo puede seleccionarlo.
  - Al hacer hover, clic o recibir foco por teclado: el borde cambia de color para indicar interactividad.
  - Al estar en edición, colores de fondo y texto cambian según estado editable o no.
  - Entrar en edición por clic o teclado (`Enter`/`F2`):
    - Si el campo está vacío, el cursor se posiciona al inicio.
    - Si tiene texto, el texto se muestra preseleccionado por completo, con el cursor en la posición del clic, o al final si se llegó por teclado.
  - Validación al perder foco o presionar `Enter`. Si validación o *parse* de datos falla, muestra el control emergente de mensajes con estado y descripción de error específica.
  - Edición termina con `Escape` o `Tab`, restaurando el valor anterior si el nuevo es inválido.
  - Para lector de pantalla, considerar etiqueta ARIA que diga "{Nombre del campo}, campo de texto" para indicar que es un campo editable. Si no es editable, usar "{Nombre del campo}, etiqueta de texto" para indicar que es solo informativo.
  - TASK: Definir color de fondo y color de texto para estados editable/no editable, color de borde para estados normal/hover/clic/foco/edición, y estilo de control emergente de validación.

- **Control emergente para mensajes:**
  - Se muestra cerca del elemento vinculado, afectado por validación no exitosa.
  - El elemento gráfico que invoca a este control emergente debe especificar el estado del mensaje y el texto a mostrar.
  - El control emerge del borde del elemento gráfico que genera el mensaje, anclándose a los bordes de este:
    - Por defecto anclado en el borde inferior del elemento vinculado, con ambos alineados en su margen izquierdo.
    - En cambio, si el elemento está cerca del borde derecho del contenedor del elemento vinculado, el control se alinea con el borde derecho del elemento.
    - Si el elemento está en el límite inferior visible, el control se ancla en el borde superior del elemento vinculado.
    - Debe mantener un margen específico respecto al otro control.
  - El Control tiene borde y color de fondo específicos.
    - Al hacer hover, clic o recibir foco por teclado: el borde cambia de color desde normal a resaltado, para indicar interactividad.
    - El color de fondo es fijo según el tipo de Estado a representar (Error, Advertencia, Información) y se mantiene mientras el control esté visible.
  - El área interna del control contiene una grilla 1x2 de alineamiento horizontal, sin margen respecto al borde.
    - El área izquierda está destinada al icono de Estado, mientras el área derecha se subdivide en otra grilla 2x1, entre el área superior que contiene el botón de cierre y la inferior donde está la etiqueta con Mensaje.
    - Ícono de Estado está anclado al borde superior izquierdo de la grilla, con un margen adecuado.
    - Botón de cierre está anclado al borde superior derecho de la celda con un margen de 0px respecto a ambos bordes.
    - La etiqueta con mensaje está centrada horizontal y verticalmente respecto a su celda, con un margen adecuado. La etiqueta y celda se expanden según el contenido de la primera.
  - El ícono de estado es de tamaño mediano, y su imagen según categoría: Error (  ), Advertencia (  ), Información (  ).
  - La etiqueta con Mensaje permite texto multilínea y con Word wrap habilitado.
  - Botón de cierre con ícono pequeño (  ) para ocultar el mensaje mediante clic o teclado.
  - Cuando el control recibe el foco por clic o teclado, se selecciona el botón de cierre. *Nota de implementación:* Los eventos de teclado en cualquier parte del control se redirigen automáticamente al botón de cierre para su procesamiento.
  - Debe ser accesible por tecnologías asistivas, incluyendo etiquetas ARIA apropiadas (nombre del campo asociado, estado del mensaje, texto del mensaje).
  - TASK: Definir colores específicos para fondo fijo por tipo de mensaje (error/advertencia/información), colores de borde para estados normal vs. resaltado, estilo de texto, margen respecto al control vinculado, márgenes internos de la grilla y elementos, tiempo de auto-ocultación (opcional), animaciones de aparición/desaparición del control emergente.

- **Barra de desplazamiento:**
  - Visible solo si el contenido excede el área visible.
  - Cambia de color al hacer hover, clic o arrastrar.
  - Implementar navegación alternativa con teclas `Page Up`/`Page Down`, `Home`/`End`, y flechas (↑↓←→).
  - TASK: Falta definir color, grosor y estilo de la barra, colores para estados normal/hover/clic/arrastrar.

- **Indicador de plegado:**
  - Botón con ícono definido y visible en el borde superior izquierdo del panel.
  - Ícono indica estado: plegado (`▶`) o desplegado (`▼`).
  - Al hacer clic, o presionar tecla `Space` o `Enter` sobre este, alterna entre estados.
  - Cambia color al hacer hover o clic.
  - Para lector de pantalla, considerar etiqueta ARIA que diga "Indicador de plegado, estado {estado actual}" para indicar el estado del panel.
  - TASK: Falta definir color, tamaño y estilo del icono, colores para estados normal/hover/clic.

- **Paneles:**
  - Puede tener título en la parte superior, alineado a la izquierda por defecto.
  - Paneles plegables muestran indicador de plegado.
  - Fondo que contraste con texto y elementos internos.
  - Por defecto sin borde, salvo que se especifique.
  - Para accesibilidad implementar estructura de encabezados jerárquica (h1, h2, h3) y derivando landmarks ARIA para navegación rápida.
  - TASK: Falta definir color de fondo, color de borde y espaciado interno.

- **Tablas:**
  - Permite desplazamiento horizontal y vertical si el contenido excede el área visible.
  - Encabezado distinguible, con fondo y texto contrastantes, no permite cambiar nombre, orden ni alto.
  - Encabezado tiene alto fijo y siempre visible al hacer scroll vertical (anclado arriba).
  - Filas alternan colores para legibilidad.
  - Alto mínimo para mostrar encabezado y fila vacía al final; atributo para cantidad de filas visibles (por defecto 3, mínimo 1).
  - Al cargar datos, genera filas según datos y siempre incluye una fila vacía al final para agregar nuevos registros, sin usar campos de texto aparte.
  - Filas cambian de color al estar seleccionadas o al hacer hover.
  - Filas sin bordes entre ellas, pero con margen especificado como atributo.
  - Alto de fila determinado por celda más alta, no cambia al hacer scroll. Incluso sin datos, la fila debe tener alto mínimo suficiente para mostrar una línea de texto.
  - Columnas tienen borde entre ellas, con margen entre celdas, especificado como atributo.
  - Columnas permiten redimensionamiento manual de ancho, salvo indicación contraria, y se autoajustan al hacer clic en el borde entre ellas.
  - Ancho mínimo calculado automáticamente según contenido, no cambia al hacer scroll horizontal.
  - Celdas no permiten modificar alto manualmente, pero sí indirectamente por contenido.
  - Celdas tienen mismo comportamiento que campos de texto respecto a interacción, validaciones, *parse* y mensajes de error.
  - Navegación por teclado desde otro control elemento gráfico externo: se debe seleccionar la primera celda izquierda de la primera fila.
  - Navegación entre celdas: Usar flechas (↑↓←→) para moverse entre celdas individuales.
  - Edición de celda: Presionar `Enter` o `F2` en la celda seleccionada para editarla.

  - Navegación entre filas:
    - Estando seleccionada una celda, usar `Tab` para seleccionar la fila completa.
    - Estando seleccionada una fila, tecla `Tab` navega a la fila siguiente, con `Shift+Tab` haciendo lo inverso.
      - Si la fila es la última de la tabla, se sale de ésta yendo al control siguiente.
      - Si la fila es la primera de la tabla, se pasa a la navegación en encabezado.
      - Sí se presiona la flecha arriba (↑) o abajo (↓), se selecciona respectivamente la fila superior o inferior a la actual, excepto en caso de los extremos:
        - Si es la primera fila y se presiona la flecha arriba (↑), se pasa a la navegación en encabezado.
        - Si es la última fila y se presiona la flecha abajo (↓), se sale de la tabla yendo al control siguiente.
      - **TODO**: Agregar navegación a botones de inserción de fila y de eliminación de fila, utilizando flechas izquierda y derecha.

  - Estando seleccionada una fila, si se presiona flecha izquierda (←), flecha derecha (→), `Home` o `End` se entra al modo de navegación entre celdas, variando cual es la celda seleccionada:
    - Si se presiona la flecha izquierda (←) o tecla `Home`, el foco pasa a la primera celda a la izquierda de la fila.
    - Sí se presiona la flecha derecha (→) o tecla `End`, el foco pasa a la última celda a la derecha de la fila.

  - Navegación en encabezados de tabla:
    - Cuando se entra a este modo de navegación de una fila del la misma tabla, se selecciona por defecto la primera celda de la izquierda del encabezado. En cambio, cuando se entra desde una celda se mantiene la misma columna desde donde venía.
    - Usar tecla flecha izquierda (←) o derecha (→) para moverse entre celdas del encabezado, seleccionando una a una.
    - Si se presiona la tecla flecha abajo (↓), regresa a la primera fila de datos.
    - Si se presione la tecla flecha arriba (↑) o `Shift+Tab`, se sale de la tabla yendo al control anterior.
    - Si se presione la tecla `Tab`, se navega a la primera fila de datos.

  - Para el lector de pantalla, asegurar encabezados asociados semánticamente con celdas de datos (por ejemplo, al navegar a celda en columna producto, fila 3, se anuncia "Producto {contenido celda}, fila 3 de {número total de filas con datos A ver}").
  - Las filas deben reservar espacio extra en el borde izquierdo y derecho de la tabla para mostrar un ícono en cualquiera de los costados. Este espacio se rellena del mismo color de la fila, y permite implementar elementos gráficos para insertar o eliminar filas.
  - TASK: Falta definir color de fondo de celdas, color de texto, color de bordes, estilo de encabezado, colores alternados para filas, colores para estados seleccionada/hover de filas, y color de fondo para espacio extra de íconos.

- **Botón de inserción de fila:**
  - Se muestra como un ícono (por ejemplo, `+`) únicamente al hacer hover con el mouse sobre el espacio entre filas, no sobre una fila.
  - El ícono debe ser claramente visible y cambiar de color al hacer hover.
  - Al hacer clic en el ícono o usar Ctrl+Insert, se inserta una nueva fila vacía en la posición correspondiente.
  - Al tener una fila seleccionada y presionar `Ctrl+Insert`, se inserta una nueva fila vacía justo debajo de la fila seleccionada.
  - El botón debe mostrar un estado visual de activación al hacer clic.
  - La nueva fila debe crearse con celdas vacías y lista para edición inmediata, posicionando el cursor en la primera celda editable de la nueva fila.
  - No debe mostrar el ícono de inserción ni activarse por teclado entre la penúltima fila de datos y la fila vacía al final de la tabla.
  - TASK: Definir color, tamaño y estilo del ícono de inserción, colores para estados normal/hover/activación.

- **Botón de eliminación de fila:**
  - Se muestra como un ícono (por ejemplo, de basurero `🗑` o `-`) al hacer hover con el mouse sobre el borde de la fila, o teniendo la fila seleccionada.
    - Con fila seleccionada presionar `Supr` es equivalente al hacer clic sobre el icono: requiere confirmación de eliminación solo si la fila contiene datos.
    - Confirmación de eliminación muestra cuadro de diálogo del sistema (estilo advertencia), con botones "Cancelar" y "Eliminar" con foco en botón de cancelar. Debe ser accesible por teclado.
  - El botón cambia de color al hacer hover.
  - Debe tener tamaño suficiente para ser fácilmente interactuable en pantallas táctiles y con mouse.
  - No debe permitir eliminar la última fila vacía destinada a agregar nuevos datos.
  - TASK: Definir colores para estados normal/hover/activación.

---

## 2. Requisitos específicos de la interfaz de usuario

- La interfaz a construir debe ser intuitiva y fácil de usar, siguiendo las mejores prácticas de UI/UX.
- Debe mostrar características responsivas y adaptarse a diferentes tamaños de ventana (ver "Características comunes" y "Comportamiento responsivo esperado").
- Se requiere implementar como un formulario con varias secciones que agrupan *widgets* de interfaz gráfica, como etiquetas, iconos, campos de texto, botones, barra de desplazamiento, tablas o paneles.
- Debe permitir la visualización de una previsualización de la cotización dentro de un panel dedicado.
- Algunos paneles deben permitir el plegado y despliegue de contenido para mostrar todo o sólo algunos elementos.

### Simbología utilizada en los Diagramas

La interfaz de usuario requerida se describe por medio de diagramas ASCII que representan gráficamente diferentes elementos de la interfaz, la relación entre ellos, como que un panel está ubicado antes que otro, la relación entre padre e hijos cuando un elemento contiene a otros dentro de su espacio, o la alineación y ubicación relativa de elementos gráficos.

- **Caracteres:**

  Los caracteres ASCII se utilizan para crear bordes, líneas y otros elementos gráficos de la interfaz. Estos caracteres permiten representar visualmente los componentes de la interfaz de usuario de manera clara y organizada.

  - Bordes: `┌─`, `└─`, `─┐`, `─┘`, `│`.
  - Líneas horizontales: `─`.
  - Líneas verticales: `│`.
  - Espacios en blanco: ` ` (espacio).

- **Texto:**

  El texto se representa con llaves `{}` para etiquetas, y con signos de menor y mayor `< >` para campos de texto. Los textos dentro de los botones no llevan signos.

  - Etiqueta: `{Etiqueta}`.
  - Campo de texto: `<Campo de texto>`.
  - Botón: `Botón`.

- **Bordes:**

  Los bordes de la ventana, botones, campos de texto, etiquetas y secciones se muestran con caracteres ASCII específicos para crear una interfaz visualmente clara y organizada.

  - Bordes de la ventana: `┌─`, `└─`, `─┐`, `─┘`.
  - Bordes verticales: `│`.
  - Bordes horizontales: `─`.

- **Ventana:**

  La ventana es el contenedor principal de la interfaz, y se representa con un borde completo.

  - Borde completo: `┌─`, `└─`, `─┐`, `─┘`.

- **Etiqueta:**

  Una etiqueta es un texto que se muestra sin bordes dentro de un panel, y se representa entre llaves '{}'. Sirve para mostrar información estática que no requiere interacción del usuario y pueden estar alineadas a la izquierda, derecha o centradas, según se requiera.

  El ejemplo siguiente muestra una etiqueta con el texto "Etiqueta 1", dentro de un panel alineada a la izquierda en sentido horizontal, y al centro en sentido vertical.

  > ```asciiart
  > ┌────────────────────────────┐
  > │                            │
  > │ {Etiqueta 1}               │
  > │                            │
  > └────────────────────────────┘
  > ```

- **Botones:**

  El texto dentro de los botones se representa sin signos en esta especificación de interfaz, y el borde del botón es completo.

  El ejemplo siguiente muestra primero un botón con el texto "Botón 1" y después uno sólo con ícono de borrado (representado como basurero `🗑`).

  > ```asciiart
  > ┌───────────────┐
  > │    Botón 1    │
  > └───────────────┘
  > ┌───────────────┐
  > │      🗑        │
  > └───────────────┘
  > ```

- **Campo de texto:**

  Los campos de texto también se representan con un borde completo, pero se diferencian de los botones por mostrar el nombre del campo entre signos de menor y mayor '<>'. Además, la posición del texto dentro del campo de texto muestra la alineación requerida para los datos del campo.

  El ejemplo siguiente muestra tres campos de texto, alineados al borde izquierdo, centrado y derecho, respectivamente.

  > ```asciiart
  > ┌─────────────────────────────────────────────┐
  > │ <Campo de texto alineado a la izquierda>    │
  > └─────────────────────────────────────────────┘
  > ┌─────────────────────────────────────────────┐
  > │           <Campo de texto centrado>         │
  > └─────────────────────────────────────────────┘
  > ┌─────────────────────────────────────────────┐
  > │      <Campo de texto alineado a la derecha> │
  > └─────────────────────────────────────────────┘
  > ```

- **Control emergente para mensajes:**

  El control emergente para mensajes se representa como un cuadro con borde que emerge del borde del elemento gráfico que genera el mensaje.

  El ejemplo siguiente muestra un panel que contiene un cuadro de texto, con el control emergente con un mensaje de error, considerando que tiene espacio suficiente para mostrarse hacia abajo y a la derecha, que es el comportamiento por defecto. Esto se traduce en que el control emergente está anclado al borde inferior y alineado al costado izquierdo del elemento gráfico al cual está vinculado.

  > ```asciiart
  > ┌───────────────────────────────────────────┐
  > │        ┌─────────┐                        │
  > │  Costo:│  -$1.234│                        │
  > │        └─────────┘────────────────┐      │
  > │        │   {Etiqueta con mensaje} │      │
  > │        └───────────────────────────┘      │
  > │                                           │
  > └───────────────────────────────────────────┘
  > ```

Si en cambio, el elemento gráfico del cual emerge está en el límite inferior visible de la ventana o panel, el control emergente debería mostrarse hacia arriba del elemento gráfico.

  > ```asciiart
  > ┌────────────────────────────────────────────────┐
  > │                                                │
  > │        ┌───────────────────────────────┐      │
  > │        │   Error: El costo debe ser un │      │
  > │        │    un valor superior a cero.   │      │
  > │        ┌─────────┐──────────────────────┘      │
  > │  Costo:│  -$1.234│                             │
  > │        └─────────┘                             │
  > └────────────────────────────────────────────────┘
  > ```

Sin embargo, si dada la posición o alineación del elemento gráfico del que emerge este se encuentra por ejemplo al borde derecho de la ventana o del panel, el control emergente debe alinearse con el borde derecho del elemento gráfico. En el siguiente diagrama de ejemplo ambos efectos ocurren simultáneamente.

  > ```asciiart
  > ┌────────────────────────────────────────────────┐
  > │                                                │
  > │                ┌─────────────────────────────┐│
  > │                │  Error: El costo debe ser un││
  > │                │   un valor superior a cero.  ││
  > │                └────────────────────┌─────────┐│
  > │                               Costo:│  -$1.234││
  > │                                     └─────────┘│
  > └────────────────────────────────────────────────┘
  > ```

- **Barra de desplazamiento:**

  La barra de desplazamiento permite al usuario desplazarse verticalmente (y opcionalmente horizontalmente) por el contenido de un formulario o panel cuando este excede el área visible de la ventana o contenedor.

  Se representa como una banda vertical o horizontal ubicada en el borde derecho o inferior del área desplazable, respectivamente.

- **Indicador de plegado**

  Este indicador implementa un icono en el programa a construir, que representa si un panel está plegado o desplegado.
  Cuando un panel se muestra desplegada, significa que se deben mostrar todos los componentes gráficos que tienen activado el atributo `MOSTRAR_DESPLEGADO`, mientras que los que no lo tienen activado se deben ocultar. A su vez, cuando el panel se muestra plegado, significa que se deben mostrar todos los componentes gráficos con el atributo `MOSTRAR_PLEGADO`, y ocultar los que no lo tengan activo.

  La tabla muestra el símbolo, significado y las acciones a realizar cuando se hace clic en cada uno:

  | Símbolo | Significado                  | Que mostrar        | Acción en clic  |
  |:-------:|------------------------------|--------------------|-----------------|
  |   `▼`   | Panel desplegado (expandido) | Contenido completo | Plegar panel    |
  |   `▶`   | Panel plegado (colapsado)    | Contenido mínimo   | Desplegar panel |

  - Sugerencia de implementación para atributo:
    Clase `TipoPlegado` - Implementar como una clase que herede de `enum`, especificando que actúan como flag, con instancias `NEUTRO`, `MOSTRAR_DESPLEGADO`,  `MOSTRAR_PLEGADO`.

- **Panel:**

  Un Panel puede contener etiquetas, campos de texto, botones o tablas. Puede tener un título o no, y puede ser plegable o no.

  Los paneles se representan aquí con un borde completo aunque en la implementación no lo tengan, y un indicador de plegado si tienen capacidad de desplegarse/plegarse. Los paneles que no tienen capacidad de plegado se muestran sin ese indicador.

  - **Ejemplo de panel sin título**

    Si el panel no tiene título, se representa con un borde completo y los elementos contenidos en éste. Los elementos se muestran alineados según se requiera.

    > ```asciiart
    > ┌─────────────────────────────────────────────────┐
    > │                ┌──────────────┐ ┌─────────────┐ │
    > │  {Etiqueta 1}  │    Botón 1   │ │   Botón 2   │ │
    > │                └──────────────┘ └─────────────┘ │
    > └─────────────────────────────────────────────────┘
    > ```

  - **Ejemplo de panel con título**

    Si el panel tiene un título, este se muestra en la parte superior del elemento gráfico, seguido de los elementos contenidos en ella. El título se muestra con el texto alineado según se requiera (izquierda, centrado, derecha).

    > ```asciiart
    > ┌─Título─de─panel─────────────────────────────────┐
    > │                ┌──────────────┐ ┌─────────────┐ │
    > │  {Etiqueta 1}  │    Botón 1   │ │   Botón 2   │ │
    > │                └──────────────┘ └─────────────┘ │
    > └─────────────────────────────────────────────────┘
    > ```

  - **Ejemplo de Panel Desplegado**

    Si el panel está desplegado, el indicador se representa con el carácter '▼' en el borde superior izquierdo.

    > ```asciiart
    > ┌─ ▼ Título─de─panel──────────────────────────────┐
    > │                ┌──────────────┐ ┌─────────────┐ │
    > │  {Etiqueta 1}  │    Botón 1   │ │   Botón 2   │ │
    > │                └──────────────┘ └─────────────┘ │
    > └─────────────────────────────────────────────────┘
    > ```

  - **Ejemplo de Panel Plegado**

    Si el panel está plegado, el indicador se representa con el carácter '▶' en el borde superior izquierdo.

    Los elementos contenidos en el panel plegado se pueden mostrar o no, dependiendo si se establece que deben mostrarse al estar plegados, que deben ser implementados como una propiedad de los elementos gráficos contenidos dentro de este panel.

    En el ejemplo siguiente, se considera que es el mismo panel del ejemplo anterior,salvo que ahora está plegada y en cambio muestra dos etiquetas. La etiqueta de "Etiqueta 1" tiene la propiedad de mostrarse tanto al estar plegada como desplegada, mientras que la etiqueta de "Etiqueta 2" sólo se muestra al estar plegada. Por otro lado, los botones no se muestran al estar plegado el panel, pues en este ejemplo no se ha establecido que deban mostrarse al estar plegados.

    > ```asciiart
    > ┌─ ▶ Título─de─panel──────────────────────────────┐
    > │  {Etiqueta 1}                     {Etiqueta 2}  │
    > └─────────────────────────────────────────────────┘
    > ```

- **Tabla:**

  Una tabla es un elemento gráfico que contiene otros elementos gráficos: una fila de encabezados y múltiples filas de datos alineados en una grilla. En sentido vertical, contiene encabezados de columna en la primera fila, y luego continúan celdas de datos alineadas en una grilla.

  La tabla se representa en esta especificación con un borde completo alrededor, las columnas se representan con caracteres `|` entre las celdas, mientras que las filas de la grilla sólo se representan con cambios de línea y bordes horizontales. Nota: Por limitaciones del formato asciiart no se puede representar los espacios entre filas, ni bordes entre celdas, aunque sí se requiera.

  La especificación de una tabla contiene los encabezados de columna en la primera fila, la segunda fila la alineación de cada columna, y luego siguen las filas de datos. Los encabezados especifican el nombre de cada columna y también siguen la alineación especificada para cada columna.

  - **Alineación de datos en la Tabla**

    Los datos en la tabla pueden alinearse a la izquierda, derecha o centrados. La alineación se indica con guiones precedidos o terminados con dos puntos ':' al borde izquierdo o derecho de la celda. Así, ':----' indica que los datos están alineados a la izquierda, '----:' indica que están alineados a la derecha, y ':---:' indica que están centrados. Adicionalmente, si no se especifica la alineación, como en '-----', se asume que los datos están alineados a la izquierda.

    En el siguiente ejemplo, se muestra una tabla con tres columnas: "Item" tiene alineación a la derecha, "Producto" a la izquierda, y "Cantidad" especifica datos centrados.

    > ```asciiart
    > ┌───────────────────────────────┐
    > │   Item|Producto  |  Cantidad  │
    > │------:|:---------|:----------:│
    > │      1|ABC       |     3      │
    > │      2|XYZ       |     9      │
    > └───────────────────────────────┘
    > ```

## 3. Diagramas con especificación de interfaz para el programa

A continuación, cada diagrama especifica las características de la interfaz el usuario a construir, en sus diferentes estados. Cada elemento gráfico a construir debe tomar su atributos y estados iniciales a partir de lo descrito en estos diagramas. así valores como el nombre, tipo de objeto gráfico, alineación, pertenencia a otro elemento gráfico, anclaje al borde u otro objeto gráfico, visibilidad al desplegarse o plegarse el panel, descripción de que acción hace un botón, u otros, deben determinarse a partir de estos diagramas.

- Formulario dentro de ventana de la aplicación

  La ventana de la aplicación primeramente tiene un panel "Título" que contiene la etiqueta con el título del programa -centrada respecto al ancho de la ventana-, que para cada programa debe variar según el nombre del framework utilizado, Ejemplo, "Cotizador De productos - customtkinter", "Cotizador De productos - Flet", etcétera. Este panel está anclado al borde superior de la ventana, y tiene la capacidad de achicar su alto cuando el usuario vaya desplazándose hacia abajo en el formulario, manteniéndose en una capa flotante superior respecto al formulario.

  El cuerpo de formulario se desplaza debajo de los paneles superior e inferior, mostrando una barra de desplazamiento en el lado derecho, que muestra al usuario la posición de este.
  El formulario contiene los paneles "Datos cliente", otro panel "Detalle productos", y un panel "Previsualización" escondido por defecto. El panel de "Detalle productos" contiene una tabla "Productos Cotizados".

  Finalmente, existe un panel "Botones" que está anclado al borde inferior de la ventana, manteniéndose también en una capa flotante superior respecto al formulario.

  > ```asciiart
  > ┌──────────────────────────────────────────────────────────────────┐
  > │┌────────────────────────────────────────────────────────────────┐│
  > ││         {Cotizador de Productos - <Nombre framework>}          ││
  > │└────────────────────────────────────────────────────────────────┘│
  > │┌─Datos─Cliente─────────────────────────────────────────────────┐▲│
  > ││        ┌────────────────────────────────────────────────────┐ │││
  > ││{Nombre}│ <Cliente>                                          │ │││
  > ││        └────────────────────────────────────────────────────┘ │││
  > │└───────────────────────────────────────────────────────────────┘││
  > │┌─ ▼ Detalle─Productos──────────────────────────────────────────┐││
  > ││ {Productos Cotizados}                                         │││
  > ││ ┌───────────────────────────────────────────────────────────┐ │││
  > ││ │  Item|Producto  | Cantidad |  Precio Unitario|       Total│ │││
  > ││ │-----:|:---------|:--------:|----------------:|-----------:│ │││
  > ││ │      |          |          |                 |            │ │││
  > ││ │      |          |          |                 |            │ │││
  > ││ └───────────────────────────────────────────────────────────┘ │││
  > ││ ┌─────────────────┐                          ┌──────────────┐ │││
  > ││ │  Limpiar Datos  │           {Total general}│  <Suma Total>│ │││
  > ││ └─────────────────┘                          └──────────────┘ │││
  > │└───────────────────────────────────────────────────────────────┘││
  > │┌─ ▶ Visualizar─Cotización──────────────────────────────────────┐││
  > │└───────────────────────────────────────────────────────────────┘▼│
  > │┌────────────────────────────────────────────────────────────────┐│
  > ││        ┌───────────────────┐      ┌───────────────────┐        ││
  > ││        │ Grabar Cotización │      │      Cerrar       │        ││
  > ││        └───────────────────┘      └───────────────────┘        ││
  > │└────────────────────────────────────────────────────────────────┘│
  > └──────────────────────────────────────────────────────────────────┘
  > ```

- Formulario con panel Previsualización visible

  El panel "Previsualización" debe aparecer completo entre los paneles de detalle de productos y el panel inferior con los botones. Este diagrama muestra parte de la ventana y como se representa el formulario con este panel desplegado.

  > ```asciiart
  > ┌─ ▼ Detalle─Productos──────────────────────────────────────────┐│
  > │ {Productos Cotizados}                                         ││
  > │ ┌───────────────────────────────────────────────────────────┐ ││
  > │ │  Item|Producto  | Cantidad |  Precio Unitario|       Total│ ││
  > │ │-----:|:---------|:--------:|----------------:|-----------:│ ││
  > │ │      |          |          |                 |            │ ││
  > │ │      |          |          |                 |            │ ││
  > │ └───────────────────────────────────────────────────────────┘ ││
  > │ ┌─────────────────┐                          ┌──────────────┐ ││
  > │ │  Limpiar Datos  │           {Total general}│  <Suma Total>│ ││
  > │ └─────────────────┘                          └──────────────┘ ││
  > └───────────────────────────────────────────────────────────────┘│
  > ┌─ ▼ Visualizar─Cotización──────────────────────────────────────┐│
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > │                                                               ││
  > └───────────────────────────────────────────────────────────────┘▼
  > ┌────────────────────────────────────────────────────────────────┐
  > │        ┌───────────────────┐      ┌───────────────────┐        │
  > │        │ Grabar Cotización │      │      Cerrar       │        │
  > │        └───────────────────┘      └───────────────────┘        │
  > └────────────────────────────────────────────────────────────────┘
  > ```

TASK: Definir el contenido a mostrar en el panel "Previsualización".

- Formulario con panel de detalle de productos plegado

  Para el panel "Detalle productos" existen ciertos ciertos campos o etiquetas que se muestran de todas maneras al estar plegados.

  - Etiqueta "Total general" y campo "Total" se deben mostrar en ambos casos.
  - Etiqueta "Cantidad Items" debe ocultarse en la vista desplegada, pero al plegarse sí se debe mostrar.
  - Al plegarse se ocultan el botón "Limpiar datos" y la tabla "Productos Cotizados".

  > ```asciiart
  > ┌─ ▶ Detalle─Productos──────────────────────────────────────────┐
  > │                                              ┌──────────────┐ │
  > │ {Cantidad Items}              {Total general}│  <Suma Total>│ │
  > │                                              └──────────────┘ │
  > └───────────────────────────────────────────────────────────────┘
  > ```

## 4. Comportamiento responsivo esperado

Esta sección detalla el comportamiento responsivo de la interfaz, complementando las definiciones generales de "Características comunes", "Tablas", "Paneles" y "Especificaciones adicionales".

- El formulario debe mostrar scroll vertical si el contenido excede el alto visible (ver "Características comunes" y "Barra de desplazamiento").

- Todos los paneles principales deben estirarse horizontalmente según el ancho de la ventana (ver "Características comunes").

- El panel "Título" y el panel "Botones" deben permanecer fijos (flotantes) anclados al borde superior e inferior de la ventana, respectivamente (ver atributo de anclaje en "Características comunes").

- El panel "Título" puede reducir su altura y/o fuente si la ventana es muy pequeña, pero sólo hasta modificar el título hasta el tamaño de fuente del texto normal con negritas, manteniendo márgenes verticales mínimos de 5px.

- Las columnas de la tabla "Productos Cotizados" deben:
  - Mantener proporciones al modificar el ancho de la ventana (ver "Tablas").
  - Las columnas "Ítem", "Cantidad", "Precio Unitario" y "Total" pueden expandir su ancho proporcionalmente, pero solo reducirse hasta el ancho mínimo necesario para mostrar su contenido más largo.
  - La columna "Producto" puede expandirse solo hasta que las otras columnas alcancen su ancho mínimo, pero sus celdas pueden aumentar en altura usando texto multi-línea con ajuste de palabras (wordwrap).
  - Permitir redimensionamiento manual arrastrando los bordes entre columnas, respetando las limitaciones anteriores (ver "Tablas").
  - Activar scroll horizontal si no caben.

- Las filas de la tabla "Productos Cotizados" deben:
  - Activar scroll vertical si no caben (ver "Tablas").
  - No permitir redimensionamiento manual de altura por parte del usuario.

- Para el panel "Detalle productos":
  - Los elementos mantienen su distribución según los diagramas y "Especificaciones adicionales", respetando márgenes sin solaparse.
  - Estado desplegado: muestra tabla, etiqueta "Productos Cotizados", botón "Limpiar datos", etiqueta "Total general" y campo "Suma Total".
  - Estado plegado: sólo muestra etiquetas "Cantidad Ítems" y "Total general", más el campo "Suma Total".
  - La etiqueta "Cantidad Items" se ajusta automáticamente a su contenido sin truncarse.
  - El campo "Suma total" mantiene como ancho, el máximo entre el ancho requerido para representar de manera completa su texto, y el de la columna "Total" de la tabla. Si este último no se puede obtener, por ejemplo si está oculta la tabla, asignarle valor cero dentro del cálculo.
  - Activar scroll horizontal si los elementos no caben en el ancho disponible.

- Para panel "Previsualización":
  - Si el panel está plegado, el indicador de plegado debe habilitarse solo si la validación 'Items Válidos en Detalle Productos' es verdadera.
  - Si el panel está desplegado, el contenido debe estar visible pero en estado deshabilitado.
  - Al estar desplegado puede modificarse su alto arrastrando el borde inferior, aunque tiene un alto mínimo determinado.

- Panel "Botones" tiene altura fija.

---

## 5. Especificaciones adicionales

### Detalles adicionales de campos

Para especificar detalles que no pueden ser descritos en los diagramas, la tabla siguiente contiene detalles adicionales de campos:

TODO: Convertir esta tabla en un listado estructurado

|Campo    | Tipo objeto gráfico, Tipo de datos | Detalles                         |
|---------|:----------------------------------:|----------------------------------|
|Cliente  | Campo de texto, Texto | Nombre del cliente, ingresado por el usuario con "*Parse* de Texto", debe usar "Validación Nombre Cliente". |
|Item     | Celda de tabla, Número entero | Generado automáticamente por el sistema (comienza en 1 numerando consecutivamente cada fila de la tabla), usa formato de cantidad sin decimales. |
|Producto | Celda de tabla, Texto | Texto ingresado por el usuario con "*Parse* de Texto", debe usar "Validación Nombre Producto". |
|Cantidad | Celda de tabla, Número Entero | Ingresado por el usuario con "*Parse* de Cantidad", usa "Validación de Cantidad con valor positivo", para mostrarse con formato de cantidad sin decimales. |
|Precio Unitario | Celda de tabla, Cantidad monetaria | Ingresado por el usuario con "*Parse* de Formato Monetario" (si se ingresa con decimales se acepta redondeo de hasta dos dígitos), usa "Validación de moneda con monto positivo", para mostrarse con Formato Monetario hasta dos decimales. |
|Total    | Celda de tabla, Cantidad monetaria | Calculado por el sistema cuando se ingresan producto, cantidad y precio unitario en la misma fila, es decir el resultado de `Cantidad * Precio Unitario` redondeado a cero decimales. Para mostrarse usa Formato Monetario sin decimales. |
|Suma total | Campo de texto solo lectura, cantidad monetaria | Calculado por el sistema luego de ingresado o modificado algún registro de la tabla, para mostrarse con Formato Monetario sin decimales. |
|Cantidad Items | Etiqueta, Texto | Calculado por el sistema luego de ingresar, modificar o eliminar algún registro de la tabla, para mostrarse usa formato de cantidad sin decimales. Solo considera celdas con datos. |

### Reglas de cálculo automático

| Campo calculado  | Fórmula o lógica                             | Evento que lo activa                 |
|------------------|----------------------------------------------|--------------------------------------|
| Total (por fila) | `Cantidad * Precio Unitario`                 | Cuando se modifica cantidad o precio |
| Suma Total       | Suma de todos los campos "Total" de la tabla | Cuando se modifica una fila          |
| Cantidad Ítems   | Si tabla está vacía, mostrar "Sin ítems", habiendo 1 fila mostrar "1 ítem" y para el resto mostrar "X ítems" con X la cantidad. La cantidad es obtenida desde la "Validación Items Válidos en Detalle productos"  | Al agregar o quitar una fila válida, o acción del botón "Limpiar Datos" |

### Jerarquía de navegación con el teclado

- La navegación directa entre elementos gráficos se da al usar la tecla `Tab`.
- La navegación inversa se realiza al utilizar `Shift+Tab`,
- El primer elemento corresponde al valor por defecto cuando cuando se abre la aplicación.
- Al recorrer la lista utilizando el teclado, cuando se llega a cualquiera de los dos extremos no se puede avanzar o retroceder más allá de éste.
- También se puede navegar al comienzo o al final de la lista con las teclas `Home` y `End`, respectivamente.

- Orden de navegación entre elementos gráficos:
  - Panel "Datos cliente", campo "Cliente".
  - Panel "Detalle productos", Indicador de plegado.
  - Panel "Detalle productos", Tabla "Productos Cotizados".
  - Panel "Detalle productos", Botón "Limpiar Datos".
  - Panel "Detalle productos", Campo "Suma total".
  - Panel "Previsualización", Indicador de plegado.
  - Panel "Botones", Botón "Grabar cotización".
  - Panel "Botones", Botón "Cerrar".

## 6. Notas de implementación

### Construcción de controles personalizados

- Se debe construir un control personalizado desde cero solo en el caso de que un control estándar no exista en el framework utilizado.
- Sin embargo, se debe evitar la duplicación de esfuerzos y reutilizar componentes existentes siempre que sea posible. Por ejemplo, si el control de texto ya existe, pero le falta la funcionalidad de mostrar que tiene el foco, se debe extender ese control en lugar de crear uno nuevo.
- Además, se debe documentar adecuadamente el control personalizado para facilitar su mantenimiento y posible reutilización en el futuro.

### Propiedades de interés para Control emergente para mensajes

- Control vinculado: Vinculo al control desde donde se muestra el mensaje emergente.
- Texto de categoría de mensaje: Valores válidos "error", "advertencia", "información". Si el framework contiene constante para estas categorías, utilizarlas para la implementación.
- Mensaje: Texto a mostrar en la etiqueta Mensaje.
- Colores para borde del control: Etiquetas de color para estados normal y resaltado. Utilizar sistemas de color y tipos de datos que utilice el framework.
- Colores para categoría de mensaje: Etiquetas de color según cada categoría, para mostrar como color de fondo del control. Utilizar sistemas de color y tipos de datos que utilice el framework.
- Estilo de texto del mensaje: Color, familia de fuente, tamaño de fuente, estilo (normal, negrita, cursiva).
- Alto y ancho mínimos del control: Valores de solo lectura en píxeles.
- Los demás atributos específicos que requiera o hereda por ser elemento gráfico en cada framework.

### Implementación de formatos

Para la representación en string de los formatos, tanto del de Cantidad, como del Monetario, se debe utilizar las funcionalidades de la librería `locale`, estableciéndose la utilización de esos formatos como constantes en todo el programa.
Como se muestra en el siguiente ejemplo de código, se debe utilizar la constante `FORMATO_CANTIDAD` en todo el programa:

```python
  import locale
  locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')  # Configuración para chile
  numero = 1234567
  FORMATO_CANTIDAD: str = ":n"

  formatted = f"{numero{FORMATO_CANTIDAD}}"  # "1.234.567"
```

### Detalle de Validaciones y Funciones de *Parse*

- **Validación Nombre Cliente**
  Esta validación implica que un texto debe ser al menos 3 caracteres partiendo por una letra (no importando si es mayúscula, minúscula o con acento), permitiendo solo espacios ' ' simples.
  Ejemplo de valores válidos: "Juan Pérez", "ABC", "Sociedad comercial S.A.". Ejemplos no válidos: "123", "A", "#ana".

- **Validación Nombre Producto**
  Un texto debe tener al menos 3 caracteres partiendo por una letra (no importando si es mayúscula, minúscula o con acento), permitiendo solo espacios ' ' simples.
  Ejemplo de valores válidos: "Jabón pollito", "BIC", "Lápiz #3". Ejemplos no válidos: "321", "Z", "?AB".

- **Validación de Cantidad con valor positivo**
  Consiste en validar que es un número entero o de puntos flotante pero con valores mayores a cero.
  *Nota de implementación:* Considerar que parámetro de entrada es de tipo int o float.
  Ejemplo de valores válidos: `10000`, `123.00`. Ejemplos no válidos: `0`, `-123`, `math.inf`, `math.nan`.

- **Validación de Moneda con monto positivo**
  Consiste en validar que el monto de un valor monetario es un número entero o de punto flotante pero con valor mayor a cero.
  *Nota de implementación:* Considerar que parámetro de entrada es de tipo int o float.
  Ejemplo de valores válidos: `10000`, `123.00`. Ejemplos no válidos: `0`, `-123`, `math.inf`, `math.nan`.

- **Validación Items Válidos en Detalle productos**
  Se debe validar que la tabla de "Detalle productos" tenga registros válidos, es decir que existan filas tanto con producto válido como con totales calculados, ignorando filas vacías que se muestren en pantalla o registros incompletos que no permitan calcular aún el total de la fila. La validación deben resultar falsa si la cantidad de registros validos es cero, verdadera si hay al menos uno.  También debe entregarse la cantidad de registros válidos.

- ***Parse* de Texto**
- Al recibirse el texto, lo primero es recortar todos los caracteres de espacio al principio y al final. Luego, debe reemplazar todos los caracteres de la clase espacio por el carácter de espacio simple ' ', y eliminar espacios múltiples entre palabras para dejar sólo uno.

- ***Parse* de Cantidad**
  Al recibirse el texto, lo primero es recortar todos los caracteres de espacio al principio y al final. Luego, tratar de convertir al número entero o de punto flotante, pero respetando las convenciones de caracteres de punto decimal y de separador de miles que se use en este computador corriendo Windows. Si el texto entregado se puede transformar a un número en punto flotante, se debe usar la función de truncar con cero decimales. Si no se puede convertir a número, entregar error de valor.
  *Nota de implementación:* Se deben utilizar las funcionalidades de la librería `locale` como se describió antes en la sección [Implementación de formatos](#implementación-de-formatos).

- ***Parse* de Formato Monetario**
  Al recibirse el texto, lo primero es recortar todos los caracteres de espacio al principio y al final. Luego, tratar de convertir al número entero o de punto flotante, pero respetando las convenciones de caracteres de moneda, punto decimal y de separador de miles que se use en este computador corriendo Windows. Luego considerando la cantidad de decimales especificada como parámetro opcional (valor por defecto cero, rechazando valores negativos como error de valor), se debe redondear el valor con esa especificación de decimales. Si no se puede convertir a número, entregar error de valor.
*Nota de implementación:* Se deben utilizar las funcionalidades de la librería `locale` como se describió antes en la sección [Implementación de formatos](#implementación-de-formatos).

### Acciones del usuario

| Botón / Acción                | Comportamiento esperado                                                                     |
|-------------------------------|---------------------------------------------------------------------------------------------|
| Clic Botón de cierre en control emergente para mensajes | Cierra el control emergente, sin actualizar el estado del control vinculado. |
| Clic Botón Grabar Cotización  | Validar todos los campos visibles. Si son válidos, generar archivo PDF.                     |
| Clic Botón Cerrar             | Cierra la aplicación. Si hay cambios no guardados debe mostrar un diálogo de confirmación.  |
| Clic Botón Limpiar Datos      | Elimina todas las filas de la tabla y reinicia el campo “Suma Total” a cero.                |
| Clic `▶ / ▼` "Productos Cotizados"  | Alterna la visibilidad del panel de tabla de productos.                                |
| Clic `▶ / ▼` Previsualización | Muestra/oculta el panel "Previsualización", pero solo si ya hay datos disponibles.    |
| Edición de celda de tabla     | Al modificar celda de cantidad o precio, recalcular celda “Total” de la fila, actualizar “Suma Total” y  “Cantidad Items”. Si se modifica celda producto, validar nombre. Si se actualiza “Cantidad Items”, se debe validar estado activación de indicador de plegado de panel "Previsualización". |
| Clic en fila de tabla         | Selecciona la fila, permitiendo eliminarla con el botón de eliminación.                     |
| Clic en ícono inserción tabla | Inserta una nueva fila vacía debajo de la fila actual. Posiciona el cursor en la primera celda editable. |
| Clic en ícono eliminación tabla | Elimina la fila seleccionada, mostrando confirmación si la fila contiene datos.           |

## 7. Referencias

- Herramienta web para crear bosquejos: <https://asciiflow.com/>
