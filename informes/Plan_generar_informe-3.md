# Planificación de tareas para el informe de commits (mes completo)

1. Preguntar por mes a generar
   - Preguntar al usuario qué mes desea generar el informe de commits.
   - Asegurarse que el mes es válido y según eso calcular el rango de fechas a considerar.
   - Al usuario la lista de fechas a considerar, por ejemplo, si es julio de 2025, las fechas serían del 1 al 31 de julio de 2025.
   - Recordar el mes y año seleccionado para su uso posterior en el informe, el que se referenciará como `{mes}` y `{año}` en el resto del informe.

2. Obtener la lista de commits

   - Consultar el repositorio en GitHub para obtener todos los commits realizados en el rango de fechas para el informe.
     - Utilizar herramienta MCP: Obtener la lista completa de commits del rango de fechas a informar.

     - Para cada commit obtener los detalles:
       - Identificador único (SHA)
       - Fecha y hora
       - Enlace al commit
       - Título y detalles del mensaje de commit: El título es la primera línea antes de un salto de línea, y los detalles son el resto del mensaje.

     - Escribir el detalle de todos los commits al archivo `informes/commits_{mes}_{año}.md`, con el formato siguiente:
     - Revisar el archivo generado con `markdownlint-cli2` y corregir cualquier problema de formato detectado.

        > ```markdown
        > # Lista detallada de commits - {mes} {año}
        >
        > ## Lista de commits
        > | Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         |
        > |---------------------|---------------|-------------------|----------------|------------------|
        > | YYYY-MM-DD HH:MM:SS | SHA           | [Ver commit](URL) | Título Mensaje | Detalles Mensaje |
        > |                     |               |                   |                |                  |
        > ```

3. Analizar los archivos modificados por commit

   - Para cada commit, listar los archivos modificados y obtener el número de líneas agregadas y eliminadas por archivo.
     - Asegurarse que están ordenados por fecha y hora de forma ascendente (del más antiguo al más reciente).

   - Generar una lista de "Cambios técnicos realizados" en el commit.
     - **Importante:** Si tienes la capacidad de crear subagentes, utilízalos y delega esta tarea a un subagente especializado en análisis de código y generación de resúmenes técnicos.
       - El subagente puedes llamarlo "Agente Analista de Commits".
       - Este subagente debe tener la capacidad de leer y analizar diffs de código, entender cambios en variables, lógica y documentación, y generar resúmenes técnicos claros.
       - Comunica al subagente los detalles del commit y solicita el análisis técnico y el resumen de cambios.
       - Genera un prompt claro y detallado para el subagente, asegurándote de incluir:
         - El contexto del proyecto.
         - El objetivo del análisis.
         - El formato esperado para la respuesta.
         - Cualquier restricción o detalle específico que deba considerar.
       - Genera 2 o 3 subagentes si es necesario para dividir la carga de trabajo.
       - Supervisa el progreso del subagente y asegúrate de que cumple con los requisitos.
       - Revisa y valida la información proporcionada por el subagente antes de integrarla en el informe final.
       - Si no tienes la capacidad de crear subagentes, realiza esta tarea tú mismo.
     - Leer el diff de cada commit para entender los cambios realizados, tanto a nivel de variables, como de lógica y documentación.
     - El objetivo es describir los cambios de una manera técnica y detallada, explicando que cambió.
     - Se debe procesar y analizar uno por uno los commits, para asegurar que se comprende cada cambio realizado.
     - Esto se debe describir en el archivo como una lista con el detalle de los cambios técnicos realizados en el commit.

   - Generar un "Resumen de cambios de este commit".
     - Sintetizar los cambios de realizados desde un punto de vista global, de manera que cualquier persona pueda entender como estos cambios afectan al proyecto.
     - Esto se debe hacer analizando commit por commit, y entendiendo el impacto de cada cambio.

   - Guardar esta información en archivo `informes/commits_detallados_{mes}_{año}.md`,con un formato siguiente:
   - Revisar el archivo generado con `markdownlint-cli2` y corregir cualquier problema de formato detectado.

      ```markdown
      ### {numero correlativo}. Título del Commit - {SHA resumido a 7 caracteres}
      - **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
      - **Enlace al Commit:** [Commit {SHA resumido a 7 caracteres}]({URL})
      - **Título:** {Título Mensaje}
      - **Detalles:** {Detalles Mensaje}
      - **Archivos Modificados:**
        - {Archivo Modificado}: {Líneas Agregadas} líneas agregadas | {Líneas Eliminadas} líneas eliminadas.
      - **Cambios técnicos realizados:**
         - {Lista de Cambios técnicos realizados en el commit}
      - **Resumen de cambios:**
        {Resumen de cambios realizados en el commit}

      ---

      ```

      Como ejemplo:

      > ```markdown
      > ### 1. Mejora de rendimiento - 1234567890abcdef
      > - **Fecha y Hora:** 2025-07-01 10:00:00
      > - **Enlace al Commit:** [Commit 1234567](https://github.com/usuario/repositorio/commit/1234567890abcdef)
      > - **Título:** Mejora de rendimiento
      > - **Detalles:** Se optimizó el algoritmo de búsqueda para reducir el tiempo de ejecución.
      > - **Archivos Modificados:**
      > - archivo1.py: 10 líneas agregadas | 5 líneas eliminadas.
      > - archivo2.py: 3 líneas agregadas | 2 líneas eliminadas.
      >
      > ---
      >
      > ```

   - **Importante:** Abstente de agregar otras secciones o detalles que no sean estrictamente necesarios para el informe de commits.
   - Asegúrate que cada commit tiene un número correlativo único y que están ordenados por fecha y hora de forma ascendente (del más antiguo al más reciente).
   - Asegúrate que La cantidad de commits sea la misma que la cantidad de líneas en la tabla de commits.
   - Reescribe el archivo `informes/commits_detallados_{mes}_{año}.md` si es necesario, para mantener la consistencia y claridad del informe.

