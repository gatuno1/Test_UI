# **Análisis Comparativo de Asistentes de Codificación CLI: Claude, Gemini y GitHub Copilot para Entornos de Desarrollo en Windows**

## **1\. Introducción Ejecutiva**

### **1.1. Contexto del Informe y Objetivo del Análisis**

El panorama del desarrollo de software está experimentando una transformación acelerada impulsada por la inteligencia artificial. Los asistentes de codificación han evolucionado desde simples herramientas de autocompletado hasta agentes de IA con capacidades holísticas capaces de interactuar con el entorno de desarrollo, el sistema de archivos y los flujos de trabajo de control de versiones. Para los equipos de ingeniería que operan en la plataforma Windows, la elección de la herramienta adecuada es una decisión estratégica que afecta la productividad, la seguridad y la integración con la infraestructura existente.
Este informe tiene como objetivo principal realizar un análisis exhaustivo y riguroso de las capacidades de los asistentes de codificación basados en línea de comandos (CLI): Claude CLI de Anthropic, Gemini CLI de Google y GitHub Copilot CLI de GitHub. La evaluación se centra específicamente en su idoneidad y desempeño en un entorno de desarrollo típico de Windows, asumiendo su integración con Visual Studio Code. A través de este análisis, se busca proporcionar una evaluación objetiva y basada en datos para que los líderes técnicos, los gerentes de proyecto y los equipos de desarrollo puedan tomar decisiones informadas sobre la adopción de estas tecnologías.

### **1.2. Metodología de Investigación y Fuentes**

La metodología de investigación se basa en un enfoque de diligencia técnica que combina la información de la documentación oficial con datos complementarios de fuentes de la comunidad. Las fuentes primarias incluyen documentación técnica y sitios web oficiales de cada proveedor.1 Para obtener una perspectiva más amplia sobre la experiencia de usuario y las configuraciones del mundo real, se consultaron reseñas, foros de discusión (como Reddit) y tutoriales en video de YouTube.14 La combinación de estas fuentes permite una comprensión matizada tanto de las capacidades declaradas como de la aplicación práctica de cada herramienta en un entorno de desarrollo.

### **1.3. Resumen de Hallazgos Clave**

El análisis comparativo revela que cada asistente adopta un paradigma de diseño fundamentalmente diferente. GitHub Copilot CLI se posiciona como una extensión fluida del ecosistema GitHub, centrada en la sinergia y la simplicidad. Gemini CLI se presenta como un agente unificado y guiado que opera con un bucle ReAct, ofreciendo una experiencia segura y controlada para tareas complejas. Claude CLI, por otro lado, se distingue por su enfoque composable y de bajo nivel, permitiendo a los usuarios avanzados orquestar flujos de trabajo personalizados a través de la creación de sub-agentes y una gestión granular del contexto.
Un hallazgo crítico para los equipos de Windows es la dependencia de Claude CLI del Subsistema de Windows para Linux (WSL), lo que introduce una capa de fricción de instalación y un flujo de trabajo menos nativo en comparación con las integraciones más directas y simplificadas de GitHub Copilot y Gemini. La forma en que cada herramienta maneja el contexto y la seguridad de los archivos locales también varía significativamente, con Claude y Gemini adoptando un enfoque de "contexto como código" y Gemini destacando con el soporte de sandboxing. La elección entre ellos, en última instancia, dependerá de la estrategia de flujo de trabajo del equipo: la flexibilidad y control de Claude, la simplicidad y seguridad guiada de Gemini, o la integración sin fisuras de Copilot con la plataforma de GitHub.

## **2\. Visión General de Cada Asistente: Paradigmas de Diseño**

### **2.1. GitHub Copilot CLI: El Facilitador del Ecosistema**

La oferta de GitHub Copilot en la línea de comandos no se presenta como una herramienta CLI autónoma, sino como una extensión del gh cli, la interfaz de línea de comandos oficial de GitHub.5 Esta arquitectura lo posiciona como un habilitador del ecosistema en lugar de un agente de código de propósito general. Su función principal es proporcionar una interfaz de chat para ofrecer sugerencias, explicaciones y ejecutar comandos en la terminal de manera más eficiente.6 Las capacidades agenticas más profundas, como la auto-revisión de errores y la creación autónoma de
Pull Requests (PRs), se encuentran dentro de las características del modo agent del ecosistema de Copilot, que se gestionan a través de la plataforma GitHub y sus extensiones de IDE.26
La configuración en el entorno de Windows es notablemente sencilla. La integración con Visual Studio Code es directa, requiriendo únicamente la instalación de una extensión desde el Visual Studio Marketplace.34 Para la experiencia en la línea de comandos, se integra de forma experimental con
Windows Terminal Canary, permitiendo a los usuarios chatear con Copilot y obtener sugerencias de comandos directamente en el terminal.6 Este enfoque minimalista y simplificado es un diferenciador clave que reduce la barrera de entrada para los usuarios que ya están familiarizados con el ecosistema de GitHub. El valor principal de esta herramienta reside en su capacidad para actuar como un asistente que ya "conoce" el repositorio, los
issues, los PRs y el contexto del proyecto, lo que lo convierte en una extensión natural y poderosa de la experiencia de desarrollo en GitHub.9

### **2.2. Gemini CLI: El Agente Monolítico y Guiado**

Gemini CLI se describe como un "agente de IA de código abierto" que ofrece acceso directo a los modelos de Gemini en la terminal.3 Su arquitectura se basa en un bucle
reason and act (ReAct) que le permite planificar y ejecutar tareas complejas, como la corrección de errores, la creación de nuevas funcionalidades o la mejora de la cobertura de pruebas.3 Funciona con un conjunto de herramientas integradas para interactuar con el sistema local (ej.
grep, terminal, lectura/escritura de archivos) y se puede extender a través de servidores externos del Model Context Protocol (MCP).3
En cuanto a su configuración, Gemini CLI ofrece una integración profunda con Visual Studio Code a través de la extensión Gemini Code Assist.16 Un subconjunto de sus funcionalidades CLI está disponible directamente en el chat del IDE, y se pueden configurar herramientas y permisos a través del archivo de configuración
settings.json.3 Su filosofía de diseño se centra en un modo de
agent que toma el control de tareas complejas pero mantiene al desarrollador en el bucle de supervisión. Antes de modificar cualquier código, el agente presenta un plan detallado de los cambios propuestos y espera la aprobación final del usuario, garantizando que el usuario "siempre tiene el control".30 Este enfoque lo hace muy accesible para equipos que desean delegar tareas sin perder la supervisión.

