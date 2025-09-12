# Plan de Generación de Informes de Commits - Optimizado para Claude Code

**Objetivo:** Generar un informe completo y detallado de commits realizados durante un mes específico, aprovechando las capacidades nativas de Claude Code para automatización, análisis técnico y documentación.

## Herramientas y Capacidades de Claude Code

### Herramientas Principales

- **Bash**: Comandos Git con soporte PowerShell/Windows, ejecución paralela
- **Read/Write/Edit/MultiEdit**: Manejo avanzado de archivos con ediciones masivas
- **Grep/Glob**: Búsqueda inteligente de archivos y patrones
- **Task**: Agentes especializados para análisis técnico complejo
- **TodoWrite**: Gestión granular de tareas con seguimiento en tiempo real
- **markdownlint-cli2**: Validación automática con configuración específica:

  ```powershell
  markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/commits_{mes}_{año}.md"
  ```

### Optimizaciones Específicas

- **Procesamiento en lotes**: Análisis de múltiples commits simultáneamente
- **Agentes especializados**: Delegación de análisis técnico complejo
- **Ejecución paralela**: Comandos Git concurrentes cuando es posible
- **Validación continua**: Linting automático después de cada generación
- **MultiEdit**: Operaciones masivas de edición en archivos grandes

## Variables del Proyecto

- **{repositorio}**: `Especificaciones-UI` Asignado para el informe
- **{mes}** y **{año}**: Definidos por input del usuario
- **{mes como número}**: Conversión automática (enero=01, febrero=02, etc.)

## Proceso Optimizado - 6 Fases

### Fase 0: Preparación Automática

**Tareas automáticas de Claude:**

- Asegurarse que tienes acceso al repositorio en GitHub y que puedes clonarlo localmente si es necesario
- Asegurarse que tienes permisos para leer los commits y detalles del repositorio
- Verificar herramientas Git y markdownlint-cli2 están instaladas y funcionan correctamente
- Validar/crear estructura: `informes/{año}-{mes como número}/`
- Configurar variables del proyecto automáticamente

**Nota:** Solo reportar al usuario si hay errores críticos

### Fase 1: Configuración de Período

**Interacción con usuario:**

- Solicitar mes y año específico
- Validación automática (1-12 para mes, año coherente)
- Cálculo automático del rango de fechas completo
- Confirmación de período seleccionado

### Fase 2: Extracción Masiva de Datos

#### 2.1 Comando Git Optimizado

```powershell
git log --since="YYYY-MM-01" --until="YYYY-MM-31" --pretty=format:"%H|%an|%ad|%s" --date=iso --reverse
```

**Procesamiento inteligente:**

- **Crítico**: Obtener la lista completa de commits del rango de fechas, considerando que la información puede llegar en lotes y no completa de una sola vez. Usar paginación si es necesario
- Asegurarse que se obtienen todos los commits, sin omitir ninguno
- Si no hay commits en el rango de fechas, informar al usuario y finalizar el proceso
- Estructuración completa de datos en memoria
- Generación automática de enlaces GitHub desde `git remote -v`
- Ordenamiento cronológico ascendente (del más antiguo al más reciente)
- **Garantía**: Obtención completa de todos los commits

**Cada commit debe incluir:**

- Identificador único (SHA)
- Autor
- Fecha y hora
- Mensaje de commit completo
- Enlace al commit en GitHub (se completará después si no se puede obtener inicialmente)

#### 2.2 Generación de Archivo Base

**Archivo:** `commits_{mes}_{año}.md`

**Formato del encabezado del archivo:**

```markdown
# Lista detallada de commits - {mes} {año}

Generado usando `{nombre archivo del plan}`.

## Tabla de commits
| Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         | Archivo Afectado | Líneas +  | Líneas -   |
|---------------------|---------------|-------------------|----------------|------------------|------------------|----------:|-----------:|
| YYYY-MM-DD HH:MM:SS | SHA corto     | [Commit {SHA corto}](URL) | Título Mensaje | Detalles Mensaje |`Archivo1`<br>`Archivo2`<br>`Archivo3` |num_agregadas1<br>num_agregadas2<br>num_agregadas3|num_eliminadas1<br>num_eliminadas2<br>num_eliminadas3|
```

