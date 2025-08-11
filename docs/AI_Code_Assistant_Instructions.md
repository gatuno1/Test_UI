# CLAUDE.md

This file provides guidance to an AI Code Assistant when working with code in this repository.

## Project Overview

This is a comprehensive UI framework comparison project featuring 6 Python desktop applications that implement the same office products quotation generator. Each demo showcases different GUI frameworks while maintaining identical functionality and visual design for direct comparison.

## Project Structure

The repository contains 6 framework demonstrations with specific structure for each:

- **Demo_customtkinter/**: Modern Tkinter with enhanced widgets, collapsible sections, and custom themes
- **Demo_flet/**: Flutter-based declarative framework with modular components
- **Demo_PySide6/**: Qt6 Python bindings with professional QTableWidget implementation
- **Demo_QtQuick/**: Qt6 with QML declarative UI separated from Python backend logic
- **Demo_tkinter_ttk/**: Tkinter with themed TTK widgets and custom collapsible frames
- **Demo_wxPython/**: Native cross-platform GUI with wx.grid.Grid and comprehensive testing

## Unified Visual Design

All demos implement identical visual specifications explained on ASCII art diagrams:

### Color Palette

As customtkinter theme: !['light-blue'](Tema_light-blue.png)

### Interface Layout Requirements

  Read document [Especificaciones interfaz de usuario](Especificaciones_UI.md)

## Framework-Specific Directory Structure

Each demo has a tailored structure for its framework requirements:

### Demo_customtkinter/

```text
Demo_customtkinter/
├── README.md                   # CustomTkinter-specific guide
├── requirements.txt            # customtkinter, jinja2, weasyprint, pydyf
├── pyproject.toml              # Project config
├── main.py                     # App with collapsible sections
├── utils.py                    # Common formatting utilities
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

### Demo_flet/

```text
Demo_flet/
├── README.md                   # Flet-specific guide
├── requirements.txt            # flet[desktop]==0.28.3, jinja2, weasyprint, pydyf
├── pyproject.toml              # Project config
├── main.py                     # Declarative Flutter-style app
├── components/                 # Modular UI components
│   ├── client_form.py          # Client data form
│   └── product_table.py        # Product table component
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

### Demo_PySide6/

```text
Demo_PySide6/
├── README.md                   # PySide6-specific guide
├── requirements.txt            # PySide6==6.6.0, jinja2, weasyprint, pydyf
├── pyproject.toml              # Project config + Qt-specific
├── main.py                     # Professional Qt6 application
├── ui/                         # Separated UI modules
│   ├── main_window.py          # Main window class
│   └── product_table.py        # QTableWidget implementation
├── utils/
│   └── formatters.py           # Qt-specific formatting
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

### Demo_QtQuick/

```text
Demo_QtQuick/
├── README.md                   # QtQuick/QML-specific guide
├── requirements.txt            # PySide6==6.6.0, jinja2, weasyprint, pydyf
├── pyproject.toml              # Qt + QML configuration
├── pyrightconfig.json          # TypeScript-style type checking
├── main.py                     # Python backend with signals
├── qml/                        # Declarative QML interface
│   ├── main.qml                # Main UI definition
│   ├── ClientForm.qml          # Client form component
│   └── ProductTable.qml        # Product table component
├── backend/                    # Python business logic
│   ├── app_controller.py       # Main controller
│   └── formatters.py           # Data formatting
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

### Demo_tkinter_ttk/

```text
Demo_tkinter_ttk/
├── README.md                   # Tkinter TTK-specific guide
├── requirements.txt            # jinja2, weasyprint, pydyf (tkinter built-in)
├── pyproject.toml              # Project config
├── main.py                     # Standard Tkinter with TTK
├── widgets/                    # Custom TTK widgets
│   ├── collapsible_frame.py    # Custom collapsible frame
│   └── product_treeview.py     # Formatted Treeview
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

### Demo_wxPython/

```text
Demo_wxPython/
├── README.md                   # wxPython-specific guide
├── requirements.txt            # wxPython, jinja2, weasyprint, pydyf
├── pyproject.toml              # Project config
├── tox.ini                     # Automated testing configuration
├── main.py                     # Native cross-platform app
├── panels/                     # Modular wx panels
│   ├── client_panel.py         # Client data panel
│   └── product_grid.py         # wx.grid.Grid implementation
└── templates/
    └── cotizacion.html         # Template with CSS styling
```

## Common Development Commands

### Environment Setup

```bash
# Create virtual environment with uv: 3.12 python environment (preferred method)
uv venv .venv --python 3.12 --managed-python --seed

# Alternative method (fallback if uv not available)
python -m venv .venv

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate (Linux/macOS)
source .venv/bin/activate

# Install specific framework dependencies
cd Demo_[framework]/
uv pip install -r requirements.txt

# Install development tools (from base directory)
cd ..
uv pip install -r requirements-dev.txt

# Alternative method (fallback if uv not available)
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running Applications

```bash
# Run any specific demo
cd Demo_[framework]/
python main.py
```

### Development Tools

```bash
# Linting and formatting (available across projects)
pylint main.py           # Análisis estático completo
ruff check .             # Alternativa rápida y moderna
ruff format .            # Formateo rápido

# Testing (where implemented)
pytest                   # Tests unitarios básicos
pytest --cov=cotizador   # Tests con análisis de cobertura
pytest-mock  # Mock objects for testing
pytest-qt    # Qt-specific testing utilities

# Code coverage analysis
coverage run -m pytest
coverage report
coverage html

# Performance profiling
scalene main.py

# Debugging
debugpy        # Debug adapter for Python

# Test automation (wxPython demo)
tox          # Automatización de testing en múltiples entornos
tox -e lint  # Pipeline de linting completo
tox -e py312 # Test en Python 3.12 específicamente
```

## Shared Architecture and Standards

All demos implement identical functionality using common patterns while respecting framework-specific approaches:

### Core Components

1. **main.py**: Application entry point with GUI logic (structure varies by framework)
2. **templates/cotizacion.html**: Jinja2 HTML template for PDF generation with unified color palette
3. **requirements.txt**: Framework-specific dependencies
4. **README.md**: Framework-specific setup and execution guide
5. **pyproject.toml**: Project configuration with linting, formatting, and testing tools

### Application Flow

1. **Client Data Entry**: Name input with validation in dedicated section
2. **Product Management**: Add/edit products with input validation and automatic formatting of quantity/price fields
3. **Collapsible Interface**: ~~Products section toggles between expanded/collapsed states~~
4. **PDF Preview**: Optional preview section shows formatted quotation
5. **PDF Generation**: Render HTML template using Jinja2 → Convert to PDF with WeasyPrint
6. **File Export**: Save PDF using native file dialogs with proper error handling

### Formatting Standards

All demos implement consistent number formatting:

#### Input Field Formatting (on focus lost)

- **Quantity fields**: Integer formatting with thousands separators locale aware
- **Price fields**: Currency formatting with locale-aware thousands separators, money sign and decimal places
- **Implementation**: `format_cantidad_input()` and `format_precio_input()` functions
  TODO: specify requirements for input formatting functions, optional parameters and internal use of round numbering

#### Table/Grid Cell Formatting

- **Quantity columns**: Right-aligned integers with separators
- **Price columns**: Right-aligned currency with decimal places
- **Implementation**: `format_integer()` and `format_currency()` utility functions
  TODO: specify requirements for formatting functions, optional parameters and internal use of round numbering

#### PDF Generation Formatting

- **All monetary values**: ~~Locale-aware currency formatting~~
- **All quantities**: ~~Integer formatting with separators~~
- **Implementation**: ~~Consistent use of formatting functions in template context~~

### Common Dependencies

- **Jinja2**: HTML template rendering with color palette variables
- **WeasyPrint==61.2**: HTML to PDF conversion
- **pydyf==0.10.0**: Required for WeasyPrint compatibility

## Framework-Specific Implementation Notes

### CustomTkinter

- **Collapsible Sections**: Custom frame implementation with toggle buttons
- **Theme Integration**: Uses defined theme
- **Event Binding**: `bind("<FocusOut>")` for automatic field formatting
- **File Structure**: Single `main.py` with `utils.py` for formatting functions

### Flet

- **Component Architecture**: Modular components in `components/` directory
- **State Management**: Declarative state updates with `update()` calls
- **Validation**: Integrated form validation with SnackBar notifications
- **Event Handling**: `on_blur` events for field formatting

### PySide6

- **Project Config**: Uses `pyproject.toml` with Black, Pylint, Ruff configurations
- **Modular Design**: Separated UI classes in `ui/` directory
- **Qt Integration**: QTableWidget with custom cell formatting
- **Signal/Slot**: Event-driven architecture with Qt signals
- **Type Hints**: Comprehensive type annotations required (Python 3.12+)

### QtQuick

- **QML-Python Bridge**: Context properties for data binding between QML and Python
- **File Organization**: QML files in `qml/`, Python backend in `backend/`
- **Type Checking**: `pyrightconfig.json` for TypeScript-style Python checking
- **Async Communication**: Qt signals for non-blocking operations
- **Declarative UI**: Complete UI definition in QML with Python business logic

### Tkinter TTK

- **Built-in Widgets**: Uses standard library TTK widgets with custom enhancements
- **Custom Widgets**: Collapsible frames and formatted Treeview in `widgets/`
- **Theme Support**: Native OS themes with TTK styling
- **No External Dependencies**: Only requires template and PDF generation libraries

### wxPython

- **Native Appearance**: Platform-native controls and dialogs
- **Grid Implementation**: wx.grid.Grid for professional data entry
- **Sizer Layout**: Responsive layout using wxPython sizer system

## Development Workflow

1. **Choose Framework**: Select target demo directory based on requirements
2. **Environment Setup**: Create virtual environment and install framework-specific dependencies
3. **Run Application**: Execute `python main.py` to test functionality
4. **Code Quality**: Use appropriate linting tools for each framework
5. **Generate Tests**: Create appropriated test for each program
6. **Testing**: Run framework-specific tests implemented
7. **PDF Testing**: Verify PDF generation with sample data using institutional color scheme

## Template System

All projects use identical Jinja2 variables in `templates/cotizacion.html` with institutional styling:

### Template Variables

- `{{ cliente }}`: Client name
- `{{ fecha }}`: Current date (DD/MM/YYYY format)
- `{{ items }}`: Product list with quantity, unit_price, total
- `{{ total_general }}`: Grand total calculation

### CSS Styling (Embedded)

TODO: extract from theme definition

## Code Quality Standards

- **Python Version**: 3.12+ with comprehensive type hints
- **Line Length**: 88 characters (Black standard)
- **Error Handling**: Consistent validation and user feedback
- **File Dialogs**: Native platform dialogs for PDF export
- **Locale Support**: Currency and quantity (integers and float) formatting using `locale` module
- **Formatting Functions**: Standardized `format_integer()` and `format_currency()` across all demos
