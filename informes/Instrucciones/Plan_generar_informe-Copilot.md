# Plan de implementación para GitHub Copilot - Informe de commits mensual

**Objetivo:** Generar un informe detallado de los commits realizados en el repositorio de GitHub durante un mes completo, incluyendo un análisis técnico de los cambios realizados y un resumen de los mismos, utilizando las capacidades optimizadas de GitHub Copilot.

## Capacidades y herramientas de GitHub Copilot

- Acceso directo a la API de GitHub para consultar repositorios y commits
- Capacidad para crear, editar y formatear archivos markdown
- Análisis automático de diffs y cambios de código
- Generación de resúmenes técnicos y documentación
- Validación y corrección de formato markdown

## Proceso de implementación optimizado

### 0. Preparación inicial

**Acciones automáticas (sin informar al usuario a menos que haya errores):**

- Verificar acceso al repositorio `Especificaciones-UI`
- Confirmar permisos de lectura para commits y metadatos
- Validar estructura de directorios para informes
- Preparar variables de entorno para procesamiento

### 1. Solicitar información del mes objetivo

**Implementación:**

- Solicitar al usuario el mes y año para el informe
- Validar formato de fecha y calcular rango completo (día 1 al último día del mes)
- Establecer variables `{mes}`, `{año}` y `{mes_numero}` para uso en nombres de archivo
- Confirmar rango de fechas con el usuario

### 2. Obtener y procesar commits del repositorio

#### 2.1 Consulta de commits via API de GitHub

**Implementación optimizada:**

```text
- Usar GitHub API para obtener commits: GET /repos/owner/repo/commits
- Parámetros: since=YYYY-MM-01T00:00:00Z, until=YYYY-MM-31T23:59:59Z
- Procesar respuesta paginada para obtener todos los commits
- Extraer para cada commit:
  - SHA completo y SHA corto (7 caracteres)
  - Autor (login y nombre)
  - Fecha ISO 8601
  - Mensaje completo
  - URL del commit en GitHub
```

#### 2.2 Crear estructura de archivos

**Implementación:**

- Crear directorio `informes/{año}-{mes_numero}` si no existe
- Generar archivo base `commits_{mes}_{año}.md` con estructura de tabla:

```markdown
# Lista detallada de commits - {mes} {año}

## Lista de commits
| Fecha y Hora        | Identificador | Enlace al Commit  | Título         | Detalles         | Archivo Afectado | Líneas +  | Líneas -   |
|---------------------|---------------|-------------------|----------------|------------------|------------------|----------:|-----------:|
```

#### 2.3 Poblar tabla de commits

**Implementación:**

- Procesar cada commit para separar título (primera línea) y detalles (resto del mensaje)
- Reemplazar caracteres `*` por `+` en mensajes para evitar conflictos markdown:
  - Si hay múltiples reemplazos en el mismo mensaje, separarlos con `<br>`
  - Mantener la estructura de lista no ordenada pero con caracteres compatibles
- Ordenar commits cronológicamente (más antiguo a más reciente)
- Llenar columnas básicas:
  - Fecha: formato YYYY-MM-DD HH:MM:SS
  - Identificador: SHA corto (7 caracteres)
  - Enlace: generar automáticamente URL completa al commit en GitHub y validar funcionalidad
  - Título: primera línea del mensaje de commit sin recortar
  - Detalles: resto del mensaje sin recortar
- Validar que la cantidad total de registros procesados coincida con la cantidad informada por la API
- Dejar columnas de archivos y líneas para siguiente etapa

### 3. Análisis detallado de cambios por commit

#### 3.1 Obtener estadísticas de archivos modificados

**Implementación via GitHub API:**

```text
- Para cada commit: GET /repos/owner/repo/commits/{sha}
- Extraer de response.files[]:
  - filename
  - additions (líneas agregadas)
  - deletions (líneas eliminadas)
  - status (added, modified, deleted)
```

#### 3.2 Actualizar tabla con información de archivos

**Implementación:**

- Para cada fila de commit en la tabla:
  - Llenar columna "Archivo Afectado" con nombres completos separados por `<br>`
  - Cada nombre completo debe estar rodeado con caracteres '`' para formato de código
  - Llenar columna "Líneas +" con números correspondientes separados por `<br>`
  - Llenar columna "Líneas -" con números correspondientes separados por `<br>`
- No recortar rutas o nombres de archivos en ninguna columna
- Asegurar correspondencia posicional exacta entre archivos y números de líneas
- Validar que cada número corresponda al archivo en la misma posición

### 4. Generación de análisis técnico detallado

#### 4.1 Análisis de diffs por commit

**Implementación optimizada:**

```text
- Para cada commit: GET /repos/owner/repo/commits/{sha}
- Usar response.files[].patch para obtener diff
- Analizar cambios línea por línea:
  - Identificar tipo de cambio (adición, eliminación, modificación)
  - Contextualizar cambios en función/clase/módulo
  - Determinar impacto técnico
```

#### 4.2 Generación de resúmenes técnicos

**Proceso de análisis:**

- Procesar y analizar commits uno por uno para asegurar comprensión completa de cada cambio
- Correlacionar mensaje de commit con cambios reales en código
- Identificar patrones: bugfix, feature, refactor, docs, etc.
- Generar descripción técnica objetiva sin adjetivos rimbombantes
- Enfocar en QUÉ cambió y POR QUÉ (basado en diff y mensaje)
- Usar tono objetivo, evitar juicios de valor