4. Clasificar los cambios por temática

   - Analizar los mensajes, los cambios técnicos y el resumen de cambios realizados en los commits, para generar una lista de cambios, y estos clasificarlos en las siguientes categorías:
     - Mejores en las funcionalidades
     - Corrección de errores (bugfixes)
     - Mejoras de rendimiento
     - Refactorización de código
     - Limpieza de código y comentarios
     - Mejoras en la documentación
     - Mejoras en pruebas (testing)
     - Mejoras en empaquetado y despliegue
     - Actualizaciones de dependencias
     - Otros cambios relevantes

   - Generar un resumen de cambios agrupados por temas.
     - Proceder a ordenar y priorizar los temas dentro de cada categoría.
     - Asegurarse que cada tema tiene una descripción clara y concisa de los cambios realizados.
     - Guardar este resumen en el archivo `informes/resumen_cambios_{mes}_{año}.md`, en la sección correspondiente.
     - Revisar el archivo generado con `markdownlint-cli2` y corregir cualquier problema de formato detectado.
     - El formato del resumen de cambios por temas será el siguiente:

      ```markdown
      ## Resumen de cambios por temas

      ### Nuevas funcionalidades
      - Descripción de las nuevas funcionalidades implementadas.

      ### Corrección de errores
      - Descripción de los errores corregidos.

      ### Refactorización de código
      - Descripción de las refactorizaciones realizadas.

      ### Limpieza de código y comentarios
      - Descripción de la limpieza realizada en el código y comentarios.

      ### Mejoras de rendimiento
      - Descripción de las mejoras de rendimiento implementadas.

      ### Mejoras en la documentación
      - Descripción de las mejoras realizadas en la documentación.

      ### Mejoras en pruebas
      - Descripción de las mejoras realizadas en las pruebas del proyecto.

      ### Mejoras en empaquetado y despliegue
      - Descripción de las mejoras realizadas en el empaquetado y despliegue del proyecto.

      ### Actualizaciones de dependencias
      - Descripción de las actualizaciones realizadas a las dependencias del proyecto.

      ### Otros cambios relevantes
      - Descripción de otros cambios relevantes realizados.
      ```

5. Generar el documento Markdown

   - Estructurar el informe con:
      - Resumen que incluya la Cantidad total de commits.
      - Lista detallada de commits con toda la información relevante.
      - Resumen de cambios agrupados por temas.

6. Revisión final

   - Validar que el documento cumple con los requisitos y está listo para ser entregado.
   - Guardar el informe final en `informes/Informe_Desarrollo_desensibilizador_{mes}_{año}.md`.
   - Revisar todos los archivos Markdown generados con `markdownlint-cli2`:

     ```bash
     markdownlint-cli2 "informes/*.md"
     ```

   - Corregir cualquier problema de formato detectado por el linter en todos los archivos.