**Nota:** los campos `archivo`, `num_agregadas` y `num_eliminadas` se completarán en la siguiente etapa.

**Procesamiento de cada commit:**

- Para cada commit obtener los detalles:
  - Identificador único (SHA)
  - Fecha y hora
  - Enlace al commit
  - **Separación específica de Título y Detalles desde el mensaje de commit**, sin resumir ni acortarlos:
    - **El Título es la primera línea antes de un salto de línea**
    - **Detalles son el resto del mensaje, y puede resultar vacío si el mensaje de commit es solo una línea**

**Requisitos de escritura:**

- Escribir la información al archivo, donde cada fila de la tabla debe corresponder a un commit
- **Commits ordenados por fecha y hora ascendente (del más antiguo al más reciente)**
- Fecha y hora en formato `YYYY-MM-DD HH:MM:SS`
- Asegurarse que la cantidad de commits sea la misma que la cantidad de líneas en la tabla
- **Abstenerse de agregar otras secciones o detalles**

**Optimizaciones:**

- **Crítico**: Escape automático de caracteres problemáticos (`*` → `•`) en Título y Detalles
- Separación con `<br>` si hay múltiples reemplazos en la misma línea
- **Validación inmediata** con markdownlint-cli2

### Fase 3: Análisis Técnico con Estadísticas

#### 3.1 Extracción de Estadísticas de Archivos

**Comando optimizado por commit:**

```bash
git show --stat {SHA}
```

**Procesamiento automático:**

- Nombres de archivos modificados (cada archivo rodeado con caracteres '`')
- Separación de múltiples archivos con `<br>`
- Para cada archivo modificado en el commit, obtener:
  - Nombre del archivo
  - Número de líneas agregadas
  - Número de líneas eliminadas
- **Actualizar archivo con estadísticas**:
  - Si un commit no tiene archivos modificados, escribir "Sin cambios", "0" y "0" en las columnas de archivos afectados, líneas agregadas y líneas eliminadas, respectivamente
  - Si el commit tiene al menos un archivo modificado, listar todos los archivos y sus respectivas líneas agregadas y eliminadas, separando los nombres de los archivos con saltos de línea (`<br>`)
    - Cada nombre de archivo debe estar rodeado con caracteres '`' para formato de código
  - Escribir el valor de líneas agregadas y eliminadas en las columnas correspondientes, separando los números con saltos de línea (`<br>`) para múltiples archivos, asegurándose que cada número corresponda al archivo en la misma posición
  - No omitir ningún archivo, incluso si son muchos
- Correlación exacta archivo ↔ estadísticas (mismo orden/posición)
- Actualización masiva con MultiEdit
- Validación: cantidad procesada = cantidad total de commits

#### 3.2 Correcciones de Formato Críticas

**Tareas obligatorias:**

- Reemplazar caracteres `*` por `•` en mensajes para evitar conflictos markdown
- Si hay múltiples reemplazos en el mismo mensaje, separarlos con `<br>`
- Validación inmediata con markdownlint-cli2 usando configuración específica
- Verificación de todos los enlaces GitHub correctamente formateados y accesibles

#### 3.3 Análisis de Diffs Completo

**Comando por commit:**

```bash
git show {SHA}
git diff {SHA}^..{SHA}  # Para análisis detallado de cambios
```

**Uso específico de agentes especializados:**

Si tienes la capacidad de crear subagentes, utilízalos y delega estas tareas a un subagente especializado en análisis de código y generación de resúmenes técnicos. Si no tienes la capacidad de crear subagentes, realiza esta tarea tú mismo.

- **Nombre del subagente**: "Agente Analista de Commits"
- **Capacidades requeridas**: Leer y analizar diffs de código, entender cambios en variables, lógica y documentación, y generar resúmenes técnicos claros
- **Prompt detallado debe incluir**:
  - El contexto del proyecto
  - El objetivo del análisis
  - El formato esperado para la respuesta
  - Cualquier restricción o detalle específico que deba considerar
