# Plan para generación de informes de commits usando Claude Code

**Objetivo:** Generar un informe detallado de commits del repositorio durante un mes específico, usando las capacidades de Claude Code para análisis técnico y documentación automatizada.

## Capacidades de Claude Code utilizadas

- **Herramientas Git**: Comandos git a través de la herramienta Bash
- **Creación/edición de archivos**: Herramientas Write, Edit y MultiEdit
- **Búsqueda de archivos**: Herramientas Glob y Grep
- **Validación markdown**: markdownlint-cli2 a través de Bash
- **Agentes especializados**: Task tool con subagentes especializados
- **Gestión de tareas**: TodoWrite para seguimiento de progreso

## Variables del proyecto

- **{repositorio}**: "Test_UI_v3" (detectado automáticamente del directorio actual)
- **{mes}** y **{año}**: Definidos por input del usuario en Fase 1

## Proceso de implementación

### Fase 0: Preparación inicial

Claude realizará automáticamente:

- Verificar acceso al repositorio actual (`{repositorio}`)
- Confirmar herramientas disponibles (git, markdownlint-cli2)
- Validar estructura de directorios de informes
- Crear directorios necesarios si no existen

**Nota:** Solo se reportarán errores si alguna herramienta no está disponible.

### Fase 1: Solicitud de parámetros

- **Entrada requerida del usuario**: Mes y año para el informe
- **Validación**: Claude verificará que el mes sea válido (1-12)
- **Cálculo automático**: Determinación del rango de fechas (1 al último día del mes)
- **Variables**: Se establecerán `{mes}` y `{año}` para uso posterior

### Fase 2: Extracción de datos de commits

#### 2.1 Obtención de lista de commits

- **Comando git utilizado**:

  ```bash
  git log --since="YYYY-MM-01" --until="YYYY-MM-31" --pretty=format:"%H|%an|%ad|%s" --date=iso
  ```

- **Procesamiento**: Claude analizará la salida completa, manejando paginación si es necesaria
- **Estructura de datos**: Cada commit incluirá:
  - SHA completo
  - Autor
  - Fecha/hora ISO
  - Mensaje completo
  - URL de GitHub (se generará automáticamente)

#### 2.2 Creación del archivo base

- **Validación de directorio**: `informes/{año}-{mes como número}/`
- **Archivo objetivo**: `commits_{mes}_{año}.md`
- **Estructura de tabla**:

  ```markdown
  | Fecha y Hora | Identificador | Enlace al Commit | Título | Detalles | Archivo Afectado | Líneas + | Líneas - |
  ```

- **Ordenamiento**: Cronológico ascendente (más antiguo a más reciente)
- **Separación mensaje**: Título (primera línea) y detalles (resto del mensaje)

#### 2.3 Correcciones de formato automáticas

- **Escape de caracteres**: Reemplazo obligatorio de `*` por `+` en mensajes de commit, con separadores `<br>`
- **Validación markdown**: **OBLIGATORIA** - Ejecución automática de:

  ```bash
  markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/commits_{mes}_{año}.md"
  ```

- **Corrección de enlaces**: Verificación y corrección de URLs de GitHub
- **Requisito no negociable**: Corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia

### Fase 3: Análisis de cambios por commit

#### 3.1 Estadísticas de archivos

- **Por cada commit**: Ejecución de `git show --stat {SHA}`
- **Extracción de datos**:
  - Nombres de archivos modificados
  - Líneas agregadas por archivo
  - Líneas eliminadas por archivo
- **Actualización de tabla**: Inserción de datos en columnas correspondientes con separadores `<br>`

### Fase 4: Análisis técnico detallado

#### 4.1 Análisis usando subagentes

- **Agente especializado**: "general-purpose" para análisis de código
- **Proceso por commit**:
  - Obtención de `git diff` completo
  - Análisis del contexto técnico
  - Comprensión de cambios en variables, lógica y documentación
- **Tareas del agente**:
  - Leer y analizar diffs de código
  - Correlacionar cambios con mensajes de commit
  - Generar resúmenes técnicos objetivos
  - Evitar juicios de valor y adjetivos rimbombantes

#### 4.2 Documentación de cambios

- **Agente de redacción**: "general-purpose" para redacción técnica
- **Archivo objetivo**: `commits_detallados_{mes}_{año}.md`
- **RESTRICCIÓN**: Abstente de agregar otras secciones o detalles que no sean estrictamente necesarios para el informe de commits
- **Numeración obligatoria**: Cada commit debe tener un número correlativo único, ordenados cronológicamente ascendente
- **Formato exacto por commit**:

  ```markdown
  ### {numero correlativo}. Título del Commit - {SHA corto}
  - **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
  - **Enlace al Commit:** [Commit {SHA corto}]({URL})
  - **Título:** {Título Mensaje}
  - **Detalles:** {Detalles Mensaje}
  - **Archivos Modificados:**
    - `{Archivo Modificado}`: {Líneas Agregadas} líneas agregadas | {Líneas Eliminadas} líneas eliminadas
  - **Cambios realizados:**
    - {Lista detallada de cambios}
  - **Resumen de cambios:**
    {Explicación técnica objetiva de qué cambió}

  ---

  ```