### **2.3. Claude CLI: El Agente Composable y Filosófico**

Claude CLI se describe como una "herramienta de codificación agentica" con una filosofía de diseño "unopinionated" (sin opiniones predefinidas) y de "bajo nivel" que sigue los principios del diseño Unix.2 Esta aproximación lo convierte en una
power tool flexible y personalizable. Su poder no reside en un solo agente monolítico, sino en la capacidad de componer flujos de trabajo complejos con la creación de "sub-agentes" especializados, cada uno con su propio system prompt, permisos de herramientas y contexto de conversación independiente.27
La configuración en un entorno Windows presenta un punto de fricción crítico, ya que Claude CLI no se ejecuta de forma nativa. Su instalación requiere la utilización del Subsistema de Windows para Linux (WSL), Node.js y otras dependencias dentro de ese entorno virtualizado.15 La integración con Visual Studio Code se realiza de forma menos fluida, lanzando la aplicación desde el terminal de WSL (
code.). Este flujo de trabajo, aunque funcional, es menos nativo que el de sus competidores. Sin embargo, su filosofía de diseño compensa esta complejidad, permitiendo a los usuarios avanzados orquestar flujos de trabajo complejos con múltiples instancias, incluso ejecutándolas en paralelo en diferentes git worktrees.10 Esto lo posiciona como una herramienta preferida para desarrolladores que buscan un control granular y la capacidad de construir sus propios
pipelines de IA a medida.

## **3\. Análisis Comparativo por Categoría Técnica**

### **3.1. Comandos, Interfaz y Flujo de Trabajo**

Cada asistente presenta una aproximación distinta a la interacción a través de la terminal. **Gemini CLI** ofrece una interfaz de Read-Eval-Print Loop (REPL) interactiva con un conjunto claro de comandos slash predefinidos. Estos comandos, como /memory, /stats, /tools y /mcp, permiten al usuario gestionar directamente la sesión, el contexto y la configuración.3 De manera similar,
**Claude CLI** también utiliza una interfaz REPL, con comandos slash para funcionalidades como la gestión de permisos (/permissions), sub-agentes (/agents) o la visualización de costos (/cost).13 Adicionalmente, Claude se adhiere a la filosofía Unix permitiendo el procesamiento de contenido canalizado (piping), lo que significa que la salida de un programa puede ser la entrada de Claude (ej.
cat logs.txt | claude \-p "explain"), una capacidad poderosa para la automatización.13
**GitHub Copilot CLI**, en contraste, no opera con un REPL persistente en el mismo sentido. Su interfaz principal en el terminal se basa en comandos de delegación como gh copilot suggest y gh copilot explain.8 El usuario no mantiene una conversación de chat a largo plazo directamente en la terminal; en cambio, solicita una sugerencia o explicación y luego decide si ejecutar el comando propuesto. Los comandos
slash de Copilot, como /tests o /fix, están principalmente disponibles en la interfaz de chat de Visual Studio Code y no en la experiencia de la CLI.8
Una diferencia notable es la capacidad de crear comandos personalizados. **Claude CLI** lo permite explícitamente a través de archivos Markdown con YAML frontmatter ubicados en el directorio .claude/commands/. Esto permite a los equipos definir comandos slash personalizados a nivel de proyecto para automatizar flujos de trabajo específicos (ej. /commit para preparar y enviar commits de Git).20
**Gemini CLI** ofrece una funcionalidad similar, pero utiliza archivos TOML en directorios designados para comandos personalizados, lo que también permite la modularidad y la compartición dentro de un equipo.7
**GitHub Copilot CLI** no tiene una capacidad documentada para que los usuarios creen comandos personalizados en la CLI, más allá de la configuración de alias para comandos existentes.8 La personalización en Copilot se centra más en la adición de
custom instructions en el chat del IDE.9

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Comandos Integrados Principales** | REPL interactivo con comandos /permissions, /agents, /cost, etc..18 | REPL interactivo con comandos /memory, /stats, /tools, /mcp, etc..3 | Comandos de delegación gh copilot suggest, gh copilot explain.8 |
| **Soporte para Comandos Slash** | Sí. Definidos en .claude/commands/ a nivel de proyecto/global.20 | Sí. Definidos en .gemini/commands/ a nivel de proyecto/global.7 | Sí. Principalmente en la interfaz de chat de VS Code (/tests, /fix).8 |
| **Creación de Comandos Personalizados** | Sí. Mediante archivos Markdown con YAML en .claude/commands/.20 | Sí. Mediante archivos .toml en .gemini/commands/.7 | No documentado para la CLI. La personalización se realiza a través de custom instructions.8 |
| **Soporte para Piping (E/S)** | Sí. Permite tail \-f app.log \| claude \-p "explain".13 | Sí. Permite echo "Count to 10" \| gemini.7 | No documentado para la CLI.8 |
| **Integración con Terminal de Windows** | A través de WSL.15 | Nativamente a través de Gemini Code Assist.17 | A través de la extensión gh-copilot y Windows Terminal Canary.6 |

### **3.2. Gestión del Contexto y la Memoria del Proyecto**

