# Planificación de tareas para el informe de commits (mes completo)

**Objetivo:** Generar un informe detallado de los commits realizados en el repositorio de GitHub durante un mes completo, incluyendo un análisis técnico de los cambios realizados y un resumen de los mismos.

## Herramientas necesarias

- Capacidad para ejecutar comandos de Git en la línea de comandos.
- Capacidad para crear y editar archivos markdown.
- Herramienta de linting para markdown, invocándola con el siguiente comando usando el archivo de configuración específico:

  ```powershell
  markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/commits_{mes}_{año}.md"
  ```

## Etapas del proceso

### 0. Preparación inicial

Realizar las siguientes acciones, informando al usuario solo en caso de error si alguna de estas acciones no se puede completar:

- Recordar que el nombre del repositorio es `Especificaciones-UI`.
- Asegurarse que tienes acceso al repositorio en GitHub y que puedes clonarlo localmente si es necesario.
- Asegurarse que tienes permisos para leer los commits y detalles del repositorio.
- Asegurarse que están instaladas las [herramientas listadas en la sección](#herramientas-necesarias) y que funcionan correctamente.

### 1. Preguntar por mes a generar

- Preguntar al usuario qué mes desea generar el informe de commits.
- Asegurarse que el mes es válido y según eso calcular el rango de fechas a considerar. Por ejemplo, si lo solicitado es julio de 2025, el rango de fechas a considerar es del 1 al 31 de julio de 2025.
- Recordar el mes y año seleccionado para su uso posterior en el informe, el que se referenciará como `{mes}` y `{año}` en el resto del informe.

### 2. Generar archivo de commits

#### 2.1 Obtener la lista de commits

- Consultar el repositorio en GitHub para obtener todos los commits realizados en el rango de fechas para el informe. Usar comandos como:

  ```powershell
  git log --since="YYYY-MM-01" --until="YYYY-MM-31" --pretty=format:"%H|%an|%ad|%s" --date=iso
  ```

- Utilizar herramienta: Obtener la lista completa de commits del rango de fechas a informar, teniendo en consideración que la información puede llegar en lotes y no completa de una sola vez. Usar paginación si es necesario.
- Asegurarse que se obtienen todos los commits, sin omitir ninguno. Si no hay commits en el rango de fechas, informar al usuario y finalizar el proceso.
- Guardar la lista de commits en una estructura de datos adecuada para su posterior procesamiento.
- Cada commit debe incluir:
  - Identificador único (SHA)
  - Autor
  - Fecha y hora
  - Mensaje de commit completo
  - Enlace al commit en GitHub, si es que se puede obtener. Si no se puede obtener, dejar este campo vacío, pues se completará después.

#### 2.2 Escribir filas de commits

- Revisar si existe directorio para el informe del mes y año seleccionado, si no existe crearlo. El directorio debe ser `informes/{año}-{mes como número}`.
- Crear un archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md` que contenga una tabla con el siguiente formato:

  > ```markdown
  > # Lista detallada de commits - {mes} {año}
  >
  > ## Lista de commits
  > | Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         | Archivo Afectado | Líneas +  | Líneas -   |
  > |---------------------|---------------|-------------------|----------------|------------------|------------------|----------:|-----------:|
  > | YYYY-MM-DD HH:MM:SS | SHA corto     | [Ver commit](URL) | Título Mensaje | Detalles Mensaje |`Archivo1`<br>`Archivo2`<br>`Archivo3` |num_agregadas1<br>num_agregadas2<br>num_agregadas3|num_eliminadas1<br>num_eliminadas2<br>num_eliminadas3|
  > ```

  Nota: los campos `archivo`, `num_agregadas` y `num_eliminadas` se completarán en la siguiente etapa.

- Para cada commit obtener los detalles:
  - Identificador único (SHA)
  - Fecha y hora
  - Enlace al commit
  - Separar título y detalles del mensaje de commit: El título es la primera línea antes de un salto de línea, y los detalles son el resto del mensaje. Esto último puede resultar vacío si el mensaje de commit es solo una línea.

- Escribir la información al archivo, donde cada fila de la tabla debe corresponder a un commit.
  - Debes asegurarte que los commits se listen ordenados por fecha y hora de forma ascendente (del más antiguo al más reciente).
  - No resumir ni acortar los mensajes de commit, pues deben reflejar con precisión los cambios declarados.

#### 2.3 Correcciones de formato

- Debes revisar los detalles del mensaje de cada commit para asegurarte que se reemplacen caracteres especiales `*` por `+` para que no rompan el formato markdown de la tabla, pues los utilizo en los mensajes del commit como viñetas de lista.
- Revisar el archivo generado con linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
  - Asegurarse de que todos los enlaces a commits de GitHub estén correctamente formateados y sean accesibles.

### 3. Determinar lineas cambiadas por commit

Para cada commit, listar los archivos modificados y obtener el número de líneas agregadas y eliminadas por archivo.

- Para cada commit en el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md`, obtener la lista de archivos modificados y el número de líneas agregadas y eliminadas por archivo.
- Para obtener esta información utilizar herramienta de línea de comandos como `git show --stat {SHA}`.
- Para cada archivo modificado en el commit, obtener:
  - Nombre del archivo modificado.
  - Número de líneas agregadas.
  - Número de líneas eliminadas.
- Actualizar el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md` para incluir esta información en las columnas correspondientes.
  - Cada archivo modificado debe estar listado dentro de la celda correspondiente, separando los nombres de los archivos con saltos de línea (`<br>`).
  - Cada nombre de archivo debe estar rodeado con caracteres '`' para formato de código.
  - Hacer lo mismo para las columnas de líneas agregadas y eliminadas, asegurándose que cada número corresponda al archivo en la misma posición.

### 4. Generar resumen de cambios por commit

#### 4.1 Analizar cada commit

Esta etapa es la más importante y crítica del proceso, ya que implica entender los cambios realizados en cada commit y generar un resumen técnico y claro de los mismos.
El objetivo es describir los cambios de una manera técnica y detallada, explicando que cambió.

Para cada commit, realizar las siguientes tareas:

- Se debe procesar y analizar uno por uno los commits, para asegurar que se comprende cada cambio realizado.
  - Utiliza la información obtenida en el paso 3 y 4 para tener un contexto completo de cada commit.
- Obtener el diff del commit, que muestre los cambios realizados en el código. Para esto, usar herramienta de línea de comandos como `git diff`.
  - Leer el diff de cada commit para entender los cambios realizados, tanto a nivel de variables, como de lógica y documentación, relacionando estos cambios con el mensaje del commit.
- Generar un resumen detallado de cada commit, que sintetice los cambios realizados en cada uno:
  - Cambios realizados en el código.
  - Impacto de los cambios.
  - Cualquier consideración especial o contexto relevante.
  - Este resumen debe ser técnico y claro, explicando qué cambió y por qué.
  - Usa un tono objetivo, evita juicios de valor y el uso de adjetivos rimbombantes.

- **Importante:** Si tienes la capacidad de crear subagentes, utilízalos y delega esta tarea a un subagente especializado en análisis de código y generación de resúmenes técnicos. Si no tienes la capacidad de crear subagentes, realiza esta tarea tú mismo.
  - El subagente puedes llamarlo "Agente Analista de Commits".
  - Este subagente debe tener la capacidad de leer y analizar diffs de código, entender cambios en variables, lógica y documentación, y generar resúmenes técnicos claros.
  - Comunica al subagente los detalles ya disponibles del commit, y solicita el análisis técnico y el resumen de cambios.
  - Genera un prompt claro y detallado para el subagente, asegurándote de incluir:
    - El contexto del proyecto.
    - El objetivo del análisis.
    - El formato esperado para la respuesta.
    - Cualquier restricción o detalle específico que deba considerar.
  - Genera varios subagentes si es necesario para dividir la carga de trabajo.
  - Supervisa el progreso del subagente y asegúrate de que cumple con los requisitos.
  - Revisa y valida la información proporcionada por el subagente antes de integrarla en el informe final.

#### 4.2 Escribir detalles de commits

- **Importante:** Si tienes la capacidad de crear subagentes, utilízalos y delega esta tarea a un subagente especializado en redacción técnica. Si no tienes la capacidad de crear subagentes, realiza esta tarea tú mismo.
  - El subagente puedes llamarlo "Agente Redactor Técnico".
  - Este subagente debe tener la capacidad de redactar resúmenes técnicos claros y concisos, adaptados a una audiencia técnica y no técnica.
  - Comunica al subagente los detalles del commit y solicita el resumen de cambios.
  - Genera un prompt claro y detallado para el subagente, asegurándote de incluir:
    - El contexto del proyecto.
    - El objetivo del resumen.
    - El formato esperado para la respuesta.
    - Cualquier restricción o detalle específico que deba considerar.
  - Genera varios subagentes si es necesario para dividir la carga de trabajo.
  - Supervisa el progreso del subagente y asegúrate de que cumple con los requisitos.
  - Revisa y valida la información proporcionada por el subagente antes de integrarla en el informe final.

- Guardar este resumen en el archivo `informes/{año}-{mes como número}/commits_detallados_{mes}_{año}.md`, en la sección correspondiente a cada commit.
  - Asegurarse que cada commit tiene un número correlativo único y que están ordenados por fecha y hora de forma ascendente (del más antiguo al más reciente).
  - Asegurarse que La cantidad de commits sea la misma que la cantidad de líneas en la tabla de commits.
  - **Importante:** Abstente de agregar otras secciones o detalles que no sean estrictamente necesarios para el informe de commits.
  - Utilizar el formato siguiente para cada commit:

  ```markdown
  ### {numero correlativo}. Título del Commit - {SHA resumido a 7 caracteres}
  - **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
  - **Enlace al Commit:** [Commit {SHA resumido a 7 caracteres}]({URL})
  - **Título:** {Título Mensaje}
  - **Detalles:** {Detalles Mensaje}
  - **Archivos Modificados:**
    - `{Archivo Modificado}`: {Líneas Agregadas} líneas agregadas | {Líneas Eliminadas} líneas eliminadas.
  - **Cambios realizados:**
     - {Lista detallada de cambios}
  - **Resumen de cambios:**
    {Explicación técnica de qué cambió}

  ---

  ```

#### 4.3 Validar el documento

- Revisar el archivo generado con linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
  - Asegurarse de que todos los enlaces a commits de GitHub estén correctamente formateados y sean accesibles.

### 5. Resumen de cambios por temas y generación del informe final

Generar un resumen de cambios agrupados por temas, basado en el análisis realizado en la etapa anterior.

#### 5.1. Clasificar los cambios por temática

- Categorías estándar para este repositorio:
  - Mejoras en las funcionalidades
  - Corrección de errores (bugfixes)
  - Mejoras de rendimiento
  - Refactorización de código
  - Limpieza de código y comentarios
  - Mejoras en la documentación
  - Mejoras en pruebas (testing)
  - Mejoras en empaquetado y despliegue
  - Actualizaciones de dependencias
  - Otros cambios relevantes

- Proceso de clasificación:
  - Análisis de mensajes de commit
  - Correlación con cambios técnicos identificados
  - Identificación de temas relevantes
  - Agrupación automática por categoría y temática dentro de cada categoría
  - Priorización dentro de cada categoría por impacto, relevancia y volumen

- Requisitos para el resumen de cambios:
  - Asegurarse que cada tema tiene una descripción clara y concisa de los cambios realizados.
  - El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes. Usar un tono profesional y objetivo.
  - Guardar este resumen en el archivo `informes/{año}-{mes como número}/resumen_cambios_{mes}_{año}.md`.
  - El formato de los temas del resumen de cambios es:

  ```markdown
  # Resumen de cambios por temas

  ## `{Categoría de Cambios}`

  ### `{Tema}`
  - **Commits:** `{número de commits}` commits de `{detalle tema}`.
  - **Impacto técnico:** `{Descripción del impacto técnico de los cambios}`.
  - **Cambios principales:**
    - `{Detalle de los cambios ordenado por prioridad}`

   ```

- Revisar el archivo generado con linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.

#### 5.2. Generar el documento del informe final

- Estructurar el informe Utilizando el template `informes/Instrucciones/Template_Informe_{repositorio}.md`, completando los campos necesarios:
  - `{repositorio}`: Nombre del repositorio.
  - `{mes}`: Mes seleccionado.
  - `{año}`: Año seleccionado.
  - `{mes y año solicitado}`: Mes y año en formato "Mes Año" (por ejemplo, "Julio 2025").
  - `{Resumen de los cambios realizados en el repositorio, indicando la cantidad de commits y principales áreas de mejora o nuevas funcionalidades.}`: Resumen que incluya la cantidad total de commits.
    - Este resumen debe listar resumidamente, en no más de cuatro párrafos, los principales cambios y ajustes realizados en las dos primeras categorías mencionadas.
    - Este resumen debe ser técnico y claro, explicando qué cambió y por qué.
    - El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes.
    - Usar un tono profesional y objetivo.
  - `{Resumen de los cambios agrupados por temas, indicando la cantidad de commits}`: Resumen generado en la etapa anterior.

- Guardar el informe como `informes/{año}-{mes como número}/Informe_Desarrollo_{repositorio}_{mes}_{año}.md`.

#### 5.3. Revisión final

- Validar que el documento cumple con los requisitos y está listo para ser entregado, incluyendo:
  - Verificar que todos los commits están listados y detallados correctamente.
  - Asegurarse que el resumen de cambios por temas es claro y conciso.
  - Confirmar que el formato del documento es consistente y profesional.
  - Asegurarse que no haya secciones o detalles no solicitados en el informe: el informe debe centrarse exclusivamente en los commits y los cambios realizados.
- Revisar el archivo generado con linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