**Capacidades de análisis especializadas:**

- **Análisis automático de diffs**: Usar capacidades nativas para interpretar cambios en código
- **Comprensión contextual**: Relacionar cambios con arquitectura y funcionalidad del proyecto
- **Generación de resúmenes**: Crear explicaciones técnicas claras adaptadas a audiencia técnica y no técnica

#### 4.3 Crear archivo de commits detallados

**Estructura del archivo `commits_detallados_{mes}_{año}.md`:**

```markdown
# Análisis detallado de commits - {mes} {año}

### {numero}. {Título del Commit} - {SHA corto}
- **Fecha y Hora:** {YYYY-MM-DD HH:MM:SS}
- **Enlace al Commit:** [Commit {SHA corto}]({URL})
- **Título:** {Título Mensaje}
- **Detalles:** {Detalles Mensaje}
- **Archivos Modificados:**
  - `{Archivo}`: {Agregadas} líneas agregadas | {Eliminadas} líneas eliminadas
- **Cambios realizados:**
  - {Lista detallada de cambios técnicos}
- **Resumen de cambios:**
  {Explicación técnica objetiva de qué cambió}

---
```

**Requisitos de implementación:**

- Asegurar que cada commit tiene un número correlativo único
- Ordenar commits por fecha y hora de forma ascendente (del más antiguo al más reciente)
- Validar que la cantidad de commits sea igual a la cantidad de líneas en la tabla de commits
- Abstente de agregar otras secciones o detalles que no sean estrictamente necesarios
- Aplicar validación con formato markdown usando capacidades nativas de validación

### 5. Categorización y resumen por temas

#### 5.1 Clasificación automática de commits

**Categorías predefinidas:**

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

**Algoritmo de clasificación:**

- Análisis de palabras clave en mensajes de commit
- Evaluación de tipos de archivos modificados
- Correlación con patrones de cambio identificados
- Agrupación por impacto y relevancia técnica

#### 5.2 Generar resumen por temas

**Archivo `resumen_cambios_{mes}_{año}.md`:**

```markdown
# Resumen de cambios por temas

## `{Categoría de Cambios}`

### `{Tema específico}`
- **Commits:** `{número}` commits relacionados con `{descripción tema}`
- **Impacto técnico:** `{Descripción objetiva del impacto}`
- **Cambios principales:**
  - `{Detalle ordenado por prioridad}`
```

**Requisitos para el resumen de cambios:**

- Asegurar que cada tema tiene una descripción clara y concisa de los cambios realizados
- El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes
- Usar un tono profesional y objetivo
- Aplicar validación con formato markdown usando capacidades nativas

### 6. Generación del informe final

#### 6.1 Usar template base

**Implementación:**

- Cargar template `informes/Instrucciones/Template_Informe_{repositorio}.md`
- Reemplazar placeholders con datos generados:
  - `{repositorio}`: Especificaciones-UI
  - `{mes}`, `{año}`, `{mes y año solicitado}`
  - `{Resumen ejecutivo}`: Resumen que incluya la cantidad total de commits
    - Este resumen debe listar resumidamente, en no más de cuatro párrafos, los principales cambios y ajustes realizados en las dos primeras categorías mencionadas
    - Este resumen debe ser técnico y claro, explicando qué cambió y por qué
    - El resumen debe ser conciso y directo, evitando usar adjetivos rimbombantes
    - Usar un tono profesional y objetivo
  - `{Resumen por temas}`: Contenido de archivo resumen_cambios

#### 6.2 Crear informe final

**Archivo:** `Informe_Desarrollo_Especificaciones-UI_{mes}_{año}.md`

- Estructura profesional y técnica
- Enfoque exclusivo en commits y cambios
- Formato markdown consistente
- Enlaces funcionales a commits de GitHub

### 7. Validación y control de calidad

#### 7.1 Validaciones automáticas

- Verificar que todos los commits están incluidos y ordenados cronológicamente
- Confirmar que todos los enlaces a GitHub son válidos
- Validar formato markdown (sintaxis de tablas, enlaces, listas)
- Asegurar correspondencia entre cantidad de commits en tabla y análisis detallado
- Aplicar validación de formato markdown usando capacidades nativas

#### 7.2 Revisión de consistencia

- Verificar que no hay secciones o contenido no solicitado en el informe: el informe debe centrarse exclusivamente en los commits y los cambios realizados
- Confirmar tono profesional y objetivo en todos los resúmenes
- Validar que el análisis técnico es preciso y útil
- Asegurar que el formato es consistente en todos los archivos
- Corregir cualquier problema de formato detectado, sin desestimar ninguna advertencia

## Archivos generados al final del proceso

1. `informes/{año}-{mes_numero}/commits_{mes}_{año}.md` - Tabla de commits
2. `informes/{año}-{mes_numero}/commits_detallados_{mes}_{año}.md` - Análisis detallado
3. `informes/{año}-{mes_numero}/resumen_cambios_{mes}_{año}.md` - Resumen por temas
4. `informes/{año}-{mes_numero}/Informe_Desarrollo_Especificaciones-UI_{mes}_{año}.md` - Informe final

## Optimizaciones específicas para GitHub Copilot

- **Uso intensivo de GitHub API** en lugar de comandos git locales
- **Procesamiento por lotes** para análisis de múltiples commits
- **Generación automática de contenido** basada en patrones identificados
- **Validación en tiempo real** de formato y consistencia
- **Análisis contextual** de cambios técnicos usando capacidades de comprensión de código
