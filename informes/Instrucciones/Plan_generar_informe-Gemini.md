# Plan de Generación de Informes de Commits - Optimizado para Gemini

**Objetivo:** Generar un informe de commits mensual, detallado y de alta calidad, utilizando las capacidades avanzadas de Gemini como agente de codificación para el análisis técnico, la clasificación y la redacción de resúmenes.

## Capacidades de Gemini Utilizadas

- **Herramientas de Terminal (`terminal`):** Ejecución de comandos `git` y `markdownlint-cli2` de forma nativa.
- **Herramientas de Sistema de Archivos (`Read`, `Write`, `Edit`):** Creación y modificación de archivos Markdown de manera eficiente.
- **Bucle de Razonamiento y Acción (ReAct):** Planificación y ejecución de tareas complejas, presentando planes detallados al usuario para su aprobación antes de modificar archivos.
- **Agente Guiado:** Mantenimiento del control del usuario en todo momento, garantizando que cada paso se ejecute con consentimiento explícito.
- **Contexto Ampliado:** Capacidad para procesar grandes volúmenes de información (logs de commits, diffs extensos) para un análisis exhaustivo.
- **Integración con Google Search:** Acceso a información actualizada para enriquecer el análisis técnico si es necesario.

## Variables del Proyecto

- **`{repositorio}`:** Se asignará el nombre `Especificaciones-UI` para el informe.
- **`{mes}` y `{año}`:** Se definirán según la entrada del usuario en la Fase 1.

## Proceso de Implementación por Fases

### Fase 0: Preparación Inicial

Realizaré las siguientes acciones de forma automática, informándote solo si encuentro un error que no pueda resolver:

- Verificaré el acceso al repositorio y los permisos de lectura.
- Confirmaré que las herramientas `git` y `markdownlint-cli2` estén disponibles y funcionales en el entorno.
- Validaré y, si es necesario, crearé la estructura de directorios requerida: `informes/{año}-{mes como número}`.

### Fase 1: Solicitar Parámetros del Informe

- Te preguntaré el mes y el año para generar el informe.
- Validaré que la entrada sea correcta y calcularé el rango de fechas exacto (desde el primer hasta el último día del mes).
- Confirmaré el período seleccionado antes de continuar.

### Fase 2: Extracción y Procesamiento de Commits

#### 2.1. Obtener la Lista de Commits

- Utilizaré mi herramienta `terminal` para ejecutar el siguiente comando `git log`, manejando la paginación si la salida es muy extensa:

    ```powershell
    git log --since="YYYY-MM-01" --until="YYYY-MM-31" --pretty=format:"%H|%an|%ad|%s" --date=iso
    ```

- Si no se encuentran commits, te informaré y finalizaré el proceso.
- Almacenaré la lista completa de commits en una estructura de datos interna, incluyendo: SHA, autor, fecha, mensaje completo y un enlace a GitHub que generaré a partir del remote del repositorio.

#### 2.2. Escribir la Tabla de Commits

- Crearé el archivo `informes/{año}-{mes como número}/commits_{mes}_{año}.md` con la siguiente cabecera y estructura de tabla:

  ```markdown
  # Lista detallada de commits - {mes} {año}

  ## Tabla de commits
  | Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         | Archivo Afectado | Líneas +  | Líneas -   |
  |---------------------|---------------|-------------------|----------------|------------------|------------------|----------:|-----------:|
  ```

- Procesaré cada commit para separar el **título** (primera línea del mensaje) y los **detalles** (resto del mensaje), sin acortarlos.
- Poblaré la tabla con la información de cada commit, ordenados cronológicamente de forma ascendente.
  - Usaré el **SHA corto** (7 caracteres) en la columna `Identificador`.
  - El enlace al commit tendrá el formato `Ver commit`.
  - Las columnas de archivos y líneas se dejarán vacías por ahora.
- Me aseguraré de que la cantidad de filas coincida con el número total de commits obtenidos.

#### 2.3. Determinar Líneas Cambiadas por Commit

- Para cada commit, ejecutaré `git show --stat {SHA}` para obtener los archivos modificados y sus estadísticas.
- Actualizaré la tabla en `commits_{mes}_{año}.md`. Para cada commit con múltiples archivos, usaré `<br>` como separador en las columnas `Archivo Afectado`, `Líneas +` y `Líneas -` para listar cada archivo (rodeado con ` `) y sus estadísticas correspondientes, asegurando que el orden se mantenga en las tres columnas.
- Para commits sin cambios en archivos, usaré "Sin cambios", "0" y "0".
- Al finalizar, validaré que la cantidad total de registros procesados coincida con la cantidad de commits obtenidos.

#### 2.4. Correcciones de Formato

- Reemplazaré los caracteres `*` por `•` en los mensajes de commit. Si hay múltiples reemplazos en el mismo mensaje, los separaré con `<br>`.
- Ejecutaré el linter para validar y corregir el archivo:

    ```powershell
    markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/commits_{mes}_{año}.md"
    ```

#### 2.5. Validación Final de la Tabla

- Me aseguraré de que todos los enlaces a commits de GitHub estén correctamente formateados y sean accesibles.

