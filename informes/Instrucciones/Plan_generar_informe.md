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
  > ## Tabla de commits
  > | Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         | Archivo Afectado | Líneas +  | Líneas -   |
  > |---------------------|---------------|-------------------|----------------|------------------|------------------|----------:|-----------:|
  > | YYYY-MM-DD HH:MM:SS | SHA corto     | [Ver commit](URL) | Título Mensaje | Detalles Mensaje |`Archivo1`<br>`Archivo2`<br>`Archivo3` |num_agregadas1<br>num_agregadas2<br>num_agregadas3|num_eliminadas1<br>num_eliminadas2<br>num_eliminadas3|
  > ```

  **Nota:** los campos `archivo`, `num_agregadas` y `num_eliminadas` se completarán en la siguiente etapa.

- Para cada commit obtener los detalles:
  - Identificador único (SHA)
  - Fecha y hora
  - Enlace al commit
  - Separar título y detalles del mensaje de commit, sin resumir ni acortarlos adicionalmente:
    - El título es la primera línea antes de un salto de línea.
    - Detalles son el resto del mensaje, y puede resultar vacío si el mensaje de commit es solo una línea.

- Escribir la información al archivo, donde cada fila de la tabla debe corresponder a un commit.
  - Debes asegurarte que los commits se listen ordenados por fecha y hora de forma ascendente (del más antiguo al más reciente).
  - Asegurarte que la cantidad de commits sea la misma que la cantidad de líneas en la tabla de commits.
  - Abstenerse de agregar otras secciones o detalles.

#### 2.3 Determinar lineas cambiadas por commit

En esta etapa se procesará cada commit, obteniendo una lista de todos los archivos modificados, y el número de líneas agregadas y eliminadas por cada uno.

**Tareas a realizar:**

- Para cada commit en el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md`, obtener la lista de archivos modificados y el número de líneas agregadas y eliminadas por archivo.
  - Utilizar herramienta de línea de comandos como `git show --stat {SHA}`.
  - Para cada archivo modificado en el commit, obtener:
    - Nombre del archivo.
    - Número de líneas agregadas.
    - Número de líneas eliminadas.

- Actualizar el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md` para incluir esta información en las columnas correspondientes.
  - Si un commit no tiene archivos modificados, escribir "Sin cambios", "0" y "0" en las columnas de archivos afectados, líneas agregadas y líneas eliminadas, respectivamente.
  - En cambio, si el commit tiene al menos un archivo modificado, listar todos los archivos y sus respectivas líneas agregadas y eliminadas, separando los nombres de los archivos con saltos de línea (`<br>`).
    - Cada nombre de archivo debe estar rodeado con caracteres '`' para formato de código.
  - Hacer lo mismo para las columnas de líneas agregadas y eliminadas, asegurándose que cada número corresponda al archivo en la misma posición.
  - No omitir ningún archivo, incluso si son muchos.

- Validar que la cantidad total de registros procesados coincida con la cantidad informada por la API.

#### 2.4 Correcciones de formato

- Reemplazar caracteres `*` por `+` en mensajes para evitar conflictos markdown:
  - Si hay múltiples reemplazos en el mismo mensaje, separarlos con `<br>`
- Revisar el archivo generado con linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
- Asegurarse de que todos los enlaces a commits de GitHub estén correctamente formateados y sean accesibles.

### 3. Generar resumen de cambios por commit

#### 3.1 Escribir detalles de commits

**Tareas a realizar:**

- Crear un archivo `informes/{año}-{mes como número}/commits_detallados_{mes}_{año}.md` que contendrá el análisis detallado de cada commit. El formato del comienzo del archivo es:

  ```markdown
  # Análisis detallado de commits - {mes} {año}

  ---

  ```

