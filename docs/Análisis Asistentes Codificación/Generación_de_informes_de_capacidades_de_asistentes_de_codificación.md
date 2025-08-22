# Generación de informes de capacidades de asistentes de codificación

## Prompt entregado

Se utilizó el siguiente prompt a ChatGPT (GPT-5 En modo investigación profunda), Google Gemini (Gemini 2.5 flash, en modo deep research) y Claude (Claude Opus 4.1, en modo investigación)

```plainttext
En el contexto de un proyecto de desarrollo de software, quiero poder comprar las capacidades de varios asistentes de codificación:
- Claude CLI
- Gemini CLI
- Github Copilot CLI

Quiero que analices las capacidades de cada uno, asumiendo que todos tienen integración con Visual Studio Code, para que determines qué comandos incorporados tiene cada asistente, si tienen acceso a capacidades  ta adicionales vía MCP, programas locales, definición de acciones de usuario basado en archivos de texto (ej. `*.md`), cómo es el uso de archivos markdown para configurar acciones o instrucciones, que capacidad tienen para generar sub agentes especializados
Para ello presenta un plan de investigación, en que sugiero que agregues la documentación oficial de cada uno de los asistentes, y la transcripción de videos en Youtube en que expliquen características y cómo usarlos.
Quiero que me generes un documento markdown con introducción, nombre y versión de cada asistente revisado, la fecha en que se género el informe, explicación de las categorías en las que se analizará a cada asistente, el análisis de cada capacidad (con vínculos a la fuentes de la información y una breve descripción de cómo se instala o configura), tablas comparativas por cada capacidad.


Agrega las siguientes consideraciones:
1. Casos de uso que me gustaría implementar:
   - Análisis de requerimientos: para encontrar contradicciones, especificaciones faltantes, capacidad de sugerir acciones según buenas prácticas o patrones más utilizados.
   - Funcionalidad de generación de código basado en requerimientos y especificaciones.
   - Asistentes de revisión de estándares y buenas practicas de codificación.
   - Ejecución de debug a código construido.
   - Generación de pruebas unitarias basadas en requerimientos y especificaciones.
   - Re-factorización de código basado en requisitos.
   - Análisis de cambios realizados en un commit a repositorio Git.
   - Solicitudes de cambio: Capacidad de adaptar requerimientos y especificaciones, especificándoles de manera ordenada.
2. Considera el ambiente de desarrollo en Windows (+ WSL2 cuando corresponda).
3. Prefiere fuentes en idioma nativo que normalmente es inglés, pero si hay algo en español no es problema.
4. Prioriza la documentación oficial, pero puedes utilizar otras fuentes como reseñas y experiencias de usuarios en foros.
```

---

## Informe Generado por Claude

[**Análisis Comparativo de Asistentes CLI de Codificación para Casos de Uso Empresariales v.3:**](Análisis_Comparativo_de_Asistentes_CLI_de_Codificación_para_Casos_de_Uso_Empresariales_v.3.md)

## Informe generado por ChatGPT

[**Comparativa de asistentes de codificación CLI:**](Comparativa_de_asistentes_de_codificación_CLI.md)

Nota: para convertir de word a markdown, use el siguiente comando en la terminal:

```powershell
pandoc -s -f docx -t gfm+subscript+superscript "Comparativa_de_asistentes_de_codificación_CLI.docx" -o "Comparativa_de_asistentes_de_codificación_CLI.md" --wrap=none --markdown-headings=atx --strip-comments=true
```

## Informe generado por Gemini

[**Análisis Comparativo de Asistentes de Codificación CLI:**](Comparativa_CLIs_para_desarrollo_Windows-amplio.md)