### Fase 3: Generación de Resumen Detallado por Commit

#### 3.1. Crear Archivo de Commits Detallados

- Crearé el archivo `informes/{año}-{mes como número}/commits_detallados_{mes}_{año}.md`.
- Para cada commit, agregaré una sección con la siguiente estructura exacta, reutilizando la información ya procesada:

  ```markdown
  ## {numero correlativo}. {Título del Commit} - {SHA corto}
  - **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
  - **Enlace al Commit:** Commit {SHA corto}
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

- Dejaré los campos de análisis (`{Lista detallada de cambios técnicos}` y `{Resumen del commit}`) como marcadores de posición para la siguiente etapa.

#### 3.2. Analizar Cada Commit (Proceso Guiado)

Esta es la fase más crítica, donde aplicaré mi modelo de agente guiado:

1. **Análisis del Diff:** Para cada commit, obtendré el `diff` completo con `git diff {SHA}^..{SHA}`.
2. **Plan de Acción:** Analizaré los cambios en el código (variables, lógica, documentación) y el mensaje del commit. Basado en esto, **te presentaré un plan detallado** que describirá el análisis técnico y el resumen que propongo generar.
3. **Aprobación del Usuario:** Esperaré tu confirmación para proceder. Siempre tendrás el control sobre el contenido final.
4. **Ejecución:** Una vez aprobado el plan, completaré las secciones `{Lista detallada de cambios técnicos}` y `{Resumen del commit}` en el archivo `commits_detallados_{mes}_{año}.md`.

**Requisitos del Análisis:**

- **Tono:** El análisis y el resumen serán técnicos, objetivos y directos, sin juicios de valor.
- **Extensión:** El resumen tendrá entre 2 y 8 líneas, proporcional a la complejidad del commit.
- **Commits Vacíos:** Si un commit no tiene cambios en archivos, el resumen indicará "Commit sin cambios en archivos".

#### 3.3. Validar el Documento

- Al finalizar el análisis de todos los commits, validaré el archivo `commits_detallados_{mes}_{año}.md` con el linter de Markdown para asegurar que no haya errores de formato.

### Fase 4: Resumen de Cambios por Temas

#### 4.1. Clasificar los Cambios por Temática

- Utilizaré mi capacidad de análisis para procesar los mensajes de commit y los resúmenes técnicos generados, y clasificaré cada commit en una de las siguientes categorías estándar:
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
- Agruparé los commits por temas dentro de cada categoría y asignaré una prioridad basada en `Impacto`, `Complejidad`, `Alcance`, `Frecuencia` y `Tamaño relativo`, explicando el motivo para rellenar el campo `{Explicación Prioridad}`.

#### 4.2. Generar Resumen por Temas

- Crearé el archivo `informes/{año}-{mes como número}/resumen_cambios_{mes}_{año}.md`.
- Generaré el resumen por temas, siguiendo el formato especificado:

  ```markdown
  ## {Categoría de Cambios} {número de commits en la categoría} commits.

  ### {Tema}
  - **Commits:** {número de commits} commits.
  - **Descripción:** {Descripción del tema}.
  - **Impacto técnico:** {Descripción del impacto técnico de los cambios}.
  - **Cambios principales:**
    - {Detalle de los cambios ordenado por prioridad}. Prioridad: {Explicación Prioridad}
  ```

- Validaré el archivo generado con el linter de Markdown.

### Fase 5: Generación del Informe Final

#### 5.1. Ensamblar el Informe Final

- Utilizaré el template `informes/Instrucciones/Template_Informe_{repositorio}.md`.
- Completaré todos los marcadores de posición:
  - `{repositorio}`, `{mes}`, `{año}` y `{mes y año solicitado}`.
  - `{Resumen de los cambios realizados en el repositorio, indicando la cantidad de commits y principales áreas de mejora o nuevas funcionalidades.}`: Redactaré un resumen ejecutivo técnico y conciso (máximo 4 párrafos) que incluya la cantidad total de commits y los principales cambios.
  - `{Resumen de los cambios agrupados por temas, indicando la cantidad de commits}`: Insertaré el contenido completo del archivo `resumen_cambios_{mes}_{año}.md`.
- Guardaré el resultado como `informes/{año}-{mes como número}/Informe_Desarrollo_{repositorio}_{mes}_{año}.md`.

#### 5.2. Revisión Final

- Realizaré una validación final de todos los documentos generados para asegurar que:
  - Todos los commits estén correctamente listados y analizados.
  - Los resúmenes sean claros, concisos y objetivos.
  - El formato sea profesional y consistente.
  - No haya secciones o detalles no solicitados.
- Ejecutaré el linter de Markdown una última vez sobre todos los archivos para garantizar la máxima calidad.

## Productos Entregables

1. `commits_{mes}_{año}.md` - Tabla detallada de commits.
2. `commits_detallados_{mes}_{año}.md` - Análisis técnico por commit.
3. `resumen_cambios_{mes}_{año}.md` - Resumen agrupado por temas.
4. `Informe_Desarrollo_{repositorio}_{mes}_{año}.md` - Informe final consolidado.