La capacidad de un asistente de IA para retener y utilizar el contexto de un proyecto a lo largo de múltiples sesiones es fundamental. **Claude CLI** y **Gemini CLI** abordan esto de manera similar, empleando un modelo de "contexto como código" (Context-as-Code) a través de archivos Markdown versionables. **Claude** utiliza un archivo CLAUDE.md, que funciona como la "memoria del proyecto", almacenando convenciones, decisiones y conocimientos que persisten entre las sesiones.18 De manera similar,
**Gemini** emplea un archivo GEMINI.md con la misma función, permitiendo a los usuarios definir reglas, guías de estilo o un persona específico para el agente.7
La similitud entre ambos sistemas se extiende al manejo jerárquico de la configuración. Tanto Claude como Gemini buscan archivos de contexto desde el directorio de trabajo actual hasta el directorio raíz del proyecto y en los subdirectorios.18 Este enfoque jerárquico permite una poderosa superposición de instrucciones, donde las reglas definidas en un archivo más específico (ej. en el directorio de un módulo) anulan o complementan las reglas más generales (ej. a nivel de proyecto o global, como
\~/.gemini/GEMINI.md).18 Esta capacidad de definir contexto en diferentes niveles de especificidad es un mecanismo poderoso para escalar el uso de la IA en bases de código complejas y para mantener la consistencia entre diferentes partes de un proyecto.
Este enfoque arquitectónico, donde el contexto se trata como un activo de software persistente y versionado, es un diferenciador clave. En lugar de ser una memoria efímera, el contexto se convierte en parte de la infraestructura del proyecto, permitiendo a los equipos de ingeniería estandarizar y escalar el uso de la IA. Un nuevo desarrollador puede clonar el repositorio y, sin ninguna configuración adicional, el asistente de IA sabrá qué reglas de estilo seguir, qué herramientas están permitidas y qué convenciones de nomenclatura se deben utilizar. Esto no solo mejora la coherencia del código, sino que también acelera significativamente el proceso de incorporación de nuevos miembros del equipo (onboarding).
**GitHub Copilot**, por el contrario, no se basa en un archivo de memoria persistente y versionado en el repositorio. En su lugar, el contexto se basa en la indexación del repositorio, chat variables (\#file, \#project) que permiten al usuario incluir información específica en sus prompts, y custom instructions que se pueden configurar a nivel de usuario, repositorio u organización.8 Este modelo, aunque efectivo, no permite el mismo nivel de control granular y versionado del contexto que los archivos
CLAUDE.md o GEMINI.md.

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Formato de Archivo de Memoria** | Archivos Markdown (CLAUDE.md).18 | Archivos Markdown (GEMINI.md).7 | No usa un archivo de memoria persistente en el repositorio.8 |
| **Manejo Jerárquico** | Sí. Los archivos más específicos anulan los más generales.18 | Sí. El contexto se combina de forma jerárquica.22 | Contexto basado en la indexación del repositorio y chat variables.8 |
| **Comandos de Gestión de Contexto** | /init para crear CLAUDE.md, /clear, /history, etc..10 | /memory show, /memory refresh, /compress, /chat save.3 | /clear, /new en la interfaz de chat.8 |
| **Recomendación de Control de Versiones** | Sí. CLAUDE.md debe ser commited y revisado.18 | Sí. GEMINI.md debe ser commited.22 | El contexto se gestiona a través de la plataforma de GitHub.9 |

### **3.3. Extensibilidad y Acceso a Sistemas Locales**

La extensibilidad y la capacidad de interactuar con el entorno local son componentes críticos de un asistente de codificación CLI. El Model Context Protocol (MCP) es un pilar arquitectónico para **Claude CLI** y **Gemini CLI**, que les permite conectarse a herramientas y datos externos, como bases de datos, APIs y sistemas de seguimiento de issues.1 Claude Context, un
plugin de MCP, permite la búsqueda de código semántico en bases de código masivas, lo que ilustra la apertura y el potencial de su ecosistema.23
**GitHub Copilot** también menciona "Copilot Extensions" y "MCP skills," aunque su modelo de extensión está más profundamente arraigado en la plataforma de GitHub a través de las GitHub Apps, que integran el poder de herramientas externas en Copilot Chat.8
Todos los asistentes tienen acceso y capacidad para interactuar con programas locales y el sistema de archivos. **Claude CLI** y **Gemini CLI** pueden realizar acciones como leer, escribir, ejecutar comandos del terminal (bash) o usar herramientas como grep.3 La forma en que gestionan la seguridad en torno a este acceso es un punto de diferenciación importante. Claude y Gemini operan con un modelo de "consentimiento explícito", que requiere que el usuario apruebe las acciones potencialmente destructivas antes de su ejecución.10 Además, ambos permiten la creación de listas blancas (
allow-listing) de comandos que pueden ejecutarse sin aprobación.20
**Gemini CLI** va un paso más allá al ofrecer soporte explícito para sandboxing con contenedores Docker para aislar las operaciones, lo que es una característica crucial para la seguridad en entornos empresariales.7 El
sandboxing de **GitHub Copilot** es diferente; su modo agent opera en un "sandbox seguro en la nube" para cada tarea que se le asigna.26
La manera en que cada herramienta gestiona el acceso a recursos locales tiene implicaciones directas para la seguridad y la adopción empresarial. La arquitectura de Gemini y Claude, que ofrece un control granular y la opción de sandboxing local, puede ser preferida por organizaciones con políticas de seguridad estrictas que requieren visibilidad y control sobre la transmisión de datos. Por otro lado, las organizaciones que confían en el "enterprise-grade security" de GitHub y Google podrían encontrar la simplicidad de **Copilot** y **Gemini** más atractiva, ya que externalizan gran parte de la gestión de la seguridad al proveedor de la plataforma.11

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Soporte MCP** | Sí. Es un pilar arquitectónico. Se pueden configurar servidores stdio, sse, y http.13 | Sí. Es un pilar arquitectónico. Soporta servidores local o remotos.3 | Sí. A través de Copilot Extensions y MCP skills, que se integran con GitHub Apps.8 |
| **Acceso a Shell/Archivos** | Sí. Puede leer, escribir, editar archivos y ejecutar comandos bash.2 | Sí. Posee herramientas integradas para grep, file read, file write y terminal.3 | Sí. El modo agent puede sugerir y ejecutar comandos de terminal.26 |
| **Modelo de Permisos/Seguridad** | Modelo de "consentimiento explícito" y whitelisting de comandos con /permissions.10 | Modelo de "consentimiento explícito" con aprobación de planes. Admite allowlisting de comandos.25 | Coding agent que opera en un cloud sandbox seguro y auto-gestionado.26 |
| **Soporte de Sandboxing** | No documentado explícitamente en el material. | Sí. Soporte para sandboxing con contenedores Docker para aislar operaciones.7 | Sí. El modo agent opera en un cloud sandbox seguro para cada tarea.26 |

### **3.4. Capacidades Agenticas y Generación de Sub-Agentes**

Las arquitecturas agenticas de cada herramienta no son solo una característica, sino un reflejo de su filosofía de diseño. **Claude CLI** sigue un modelo de "agentes composables" que permite a los usuarios crear equipos de especialistas de IA. El ciclo de trabajo Plan → Act → Review es altamente explícito.10 Los usuarios pueden influir directamente en el presupuesto de pensamiento del modelo utilizando comandos como
think hard o ultrathink para una planificación más profunda.10 La capacidad única de Claude es la creación explícita de "sub-agentes", que son mini-agentes con su propio
system prompt y un conjunto específico de herramientas y permisos.27 Un desarrollador puede definir sub-agentes para la revisión de código, la ejecución de pruebas o el diagnóstico de errores, y el agente principal puede delegar tareas a estos especialistas, reduciendo la "polución de contexto" y mejorando la fiabilidad de las respuestas.27
**Gemini CLI** adopta un modelo de "agente monolítico guiado". Su modo agent en Visual Studio Code, impulsado por el bucle ReAct, puede analizar toda la base de código y orquestar cambios multi-archivo a gran escala a partir de un único prompt.30 Su poder reside en la capacidad de tomar una tarea compleja y, después de la aprobación del usuario, coordinar todos los cambios necesarios en el código base. Aunque puede usar
core tools para tareas especializadas, la capacidad de crear "sub-agentes" definidos por el usuario no está documentada; sus capacidades agenticas se manifiestan en una única entidad de agente que puede ser controlada a través de la interfaz de chat.29
**GitHub Copilot**, por su parte, opera con un modelo de "agente integrado en el ecosistema". Su coding agent es una herramienta autónoma que se integra directamente con la plataforma de GitHub. El usuario puede asignar un issue a Copilot y el agente trabajará para realizar los cambios necesarios y crear un Pull Request para su revisión.26 El
agent de Copilot es capaz de inferir tareas adicionales necesarias, auto-corregir errores y analizar errores de tiempo de ejecución con "capacidades de auto-sanación".26 Sin embargo, la capacidad de crear sub-agentes personalizados no está documentada; su delegación de tareas se produce a través de la plataforma GitHub y un
cloud sandbox.26
La elección entre estos paradigmas es una decisión de estrategia de workflow. Un equipo que valora la flexibilidad, el control granular y la capacidad de construir flujos de trabajo de IA personalizados podría preferir Claude. Un equipo que busca la simplicidad y un flujo de trabajo de "dar una tarea y ver el plan" podría optar por Gemini, que ofrece una experiencia de bajo riesgo. Los equipos que ya están profundamente integrados en GitHub encontrarán en Copilot una extensión natural de su metodología de desarrollo, ya que su valor reside en su fluidez con el workflow de GitHub.

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Estrategia Agentica Principal** | Agentes composables y de bajo nivel (filosofía Unix).10 | Agente monolítico guiado con bucle ReAct.3 | Agente integrado en el ecosistema de GitHub.26 |
| **Soporte para Sub-Agentes** | Sí. Es una característica principal. Los usuarios pueden crear mini-agentes con sus propios permisos y contexto.27 | No documentado. El modo agent opera como una única entidad.29 | No documentado. La delegación de tareas se gestiona a través de issues y PRs en GitHub.26 |
| **Modo de Planificación** | Sí. Modo explícito Plan, con comandos think, think hard, ultrathink para presupuesto de pensamiento.10 | Sí. El modo agent propone un plan detallado antes de ejecutar los cambios.30 | Sí. Puede generar un plan para el refactoring o la implementación de una característica.32 |
| **Manejo de Tareas Multi-paso** | Orquestación de flujos de trabajo complejos con sub-agentes y hooks.18 | El modo agent puede analizar y ejecutar tareas multi-archivo a gran escala desde un solo prompt.30 | El coding agent es capaz de inferir y completar sub-tareas para un prompt primario.26 |
| **Integración con Git** | Puede crear ramas, commits y PRs directamente. Soporte para git worktrees.13 | Integración con GitHub Actions para triage de issues y PR reviews.21 | Se integra fluidamente con issues, pull requests, y code review en la plataforma.9 |

## **4\. Evaluación de Rendimiento en Casos de Uso del Ciclo de Vida del Software**

### **4.1. Análisis de Requerimientos y Planificación**

En la fase de análisis de requerimientos, la capacidad de planificar y entender la base de código es crucial. **Claude CLI** se destaca con su modo Plan Mode y el uso de comandos como think hard o ultrathink, que asignan un "presupuesto de pensamiento" adicional para un análisis más profundo de problemas complejos. Claude puede generar planes de acción, listas de tareas y documentos de arquitectura completos, y puede ser instruido para trabajar en secciones específicas de un Product Requirements Document (PRD).10
**Gemini CLI** también es adecuado para esta tarea. Su modo agent puede analizar la base de código completa para modelar la arquitectura y las dependencias, y luego proponer un plan detallado para la implementación de una característica o un cambio a gran escala.30 De manera similar,
**GitHub Copilot** se utiliza para la exploración de bases de código existentes y el análisis de funcionalidad a través de prompts de chat, lo que permite a los desarrolladores comprender rápidamente el propósito de un archivo o función.6

### **4.2. Generación de Código y Pruebas Unitarias**

Para la generación de código, **GitHub Copilot** se destaca por sus sugerencias de autocompletado y su enfoque granular. Ofrece comandos slash en la interfaz de chat como /tests para generar pruebas unitarias para el código seleccionado.8 Los usuarios pueden especificar el marco de pruebas preferido o solicitar casos de borde para obtener mejores resultados.
**Gemini CLI** es capaz de generar funciones completas o bloques de código a partir de comentarios o prompts de chat.11 Su modo
agent puede orquestar la generación de código y pruebas a través de múltiples archivos. Por su parte, **Claude CLI** puede ser utilizado para la generación de código y pruebas, pero su verdadera fortaleza reside en el uso de sub-agentes especializados, como un test-runner, que puede ser instruido para generar pruebas y luego verificarlas, corrigiendo los errores si es necesario.27

### **4.3. Revisión de Estándares y Buenas Prácticas**

Mantener los estándares de código es una tarea continua. **Gemini CLI** en su edición Enterprise puede ser personalizado con repositorios de código fuente privados para alinear sus respuestas con las mejores prácticas de la organización.11 Además, su capacidad para citar fuentes de documentación y código es una ventaja para la validación y el cumplimiento.36
**Claude CLI** permite la definición de reglas de estilo y buenas prácticas en los archivos CLAUDE.md, asegurando que el agente se adhiera a las convenciones del proyecto. Adicionalmente, se pueden crear sub-agentes de code review que están configurados con permisos de solo lectura para buscar y sugerir mejoras en el código.20
**GitHub Copilot** complementa el flujo de trabajo de revisión con sugerencias de revisión de código generadas por IA en Pull Requests y la capacidad de corregir errores de linting.6

### **4.4. Depuración y Solución de Problemas**

La depuración es una de las tareas más complejas en el desarrollo de software. **Claude CLI** puede analizar una base de código y proponer una solución a un problema después de que el usuario describa un error o pegue un mensaje de error.13
**Gemini CLI** utiliza su bucle ReAct para el diagnóstico de problemas, y su característica de checkpointing permite a los usuarios guardar un estado del proyecto (/chat save) y revertir a él (/restore) para deshacer cambios destructivos.7
**GitHub Copilot**, con su modo agent, puede analizar errores de tiempo de ejecución con capacidades de "auto-sanación" (self-healing), lo que le permite corregir sus propios errores y proponer soluciones directamente en el chat.26 La herramienta también ofrece un
Debug assistant en el ecosistema de Visual Studio que ayuda a los desarrolladores a entender y resolver problemas de código.35

### **4.5. Refactorización de Código**

La refactorización de código es una tarea en la que los asistentes de IA pueden aportar un valor significativo. **GitHub Copilot** se destaca por su enfoque directo y granular, con comandos slash como /optimize para mejorar la eficiencia o /simplify para hacer el código más conciso.8 La funcionalidad de
Copilot Edits en Visual Studio Code, una interfaz específica para la refactorización conversacional, permite a los desarrolladores realizar cambios a través de múltiples archivos de manera rápida y con una interfaz de usuario optimizada.26
**Gemini CLI** también es muy capaz en este ámbito. Su modo agent puede realizar refactorings a gran escala o actualizaciones de dependencias con un solo prompt.30
**Claude CLI**, aunque no tiene un comando específico de refactorización, es muy adecuado para la tarea debido a su modo Plan Mode y su capacidad para orquestar flujos de trabajo con git worktrees, lo que permite al desarrollador ejecutar refactorizaciones complejas a largo plazo en ramas de Git aisladas sin interferir con el resto del proyecto.10

### **4.6. Análisis de Commits y Pull Requests**

La integración con los flujos de trabajo de Git es una ventaja importante. **GitHub Copilot** es el más fuerte en este aspecto debido a su profunda integración con la plataforma de GitHub. Puede generar resúmenes de Pull Requests (AI-generated summaries) y puede ser asignado a un issue para que, de forma autónoma, cree un Pull Request con los cambios necesarios.9
**Gemini CLI** se integra con GitHub Actions, lo que le permite automatizar el triage de issues y realizar revisiones de Pull Requests generadas por IA.21 Por último,
**Claude CLI** puede interactuar directamente con Git. La herramienta puede crear ramas, realizar commits y generar Pull Requests con comandos naturales, y la comunidad ha desarrollado comandos personalizados como /commit para automatizar la preparación y el envío de commits.13

## **5\. Conclusiones y Recomendaciones**

### **5.1. Resumen de Puntos Fuertes y Débiles de Cada Asistente**

El análisis exhaustivo de Claude CLI, Gemini CLI y GitHub Copilot CLI revela que, si bien todos son asistentes de codificación poderosos, cada uno sobresale en áreas distintas y presenta un conjunto único de fortalezas y debilidades.

* **GitHub Copilot CLI** destaca por su **simplicidad y sinergia con la plataforma GitHub**. Su instalación es la más sencilla en Windows y su valor principal reside en la fluidez con los flujos de trabajo existentes de issues, pull requests y code review. Su debilidad principal es la falta de una interfaz de conversación persistente en la CLI y una menor capacidad de personalización de comandos en comparación con sus competidores.
* **Gemini CLI** sobresale por su **experiencia de agente monolítico guiado y sus robustas características de seguridad**. Su modo agent en Visual Studio Code es muy potente para tareas multi-archivo, y su modelo de aprobación de planes y la opción de sandboxing local lo convierten en una opción de bajo riesgo para la adopción en equipos. La principal desventaja es su falta de un modelo de sub-agentes composables, lo que lo hace menos flexible para flujos de trabajo personalizados y de nicho.
* **Claude CLI** se distingue por su **filosofía composable, su control granular y sus capacidades agenticas avanzadas**. Es la única herramienta que permite la creación de sub-agentes especializados, lo que abre la puerta a flujos de trabajo altamente personalizados y modulares. Su principal punto de fricción es su **dependencia crítica de WSL para funcionar en Windows**, lo que complica la instalación y crea una experiencia de usuario menos nativa y fluida.

### **5.2. Recomendaciones Basadas en Escenarios de Uso**

Con base en los hallazgos de esta investigación, se proponen las siguientes recomendaciones para los equipos de desarrollo:

* **Para equipos que valoran el control y la personalización a medida:** Se recomienda **Claude CLI**. Su arquitectura de sub-agentes y el modelo de "contexto como código" lo convierten en una plataforma poderosa para ingenieros que buscan construir flujos de trabajo de IA a medida. Es la herramienta ideal para aquellos que desean un control granular sobre las capacidades de la IA, el acceso a las herramientas y la seguridad.
* **Para la adopción masiva y equipos que buscan una experiencia guiada y segura:** Se recomienda **Gemini CLI**. Su integración nativa en Windows/VS Code, su modo agent que requiere aprobación de planes y su sandboxing ofrecen una experiencia accesible y de bajo riesgo, lo que lo hace ideal para equipos que delegan tareas y desean supervisar el trabajo del agente sin preocuparse por la seguridad de la ejecución.
* **Para equipos profundamente integrados en el ecosistema de GitHub:** Se recomienda **GitHub Copilot CLI**. Su valor reside en su fluidez con el workflow de GitHub (issues, PRs, code review), lo que lo hace una extensión natural del toolchain existente. Para un equipo que ya ha invertido en la plataforma de GitHub, la curva de aprendizaje es mínima y el retorno de la inversión es inmediato.

### **5.3. Consideraciones Finales para el Desarrollo en Windows**

La elección de un asistente de codificación CLI para un entorno Windows no se limita a las capacidades funcionales del agente, sino que también debe considerar la experiencia de usuario y la fricción de la plataforma. La dependencia de Claude CLI de WSL para su ejecución en Windows es un factor decisivo. Si bien la comunidad ha creado workarounds y guías detalladas, esta capa de abstracción contrasta con la integración más directa y nativa de Gemini y Copilot. Para las organizaciones que buscan una experiencia de usuario sin fisuras, la simplicidad de la instalación y la integración nativa de sus competidores pueden ser un factor de peso en la decisión de adopción.

## **6\. Anexos: Tablas Comparativas y Fuentes de Investigación**

### **6.1. Tabla 1: Comandos y Funcionalidades Clave**

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Comandos Integrados Principales** | REPL interactivo con comandos /permissions, /agents, /cost, etc..18 | REPL interactivo con comandos /memory, /stats, /tools, /mcp, etc..3 | Comandos de delegación gh copilot suggest, gh copilot explain.8 |
| **Soporte para Comandos Slash**  | Sí. Definidos en .claude/commands/ a nivel de proyecto/global.20 | Sí. Definidos en .gemini/commands/ a nivel de proyecto/global.7 | Sí. Principalmente en la interfaz de chat de VS Code (/tests, /fix).8 |
| **Creación de Comandos Personalizados** | Sí. Mediante archivos Markdown con YAML en .claude/commands/.20 | Sí. Mediante archivos .toml en .gemini/commands/.7 | No documentado para la CLI. La personalización se realiza a través de custom instructions.8 |
| **Soporte para Piping (E/S)** | Sí. Permite tail \-f app.log \| claude \-p "explain".13 | Sí. Permite echo "Count to 10" \| gemini.7 | No documentado para la CLI.8 |
| **Integración con Terminal de Windows** | A través de WSL.15  | Nativamente a través de Gemini Code Assist.17  | A través de la extensión gh-copilot y Windows Terminal Canary.6 |

### **6.2. Tabla 2: Gestión de Contexto**

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Formato de Archivo de Memoria** | Archivos Markdown (CLAUDE.md).18 | Archivos Markdown (GEMINI.md).7 | No usa un archivo de memoria persistente en el repositorio.8 |
| **Manejo Jerárquico** | Sí. Los archivos más específicos anulan los más generales.18 | Sí. El contexto se combina de forma jerárquica.22 | Contexto basado en la indexación del repositorio y chat variables.8 |
| **Comandos de Gestión de Contexto** | /init para crear CLAUDE.md, /clear, /history, etc..10 | /memory show, /memory refresh, /compress, /chat save.3 | /clear, /new en la interfaz de chat.8 |
| **Recomendación de Control de Versiones** | Sí. CLAUDE.md debe ser commited y revisado.18 | Sí. GEMINI.md debe ser commited.22 | El contexto se gestiona a través de la plataforma de GitHub.9 |

### **6.3. Tabla 3: Extensibilidad (MCP y Herramientas Locales)**

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Soporte MCP** | Sí. Es un pilar arquitectónico. Se pueden configurar servidores stdio, sse, y http.13 | Sí. Es un pilar arquitectónico. Soporta servidores local o remotos.3 | Sí. A través de Copilot Extensions y MCP skills, que se integran con GitHub Apps.8 |
| **Acceso a Shell/Archivos** | Sí. Puede leer, escribir, editar archivos y ejecutar comandos bash.2 | Sí. Posee herramientas integradas para grep, file read, file write y terminal.3 | Sí. El modo agent puede sugerir y ejecutar comandos de terminal.26 |
| **Modelo de Permisos/Seguridad** | Modelo de "consentimiento explícito" y whitelisting de comandos con /permissions.10 | Modelo de "consentimiento explícito" con aprobación de planes. Admite allowlisting de comandos.25 | Coding agent que opera en un cloud sandbox seguro y auto-gestionado.26 |
| **Soporte de Sandboxing** | No documentado explícitamente en el material. | Sí. Soporte para sandboxing con contenedores Docker para aislar operaciones.7 | Sí. El modo agent opera en un cloud sandbox seguro para cada tarea.26 |

### **6.4. Tabla 4: Capacidades Agenticas**

| Característica | Claude CLI | Gemini CLI | GitHub Copilot CLI |
| :------------- | :--------- | :--------- | :----------------- |
| **Estrategia Agentica Principal** | Agentes composables y de bajo nivel (filosofía Unix).10 | Agente monolítico guiado con bucle ReAct.3 | Agente integrado en el ecosistema de GitHub.26 |
| **Soporte para Sub-Agentes** | Sí. Es una característica principal. Los usuarios pueden crear mini-agentes con sus propios permisos y contexto.27 | No documentado. El modo agent opera como una única entidad.29 | No documentado. La delegación de tareas se gestiona a través de issues y PRs en GitHub.26 |
| **Modo de Planificación** | Sí. Modo explícito Plan, con comandos think, think hard, ultrathink para presupuesto de pensamiento.10 | Sí. El modo agent propone un plan detallado antes de ejecutar los cambios.30 | Sí. Puede generar un plan para el refactoring o la implementación de una característica.32 |
| **Manejo de Tareas Multi-paso** | Orquestación de flujos de trabajo complejos con sub-agentes y hooks.18 | El modo agent puede analizar y ejecutar tareas multi-archivo a gran escala desde un solo prompt.30 | El coding agent es capaz de inferir y completar sub-tareas para un prompt primario.26 |
| **Integración con Git** | Puede crear ramas, commits y PRs directamente. Soporte para git worktrees.13 | Integración con GitHub Actions para triage de issues y PR reviews.21 | Se integra fluidamente con issues, pull requests, y code review en la plataforma.9 |

### **6.5. Fuentes de Investigación Detalladas**

* \[1\]: [https://claude.ai/](https://claude.ai/)
* \[2\]: [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
* 3: [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
* \[4\]: [https://gemini-cli.xyz/docs/en/](https://gemini-cli.xyz/docs/en/)
* 5: [https://github.com/cli/cli](https://github.com/cli/cli)
* 6: [https://docs.github.com/copilot/quickstart](https://docs.github.com/copilot/quickstart)
* \[14\]: [https://apidog.com/blog/claude-code-ide-integrations/](https://apidog.com/blog/claude-code-ide-integrations/)
* 15: [https://itecsonline.com/post/how-to-install-claude-code-on-windows](https://itecsonline.com/post/how-to-install-claude-code-on-windows)
* \[16\]: [https://www.youtube.com/watch?v=NkB3tAVZWsU](https://www.youtube.com/watch?v=NkB3tAVZWsU)
* 17: [https://www.youtube.com/watch?v=ISrsYOkQ9WQ](https://www.youtube.com/watch?v=ISrsYOkQ9WQ)
* 34: [https://www.geeksforgeeks.org/installation-guide/how-to-install-github-copilot-on-vscode/](https://www.geeksforgeeks.org/installation-guide/how-to-install-github-copilot-on-vscode/)
* 18: [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
* \[19\]: [https://www.reddit.com/r/ClaudeAI/comments/1m2e7l6/claudecmd\_a\_cli\_for\_managing\_claude\_code\_commands/](https://www.reddit.com/r/ClaudeAI/comments/1m2e7l6/claudecmd_a_cli_for_managing_claude_code_commands/)
* 3: [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
* 7: [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)
* 8: [https://docs.github.com/en/copilot/reference/cheat-sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
* 9: [https://docs.github.com/en/copilot/get-started/features](https://docs.github.com/en/copilot/get-started/features)
* 20: [https://www.reddit.com/r/ClaudeAI/comments/1mpeefp/my\_claude\_code\_tips\_for\_newer\_users/](https://www.reddit.com/r/ClaudeAI/comments/1mpeefp/my_claude_code_tips_for_newer_users/)
* \[37\]: [https://gist.github.com/agokrani/919b536246dd272a55157c21d46eda14](https://gist.github.com/agokrani/919b536246dd272a55157c21d46eda14)
* 21: [https://blog.google/technology/developers/introducing-gemini-cli-github-actions/](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/)
* 22: [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
* 23: [https://github.com/zilliztech/claude-context](https://github.com/zilliztech/claude-context)
* \[24\]: [https://scottspence.com/posts/configuring-mcp-tools-in-claude-code](https://scottspence.com/posts/configuring-mcp-tools-in-claude-code)
* \[25\]: [https://milvus.io/ai-quick-reference/how-does-gemini-cli-handle-privacy-and-local-files](https://milvus.io/ai-quick-reference/how-does-gemini-cli-handle-privacy-and-local-files)
* 3: [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
* 26: [https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/)
* 35: [https://github.com/features/copilot/plans](https://github.com/features/copilot/plans)
* 27: [https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00](https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00)
* \[28\]: [https://www.youtube.com/watch?v=Pif98jOScYc](https://www.youtube.com/watch?v=Pif98jOScYc)
* 29: [https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
* 30: [https://blog.google/technology/developers/gemini-code-assist-updates-july-2025/](https://blog.google/technology/developers/gemini-code-assist-updates-july-2025/)
* 10: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)
* 18: [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
* 3: [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
* 11: [https://developers.google.com/gemini-code-assist/docs/overview](https://developers.google.com/gemini-code-assist/docs/overview)
* \[12\]: [https://docs.github.com/en/copilot/tutorials/write-tests](https://docs.github.com/en/copilot/tutorials/write-tests)
* \[31\]: [https://code.visualstudio.com/docs/copilot/guides/test-with-copilot](https://code.visualstudio.com/docs/copilot/guides/test-with-copilot)
* 13: [https://docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview)
* 18: [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
* \[38\]: [https://developers.google.com/gemini-code-assist/docs/gemini-cli](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
* 36: [https://cloud.google.com/gemini/docs/codeassist/overview](https://cloud.google.com/gemini/docs/codeassist/overview)
* 32: [https://github.blog/ai-and-ml/github-copilot/how-to-refactor-code-with-github-copilot/](https://github.blog/ai-and-ml/github-copilot/how-to-refactor-code-with-github-copilot/)
* \[33\]: [https://docs.github.com/en/copilot/tutorials/refactor-code](https://docs.github.com/en/copilot/tutorials/refactor-code)
* 36: [https://cloud.google.com/gemini/docs/codeassist/overview](https://cloud.google.com/gemini/docs/codeassist/overview)
* 18: [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
* 15: [https://itecsonline.com/post/how-to-install-claude-code-on-windows](https://itecsonline.com/post/how-to-install-claude-code-on-windows)
* 7: [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)
* 22: [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
* 29: [https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
* 8: [https://docs.github.com/en/copilot/reference/cheat-sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
* 26: [https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/)
* 9: [https://docs.github.com/en/copilot/get-started/features](https://docs.github.com/en/copilot/get-started/features)
* 27: [https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00](https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00)
* 29: [https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
* 18: [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
* \[31\]: [https://code.visualstudio.com/docs/copilot/guides/test-with-copilot](https://code.visualstudio.com/docs/copilot/guides/test-with-copilot)
* \[33\]: [https://docs.github.com/en/copilot/tutorials/refactor-code](https://docs.github.com/en/copilot/tutorials/refactor-code)
* 13: [https://docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview)
* 36: [https://cloud.google.com/gemini/docs/codeassist/overview](https://cloud.google.com/gemini/docs/codeassist/overview)

#### **Obras citadas**

1. Claude, fecha de acceso: agosto 21, 2025, [https://claude.ai/](https://claude.ai/)
2. Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows \- all through natural language commands. \- GitHub, fecha de acceso: agosto 21, 2025, [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
3. Gemini CLI | Gemini for Google Cloud, fecha de acceso: agosto 21, 2025, [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
4. Welcome to Gemini CLI documentation, fecha de acceso: agosto 21, 2025, [https://gemini-cli.xyz/docs/en/](https://gemini-cli.xyz/docs/en/)
5. cli/cli: GitHub's official command line tool \- GitHub, fecha de acceso: agosto 21, 2025, [https://github.com/cli/cli](https://github.com/cli/cli)
6. Quickstart for GitHub Copilot \- GitHub Docs, fecha de acceso: agosto 21, 2025, [https://docs.github.com/copilot/quickstart](https://docs.github.com/copilot/quickstart)
7. Google Gemini CLI Cheatsheet \- Philschmid, fecha de acceso: agosto 21, 2025, [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)
8. GitHub Copilot Chat cheat sheet \- GitHub Docs, fecha de acceso: agosto 21, 2025, [https://docs.github.com/en/copilot/reference/cheat-sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
9. GitHub Copilot features \- GitHub Docs, fecha de acceso: agosto 21, 2025, [https://docs.github.com/en/copilot/get-started/features](https://docs.github.com/en/copilot/get-started/features)
10. Claude Code: Best practices for agentic coding \- Anthropic, fecha de acceso: agosto 21, 2025, [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)
11. Gemini Code Assist overview \- Google for Developers, fecha de acceso: agosto 21, 2025, [https://developers.google.com/gemini-code-assist/docs/overview](https://developers.google.com/gemini-code-assist/docs/overview)
12. Writing tests with GitHub Copilot, fecha de acceso: agosto 21, 2025, [https://docs.github.com/en/copilot/tutorials/write-tests](https://docs.github.com/en/copilot/tutorials/write-tests)
13. Claude Code overview \- Anthropic, fecha de acceso: agosto 21, 2025, [https://docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview)
14. How to Integrate Claude Code with VSCode and JetBrains? \- Apidog, fecha de acceso: agosto 21, 2025, [https://apidog.com/blog/claude-code-ide-integrations/](https://apidog.com/blog/claude-code-ide-integrations/)
15. How To Install Claude Code on Windows: Complete Guide 2025 ..., fecha de acceso: agosto 21, 2025, [https://itecsonline.com/post/how-to-install-claude-code-on-windows](https://itecsonline.com/post/how-to-install-claude-code-on-windows)
16. How to Install Gemini CLI with VS Code \+ MCP \[Beginner Tutorial\] \- YouTube, fecha de acceso: agosto 21, 2025, [https://www.youtube.com/watch?v=NkB3tAVZWsU](https://www.youtube.com/watch?v=NkB3tAVZWsU)
17. Gemini CLI 2.0 (New Upgrades): This is now BETTER THAN Claude Code\! Integrate w, fecha de acceso: agosto 21, 2025, [https://www.youtube.com/watch?v=ISrsYOkQ9WQ](https://www.youtube.com/watch?v=ISrsYOkQ9WQ)
18. Cooking with Claude Code: The Complete Guide \- Sid Bharath, fecha de acceso: agosto 21, 2025, [https://www.siddharthbharath.com/claude-code-the-complete-guide/](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
19. Claude‑CMD: A CLI for managing Claude Code commands & workflows \- Reddit, fecha de acceso: agosto 21, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1m2e7l6/claudecmd\_a\_cli\_for\_managing\_claude\_code\_commands/](https://www.reddit.com/r/ClaudeAI/comments/1m2e7l6/claudecmd_a_cli_for_managing_claude_code_commands/)
20. My Claude Code tips for newer users : r/ClaudeAI \- Reddit, fecha de acceso: agosto 21, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1mpeefp/my\_claude\_code\_tips\_for\_newer\_users/](https://www.reddit.com/r/ClaudeAI/comments/1mpeefp/my_claude_code_tips_for_newer_users/)
21. Meet your new AI coding teammate: Gemini CLI GitHub Actions \- Google Blog, fecha de acceso: agosto 21, 2025, [https://blog.google/technology/developers/introducing-gemini-cli-github-actions/](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/)
22. Gemini CLI Tutorial Series — Part 9: Understanding Context ..., fecha de acceso: agosto 21, 2025, [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
23. Code search MCP for Claude Code. Make entire codebase the context for any coding agent. \- GitHub, fecha de acceso: agosto 21, 2025, [https://github.com/zilliztech/claude-context](https://github.com/zilliztech/claude-context)
24. Configuring MCP Tools in Claude Code \- The Better Way \- Scott Spence, fecha de acceso: agosto 21, 2025, [https://scottspence.com/posts/configuring-mcp-tools-in-claude-code](https://scottspence.com/posts/configuring-mcp-tools-in-claude-code)
25. How does Gemini CLI handle privacy and local files? \- Milvus, fecha de acceso: agosto 21, 2025, [https://milvus.io/ai-quick-reference/how-does-gemini-cli-handle-privacy-and-local-files](https://milvus.io/ai-quick-reference/how-does-gemini-cli-handle-privacy-and-local-files)
26. GitHub Copilot: The agent awakens \- The GitHub Blog, fecha de acceso: agosto 21, 2025, [https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/)
27. Practical guide to mastering Claude Code's main agent and Sub ..., fecha de acceso: agosto 21, 2025, [https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00](https://medium.com/@jewelhuq/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00)
28. Claude Code Agents: Build AI Teams That ACTUALLY Work \- YouTube, fecha de acceso: agosto 21, 2025, [https://www.youtube.com/watch?v=Pif98jOScYc](https://www.youtube.com/watch?v=Pif98jOScYc)
29. Use agentic chat as a pair programmer | Gemini Code Assist ..., fecha de acceso: agosto 21, 2025, [https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
30. New in Gemini Code Assist: Agent Mode and IDE enhancements \- Google Blog, fecha de acceso: agosto 21, 2025, [https://blog.google/technology/developers/gemini-code-assist-updates-july-2025/](https://blog.google/technology/developers/gemini-code-assist-updates-july-2025/)
31. Test with GitHub Copilot \- Visual Studio Code, fecha de acceso: agosto 21, 2025, [https://code.visualstudio.com/docs/copilot/guides/test-with-copilot](https://code.visualstudio.com/docs/copilot/guides/test-with-copilot)
32. How to refactor code with GitHub Copilot, fecha de acceso: agosto 21, 2025, [https://github.blog/ai-and-ml/github-copilot/how-to-refactor-code-with-github-copilot/](https://github.blog/ai-and-ml/github-copilot/how-to-refactor-code-with-github-copilot/)
33. Refactoring code with GitHub Copilot \- GitHub Docs, fecha de acceso: agosto 21, 2025, [https://docs.github.com/en/copilot/tutorials/refactor-code](https://docs.github.com/en/copilot/tutorials/refactor-code)
34. How to Install GitHub Copilot on VSCode? \- GeeksforGeeks, fecha de acceso: agosto 21, 2025, [https://www.geeksforgeeks.org/installation-guide/how-to-install-github-copilot-on-vscode/](https://www.geeksforgeeks.org/installation-guide/how-to-install-github-copilot-on-vscode/)
35. GitHub Copilot · Your AI pair programmer, fecha de acceso: agosto 21, 2025, [https://github.com/features/copilot/plans](https://github.com/features/copilot/plans)
36. Gemini Code Assist Standard and Enterprise overview | Gemini for ..., fecha de acceso: agosto 21, 2025, [https://cloud.google.com/gemini/docs/codeassist/overview](https://cloud.google.com/gemini/docs/codeassist/overview)