- Generar varios subagentes si es necesario para dividir la carga de trabajo
- Supervisar el progreso del subagente y asegurarse de que cumple con los requisitos
- Revisar y validar la información proporcionada por el subagente antes de integrarla

**Procesamiento con Task agent "Agente Analista de Commits":**

- **Detección de commits vacíos**: Identificar commits sin cambios en archivos
- Análisis técnico detallado de cada diff completo usando `git diff`
- Identificación específica de:
  - Cambios en variables (nuevas, eliminadas, renombradas, modificadas)
  - Cambios en lógica (funciones, estructuras de control)
  - Cambios en documentación (comentarios)
  - Cambios en archivos de configuración
- Generación de resúmenes técnicos objetivos proporcionales a la complejidad:
  - **Commits simples** (1-2 archivos, cambios menores): 1-3 líneas
  - **Commits moderados** (múltiples archivos, cambios significativos): 3-5 líneas
  - **Commits complejos** (refactorizaciones, nuevas funcionalidades): 5-8 líneas
  - **Criterios de complejidad**: número de archivos, líneas modificadas, tipo de cambios (lógica vs documentación)
- **Requisitos del análisis**:
  - Técnico y claro, explicando qué cambió y por qué
  - Evitar redundancias y explicaciones innecesarias
  - Tono objetivo, evitando juicios de valor y adjetivos rimbombantes

### Fase 4: Documentación Detallada

#### 4.1 Generación de Análisis Detallado

**Archivo:** `commits_detallados_{mes}_{año}.md`

**Formato del encabezado del archivo:**

```markdown
# Análisis detallado de commits - {mes} {año}

Generado usando `{nombre archivo del plan}`.

---

```

**Con agente especializado Task:**

- Formato estándar por commit con numeración correlativa
- Análisis técnico completo de cambios
- Resúmenes concisos y objetivos
- **Restricción CRÍTICA**: Solo contenido solicitado, sin secciones adicionales
- **Abstención obligatoria**: No agregar detalles no estrictamente necesarios
- **Manejo de commits vacíos**: Si no hay cambios, indicar "Commit sin cambios en archivos"
- **Evaluación de complejidad para resúmenes proporcionales**:
  - **Commits simples**: Cambios menores en documentación, correcciones ortográficas, ajustes de formato → 1-3 líneas
  - **Commits moderados**: Múltiples archivos modificados, nuevas características menores, refactorizaciones simples → 3-5 líneas
  - **Commits complejos**: Refactorizaciones mayores, nuevas funcionalidades significativas, cambios arquitectónicos → 5-8 líneas

**Formato exacto por commit:**

```markdown
## {N}. {Título del Commit} - {SHA corto}
- **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
- **Enlace al Commit:** [Commit {SHA corto}]({URL GitHub})
- **Título:** {Título mensaje}
- **Detalles:** {Detalles mensaje}
- **Archivos Modificados:**
  - `{archivo}`: {líneas+} líneas agregadas | {líneas-} líneas eliminadas
- **Cambios realizados:**
  - {Lista técnica detallada específica}
- **Resumen de cambios:**
  {Explicación técnica objetiva proporcional a la complejidad del commit}

---
```

**Requisitos de formato específicos:**

- Usar exactamente títulos y detalles saneados de la tabla original
- Ordenar commits cronológicamente ascendente
- Numeración correlativa única comenzando en 1
- Para commits vacíos: "Commit sin cambios en archivos" y terminar procesamiento

#### 4.2 Validación Automática

- **Obligatorio**: markdownlint-cli2 sin errores
- Verificación de enlaces GitHub
- Consistencia de formato y numeración

### Fase 5: Clasificación y Resumen

#### 5.1 Clasificación Temática Automática

**Categorías estándar:**

- Mejoras en funcionalidades
- Corrección de errores (bugfixes)
- Mejoras de rendimiento
- Refactorización de código
- Limpieza de código y comentarios
- Mejoras en documentación
- Mejoras en pruebas (testing)
- Mejoras en empaquetado y despliegue
- Actualizaciones de dependencias
- Otros cambios relevantes

**Proceso con agente Task:**