- Desde el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md`, leer cada fila de la Tabla de commits para obtener los detalles de cada uno, agregando un nuevo registro al final del archivo de commits detallados, con el siguiente formato:

  ```markdown
  ## {numero correlativo}. {Título del Commit} - {SHA corto}
  - **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
  - **Enlace al Commit:** [Commit {SHA corto}]({URL})
  - **Título:** {Título Mensaje}
  - **Detalles:** {Detalles Mensaje}
  - **Archivos Modificados:**
    - `{Archivo}`: {Cant. Agregadas} líneas agregadas | {Cant. Eliminadas} líneas eliminadas.
  - **Cambios realizados:**
     - {Lista detallada de cambios técnicos}
  - **Resumen de cambios:**
    {Resumen del commit}

  ---

  ```

**Nota:** Los campos `{Lista detallada de cambios técnicos}` y `{Resumen del commit}` se completarán en la etapa siguiente, por lo que en esta etapa deben dejarse como un marcador de posición.

**Requisitos:**

- Ordenar commits por fecha y hora de forma ascendente (del más antiguo al más reciente).
- Asegurarse que cada commit tiene un número correlativo único, comenzando en 1.
- Asegurarse que la cantidad de commits sea la misma que la cantidad de líneas en la tabla de commits en `commits_{mes}_{año}.md`.
- Reutilizar exactamente Título y Detalles saneados de la tabla, sin modificar.
- **Importante:** Abstente de agregar otras secciones o detalles que no sean estrictamente necesarios.

#### 3.2 Analizar cada commit

Esta etapa es la más importante y crítica del proceso, ya que implica entender los cambios realizados en cada commit y generar un resumen técnico y claro de los mismos.

**Tareas a realizar:**

- Procesar y analizar cada commit, para asegurar que se comprende cada cambio realizado.
  - Desde el archivo `commits_detallados_{mes}_{año}.md` generado en el paso anterior, leer cada registro de commit para obtener los detalles de cada uno.

- Se debe detectar si un commit está vacío (sin cambios en archivos): en ese caso, el resumen debe indicar "Commit sin cambios en archivos", terminando el procesamiento de de ese commit. Si no está vacío, continuar con el análisis.

- Obtener el diff del commit, que muestre los cambios realizados en el código. Para esto, usar herramienta de línea de comandos como `git diff`.
  - Leer el diff de cada commit para entender los cambios realizados, tanto a nivel de variables, como de lógica y documentación, relacionando estos cambios con el mensaje del commit.

- Generar una lista detallada de los cambios realizados en el commit. Esta lista debe incluir:
  - Cambios en variables (nuevas, eliminadas, renombradas, modificadas).
  - Cambios en la lógica del código (nuevas funciones, modificaciones en funciones existentes, cambios en estructuras de control).
  - Cambios en la documentación (nuevos comentarios, modificaciones en comentarios existentes).
  - Cambios en archivos de configuración o scripts.
  - **Requisitos de la lista detallada:**
    - Esta lista debe ser técnica y clara, explicando qué cambió y por qué.
    - Evitar redundancias y explicaciones innecesarias.
    - Usar un tono objetivo, evitando juicios de valor y el uso de adjetivos rimbombantes.

- Generar un resumen de cada commit, que sintetice los cambios realizados en cada uno:
  - Cambios realizados en el código.
  - Impacto de los cambios.
  - Motivo de los cambios, si es que se puede inferir del ¿Hay algo que guardar? mensaje del commit o del análisis del diff.
  - **Requisitos del resumen:**
    - Este resumen debe ser técnico, directo y claro, explicando qué cambió y por qué.
      - Evitar redundancias y explicaciones innecesarias.
      - Usa un tono objetivo, evita juicios de valor y el uso de adjetivos rimbombantes.
    - La extensión del resumen debe ser proporcional a la complejidad o cantidad de cambios del commit, pero no debe ser excesivamente largo. En general, un párrafo de 2 a 8 líneas es adecuado.

**Uso De agentes:**
Si tienes la capacidad de crear subagentes, utilízalos y delega estas tareas a un subagente especializado en análisis de código y generación de resúmenes técnicos. Si no tienes la capacidad de crear subagentes, realiza esta tarea tú mismo.

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

#### 3.3 Validar el documento

- Revisar el archivo generado con herramienta de linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
- Asegurarse de que todos los enlaces a commits de GitHub estén correctamente formateados y sean accesibles.

### 4. Resumen de cambios por temas y generación del informe final

Generar un resumen de cambios agrupados por temas, basado en el análisis realizado en la etapa anterior.

#### 4.1. Clasificar los cambios por temática

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
  - Priorización dentro de cada categoría por:
    - Impacto (afecta funcionalidad central / superficie de usuarios)
    - Complejidad (cambios simples versus complejos)
    - Alcance (número de archivos o módulos)
    - Frecuencia (cantidad de commits similares)
    - Tamaño relativo (líneas modificadas netas)
  - Se debe describir brevemente la prioridad asignada a cada tema, registrando el motivo, para completar el campo `{Explicación Prioridad}` en la tabla del resumen de cambios.
  - Asignación de un tema a cada commit, asegurando que cada tema tenga una descripción clara y concisa de los cambios realizados.

#### 4.2 Generar resumen por temas

- Guardar resumen de cambios en el archivo `informes/{año}-{mes como número}/resumen_cambios_{mes}_{año}.md`, con el siguiente formato de encabezado:

  ```markdown
  # Resumen de cambios por temas

  ```

- Requisitos para el resumen de cambios:
  - Asegurarse que cada tema tiene una descripción clara y concisa de los cambios realizados.
    - Si una categoría no tiene temas, no debe incluirse en el resumen.
  - El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes. Usar un tono profesional y objetivo.

- El formato de los temas es:

  ```markdown
  ## {Categoría de Cambios} {número de commits en la categoría} commits.

  ### {Tema}
  - **Commits:** {número de commits} commits.
  - **Descripción:** {Descripción del tema}.
  - **Impacto técnico:** {Descripción del impacto técnico de los cambios}.
  - **Cambios principales:**
    - {Detalle de los cambios ordenado por prioridad}. Prioridad: {Explicación Prioridad}

   ```

- Revisar el archivo generado con herramienta de linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.

#### 4.3. Generar el documento del informe final

- Estructurar el informe utilizando el template `informes/Instrucciones/Template_Informe_{repositorio}.md`, completando los campos necesarios:
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

#### 4.4 Revisión final

- Validar que el documento cumple con los requisitos y está listo para ser entregado, incluyendo:
  - Verificar que todos los commits están listados y detallados correctamente.
  - Asegurarse que el resumen de cambios por temas es claro y conciso.
  - Confirmar que el formato del documento es consistente y profesional.
  - Asegurarse que no haya secciones o detalles no solicitados en el informe: el informe debe centrarse exclusivamente en los commits y los cambios realizados.
- Revisar el archivo generado con herramienta de linter para markdown y corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia.
