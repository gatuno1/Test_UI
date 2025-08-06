# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python UI framework comparison project in **initial planning phase**. The goal is to implement identical "Cotizador de Productos" (Product Quotation) desktop applications across multiple Python GUI frameworks for direct comparison.

**Current Status**: Documentation and setup phase - no implementations exist yet.

## Target Frameworks for Implementation

The project plans to compare these 7 Python GUI frameworks:

- CustomTkinter
- Flet
- Kivy
- PySide6
- QtQuick
- Tkinter + TTK
- wxPython

## Development Commands

### Environment Setup

```bash
# Preferred method: Create virtual environment with uv
uv venv .venv --python 3.11 --managed-python --seed
.\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Install dependencies with uv (preferred)
uv pip install -r requirements.txt        # All frameworks
uv pip install -r requirements-dev.txt    # Development tools

# Alternative method (if uv not available)
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Development Tools

```bash
# Code quality tools available
pylint <file.py>         # Static analysis
ruff check .             # Fast linting
ruff format .            # Code formatting
pytest                   # Testing framework
coverage run -m pytest   # Coverage analysis
scalene <file.py>        # Performance profiling
debugpy                  # Debug adapter
```

## Current Project Structure

```asciiart
Test_UI_v3/
├── README.md                           # Project description
├── requirements.txt                    # All framework dependencies
├── requirements-dev.txt                # Development tools
├── .python-version                     # Python 3.11
├── .gitignore                          # Comprehensive Python gitignore
├── docs/
│   ├── Especificaciones_UI.md          # Detailed UI specifications
│   ├── AI_Code_Assistant_Instructions.md  # Previous iteration docs
│   └── references/                     # Color themes and examples
├── global_templates/
│   └── cotizacion.html                 # HTML template for PDF generation
├── src/                                # Empty - ready for source code
└── tests/                              # Empty - ready for test files
```

## UI Specifications

Complete UI requirements are defined in `docs/Especificaciones_UI.md` including:

- **WCAG 2.1 AA compliance** for accessibility
- **Responsive design** (minimum 800x600, adaptable)
- **Collapsible sections** for product details
- **Data validation** for client names, products, quantities, prices
- **Locale-aware formatting** for currency and numbers
- **PDF generation** using Jinja2 + WeasyPrint

### Key UI Components Required

- Client data entry section
- Collapsible product details table with add/edit/delete
- Automatic calculations (totals, item counts)
- PDF preview section (optional)
- Action buttons (Save PDF, Clear Data, Close)

## Template System

`global_templates/cotizacion.html` contains:

- Professional HTML/CSS template for PDF generation
- Institutional color palette defined in CSS variables
- Jinja2 template variables: `{{ cliente }}`, `{{ fecha }}`, `{{ items }}`, `{{ total_general }}`

## Dependencies

### All Framework Dependencies (`requirements.txt`)

```text
jinja2              # HTML templating
pydyf==0.10.0      # PDF generation support
WeasyPrint==61.2   # HTML to PDF conversion
customtkinter      # CustomTkinter framework
flet[desktop]==0.28.3  # Flet framework
PySide6==6.6.0     # Qt6 bindings
wxPython           # wxWidgets bindings
```

### Development Tools (`requirements-dev.txt`)

```text
coverage           # Code coverage
debugpy           # Debug adapter
pylint            # Static analysis
pytest            # Testing framework
pytest-cov       # Coverage integration
pytest-mock      # Mock objects
pytest-qt        # Qt testing utilities
scalene           # Performance profiler
```

## Implementation Standards

When implementing frameworks:

- **Python Version**: 3.11+ with type hints
- **Code Style**: 88 character line length (Black standard)
- **Project Structure**: Each framework in `Demo_[framework]/` directory
- **Validation**: Comprehensive input validation with clear error messages
- **Formatting**: Locale-aware currency and quantity formatting using `locale` module
- **Testing**: Unit tests with pytest, coverage analysis
- **Documentation**: Framework-specific README.md files

## Next Steps

1. **Choose Framework**: Select which framework to implement first
2. **Create Demo Directory**: `Demo_[framework]/` with framework-specific structure
3. **Implement Core Application**: Following `docs/Especificaciones_UI.md` specifications
4. **Add Testing**: Unit tests and framework-specific test utilities
5. **Repeat**: Implement same functionality in other frameworks for comparison

## ASCII Diagrams Reference

The `docs/Especificaciones_UI.md` contains detailed ASCII art diagrams showing:

- Complete window layout and component arrangement
- Collapsible section states (expanded/collapsed)
- Table structure with column specifications
- Responsive behavior requirements
- User interaction flows

Reference these diagrams when implementing any framework to ensure visual consistency across all implementations.