- Análisis automático de mensajes de commit
- Correlación con cambios técnicos identificados
- Identificación de temas relevantes
- Agrupación automática por categoría y temática dentro de cada categoría
- **Priorización dentro de cada categoría por**:
  - Impacto (afecta funcionalidad central / superficie de usuarios)
  - Complejidad (cambios simples versus complejos)
  - Alcance (número de archivos o módulos)
  - Frecuencia (cantidad de commits similares)
  - Tamaño relativo (líneas modificadas netas)
- **Crítico**: Describir brevemente la prioridad asignada a cada tema, registrando el motivo, para completar el campo `{Explicación Prioridad}`
- Asignación de un tema a cada commit, asegurando que cada tema tenga una descripción clara y concisa

#### 5.2 Generación de Resumen por Temas

**Archivo:** `resumen_cambios_{mes}_{año}.md`

**Formato del encabezado del archivo:**

```markdown
# Resumen de cambios por temas

Generado usando `{nombre archivo del plan}`.

```

**Requisitos para el resumen de cambios:**

- Asegurarse que cada tema tiene una descripción clara y concisa de los cambios realizados
- Si una categoría no tiene temas, no debe incluirse en el resumen
- El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes. Usar un tono profesional y objetivo

**Formato por categoría y tema:**

```markdown
## {Categoría de Cambios} - {número de commits en la categoría} commits

### {Tema}
- **Commits:** {número de commits} commits
- **Descripción:** {Descripción del tema}
- **Impacto técnico:** {Descripción del impacto técnico de los cambios}
- **Cambios principales:**
  - {Detalle de los cambios ordenado por prioridad}. Prioridad: {Explicación Prioridad}
```

### Fase 6: Informe Final Consolidado

#### 6.1 Generación desde Template

**Base:** `informes/Instrucciones/Template_Informe_{repositorio}.md`

**Variables auto-completadas:**

- `{nombre archivo del plan}`: Nombre del archivo del plan actual.
- `{repositorio}` → Nombre asignado al repositorio para el informe
- `{mes}` → Mes seleccionado por el usuario
- `{año}` → Año seleccionado por el usuario
- `{mes y año solicitado}` → Formato "Mes Año" (ej: "Julio 2025")
- `{Resumen ejecutivo}` → Resumen técnico en máximo 4 párrafos:
  - Incluir cantidad total de commits
  - Listar principales cambios de las dos primeras categorías
  - Explicar qué cambió y por qué (técnico y claro)
  - Tono profesional y objetivo, sin adjetivos rimbombantes
- `{Resumen por temas}` → Contenido completo del archivo resumen_cambios

**Archivo final:** `Informe_Desarrollo_{repositorio}_{mes}_{año}.md`

#### 6.2 Validación Final Completa

- **Crítico**: markdownlint-cli2 con configuración específica:

  ```powershell
  markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/*.md"
  ```

- Verificación de todos los enlaces GitHub funcionales
- Completitud: cantidad de commits procesados = cantidad listada
- Sin secciones adicionales no solicitadas en ningún documento

#### 6.3 Revisión Final de Requisitos

**Validación obligatoria antes de entregar:**

- Verificar que todos los commits están listados y detallados correctamente
- Confirmar que el resumen de cambios por temas es claro y conciso
- Validar formato consistente y profesional en todos los documentos
- **Crítico**: No debe haber secciones o detalles no solicitados en ningún informe
- El informe debe centrarse exclusivamente en commits y cambios realizados

## Productos Entregables

1. **`commits_{mes}_{año}.md`** - Tabla completa con estadísticas
2. **`commits_detallados_{mes}_{año}.md`** - Análisis técnico detallado
3. **`resumen_cambios_{mes}_{año}.md`** - Clasificación temática
4. **`Informe_Desarrollo_{repositorio}_{mes}_{año}.md`** - Documento final consolidado

## Gestión de Tareas con TodoWrite

Claude utilizará TodoWrite para:

- **Planificación granular**: Cada sub-tarea como ítem individual
- **Seguimiento en tiempo real**: Estado actualizado continuamente
- **Progreso visible**: El usuario ve el avance paso a paso
- **Detección de problemas**: Identificación temprana de issues
- **Completitud garantizada**: Verificación de que todas las tareas se completan