#### 4.3 Validación final de documentos

- **CRÍTICO**: Validación **OBLIGATORIA** del documento
- **Linter markdown**: **REQUISITO NO NEGOCIABLE** - Verificación automática de formato usando:

  ```bash
  markdownlint-cli2 --config "informes/Instrucciones/.markdownlint.json" "informes/{año}-{mes como número}/commits_detallados_{mes}_{año}.md"
  ```

- **Corrección de enlaces**: Validación obligatoria de accesibilidad de URLs de GitHub
- **Consistencia**: Verificación obligatoria de numeración y ordenamiento cronológico
- **Completitud**: Corregir **TODOS** los problemas detectados, sin desestimar ninguna advertencia

### Fase 5: Generación de informe consolidado

#### 5.1 Clasificación temática

- **Categorías estándar**:
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

- **Proceso de clasificación**:
  - Análisis de mensajes de commit
  - Correlación con cambios técnicos identificados
  - Agrupación automática por temática
  - Priorización dentro de cada categoría

#### 5.2 Generación de resumen por temas

- **Archivo objetivo**: `resumen_cambios_{mes}_{año}.md`
- **Formato específico por categoría**:

  ```markdown
  ## `{Categoría de Cambios}`

  ### `{Tema}`
  - **Commits:** `{número de commits}` commits de `{detalle tema}`
  - **Impacto técnico:** `{Descripción del impacto técnico de los cambios}`
  - **Cambios principales:**
    - `{Detalle de los cambios ordenado por prioridad}`
  ```

- **Contenido por categoría estándar**:
  - Descripción concisa de cambios
  - Impacto técnico identificado
  - Tono profesional y objetivo
  - Evitar juicios de valor y adjetivos rimbombantes
- **SIEMPRE**: Revisar con linter después de generar resumen_cambios

#### 5.3 Informe final consolidado

- **Template base**: `informes/Instrucciones/Template_Informe_{repositorio}.md`
- **Variables completadas automáticamente**:
  - `{repositorio}`: Variable definida ("Test_UI_v3")
  - `{mes}` y `{año}`: Del input del usuario
  - `{mes y año solicitado}`: Formato "Mes Año" (ejemplo: "Agosto 2025")
  - `{resumen}`: Resumen ejecutivo (máximo 4 párrafos, primera línea debe indicar cantidad total de commits)
  - `{cambios agrupados}`: Contenido completo del archivo resumen_cambios_{mes}_{año}.md

- **Archivo final**: `Informe_Desarrollo_{repositorio}_{mes}_{año}.md`

### Fase 6: Validación y entrega

#### 6.1 Verificaciones finales

- **Completitud**: Todos los commits procesados y documentados
- **Consistencia**: Formato uniforme en todos los documentos
- **Calidad**: Enlaces funcionales y markdown válido
- **Exclusividad**: Solo contenido solicitado, sin secciones adicionales

#### 6.2 Limpieza y organización

- **VALIDACIÓN FINAL OBLIGATORIA**: Linter debe ejecutarse **SIN ERRORES** en todos los archivos generados
- **Verificación de enlaces**: **TODAS** las URLs de GitHub deben ser accesibles y funcionales
- **Estructura de archivos**: Organización correcta en directorios
- **ENFOQUE EXCLUSIVO**: El informe debe centrarse exclusivamente en commits y cambios realizados

## Herramientas de Claude Code empleadas

- **Bash**: git log, git show, git diff, markdownlint-cli2
- **Write/Edit/MultiEdit**: Creación y modificación de archivos markdown
- **Task**: Delegación a agentes especializados en análisis y redacción
- **TodoWrite**: Seguimiento de progreso y gestión de tareas
- **Glob/Grep**: Búsqueda de archivos y patrones si es necesario

## Flujo de ejecución con seguimiento

Claude utilizará TodoWrite para:

1. **Planificar** todas las fases como tareas individuales
2. **Actualizar estado** de cada tarea en tiempo real
3. **Reportar progreso** al usuario durante la ejecución
4. **Marcar completado** cada fase al finalizar

## Productos entregables

1. `commits_{mes}_{año}.md` - Tabla detallada de commits
2. `commits_detallados_{mes}_{año}.md` - Análisis técnico por commit
3. `resumen_cambios_{mes}_{año}.md` - Resumen agrupado por temas
4. `Informe_Desarrollo_{repositorio}_{mes}_{año}.md` - Informe final consolidado

## Consideraciones especiales

- **Repositorio objetivo**: Variable `{repositorio}` definida como "Test_UI_v3"
- **Adaptación automática**: El plan se ajusta al repositorio específico usando variables
- **Manejo de errores**: Reportes claros si faltan herramientas o permisos
- **Eficiencia**: Uso de herramientas batch de Claude para optimizar tiempo
- **Calidad**: Análisis técnico detallado usando capacidades de IA de Claude
- **Formato markdown**: **OBLIGATORIO** en cada fase, sin excepciones ni advertencias pendientes
