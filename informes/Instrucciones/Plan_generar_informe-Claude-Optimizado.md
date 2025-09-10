# Plan de Generación de Informes de Commits - Optimizado para Claude Code

**Objetivo:** Generar un informe completo y detallado de commits realizados durante un mes específico, aprovechando las capacidades nativas de Claude Code para automatización, análisis técnico y documentación.

## Herramientas y Capacidades de Claude Code

### Herramientas Principales

- **Bash**: Comandos Git con soporte PowerShell/Windows, ejecución paralela
- **Read/Write/Edit/MultiEdit**: Manejo avanzado de archivos con ediciones masivas
- **Grep/Glob**: Búsqueda inteligente de archivos y patrones
- **Task**: Agentes especializados para análisis técnico complejo
- **TodoWrite**: Gestión granular de tareas con seguimiento en tiempo real
- **markdownlint-cli2**: Validación automática de formato markdown

### Optimizaciones Específicas

- **Procesamiento en lotes**: Análisis de múltiples commits simultáneamente
- **Agentes especializados**: Delegación de análisis técnico complejo
- **Ejecución paralela**: Comandos Git concurrentes cuando es posible
- **Validación continua**: Linting automático después de cada generación
- **MultiEdit**: Operaciones masivas de edición en archivos grandes

## Variables del Proyecto

- **{repositorio}**: Auto-detectado del directorio Git actual
- **{mes}** y **{año}**: Definidos por input del usuario
- **{mes como número}**: Conversión automática (enero=01, febrero=02, etc.)

## Proceso Optimizado - 6 Fases

### Fase 0: Preparación Automática

**Tareas automáticas de Claude:**

- Detectar nombre del repositorio desde `git remote -v`
- Verificar herramientas Git y markdownlint-cli2
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
git log --since="YYYY-MM-01" --until="YYYY-MM-31" --pretty=format:"%H|%an|%ad|%s" --date=iso --all
```

**Procesamiento inteligente:**

- Manejo automático de paginación Git
- Estructuración completa de datos en memoria
- Generación automática de enlaces GitHub desde `git remote -v`
- Ordenamiento cronológico (ascendente)
- **Garantía**: Obtención completa de todos los commits

#### 2.2 Generación de Archivo Base

**Archivo:** `commits_{mes}_{año}.md`

**Optimizaciones:**

- Separación automática de título/detalles en mensajes de commit
- Escape automático de caracteres problemáticos (`*` → `+`)
- Formato de tabla markdown optimizado
- **Validación inmediata** con markdownlint-cli2

### Fase 3: Análisis Técnico con Estadísticas

#### 3.1 Extracción de Estadísticas de Archivos

**Comando optimizado por commit:**

```bash
git show --stat {SHA}
```

**Procesamiento automático:**

- Nombres de archivos modificados (con formato `código`)
- Líneas agregadas/eliminadas por archivo
- Correlación exacta archivo ↔ estadísticas
- Actualización masiva con MultiEdit

#### 3.2 Análisis de Diffs Completo

**Comando por commit:**

```bash
git show {SHA}
```

**Procesamiento con Task agent "general-purpose":**

- Análisis técnico detallado de cada diff
- Identificación de cambios en variables, funciones, lógica
- Detección automática de tipos de cambios
- Generación de resúmenes técnicos objetivos

### Fase 4: Documentación Detallada

#### 4.1 Generación de Análisis Detallado

**Archivo:** `commits_detallados_{mes}_{año}.md`

**Con agente especializado Task:**

- Formato estándar por commit con numeración correlativa
- Análisis técnico completo de cambios
- Resúmenes concisos y objetivos
- **Restricción**: Solo contenido solicitado, sin secciones adicionales

**Formato exacto:**

```markdown
### {N}. Título del Commit - {SHA corto}
- **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
- **Enlace al Commit:** [Commit {SHA corto}]({URL GitHub})
- **Título:** {Título mensaje}
- **Detalles:** {Detalles mensaje}
- **Archivos Modificados:**
  - `{archivo}`: {líneas+} líneas agregadas | {líneas-} líneas eliminadas
- **Cambios realizados:**
  - {Lista técnica detallada}
- **Resumen de cambios:**
  {Explicación técnica objetiva}
```

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
- Correlación con cambios técnicos
- Agrupación inteligente por temática
- Priorización por impacto/complejidad

#### 5.2 Generación de Resumen por Temas

**Archivo:** `resumen_cambios_{mes}_{año}.md`

**Formato optimizado:**

```markdown
## {Categoría} - {N} commits

### {Tema específico}
- **Commits:** {N} commits
- **Descripción:** {Descripción técnica concisa}
- **Impacto técnico:** {Impacto identificado}
- **Cambios principales:**
  - {Detalles priorizados por impacto}
```

### Fase 6: Informe Final Consolidado (1 minuto)

#### 6.1 Generación desde Template

**Base:** `Template_Informe_{repositorio}.md`

**Variables auto-completadas:**

- `{repositorio}` → Auto-detectado
- `{mes}` y `{año}` → Del usuario
- `{mes y año solicitado}` → Formato "Mes Año"
- `{Resumen ejecutivo}` → Máximo 4 párrafos, iniciando con cantidad de commits
- `{Resumen por temas}` → Contenido completo del resumen_cambios

**Archivo final:** `Informe_Desarrollo_{repositorio}_{mes}_{año}.md`

#### 6.2 Validación Final Completa

- **Crítico**: markdownlint-cli2 en todos los archivos generados
- Verificación de todos los enlaces GitHub
- Consistencia de formato en todos los documentos
- Completitud de datos procesados

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

## Optimizaciones vs Plan Original

### Mejoras de Eficiencia

- **Tiempo estimado**: 7-12 minutos vs 30-60 minutos manual
- **Procesamiento paralelo**: Comandos Git concurrentes
- **Operaciones masivas**: MultiEdit para archivos grandes
- **Agentes especializados**: Análisis técnico automatizado

### Mejoras de Calidad

- **Validación continua**: Linting en cada fase
- **Consistencia garantizada**: Formato uniforme automático
- **Completitud verificada**: Conteo y verificación de todos los commits
- **Enlaces funcionales**: Verificación automática de URLs GitHub

### Automatización Completa

- **Detección automática**: Repositorio, fechas, estructura
- **Procesamiento inteligente**: Análisis de diffs y clasificación temática
- **Generación masiva**: Todos los documentos con un solo comando
- **Validación integral**: Sin intervención manual para correcciones

Este plan optimizado elimina pasos manuales repetitivos, reduce significativamente el tiempo de ejecución, y garantiza la calidad y completitud del informe final mediante el uso inteligente de las capacidades avanzadas de Claude Code.
