# AI Project Assistant Instructions

This file provides guidance to an AI Project Assistant when working with files in this repository.

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

## UI Specifications

Complete UI requirements are defined in `Especificaciones_UI.md` including:

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

## Next Steps

- 1 **Choose Framework**: Select which framework to implement first (already completed; CustomTkinter with 'Oceanix' theme selected)
- 2 **Framework Evaluation Steps**
  - 2.1. Review the official documentation and available resources for CustomTkinter, focusing on theme customization, accessibility features, and responsive design capabilities.
  - 2.2. Prototype key UI components using the 'Oceanix' theme
    - 2.2.1 Main window and floating panels
    - 2.2.2 Collapsible sections and toggle indicators
    - 2.2.3 Product table with CRUD operations and custom formatting
    - 2.2.4 Validation messages and pop-up controls
  - 2.3 Assess responsive behavior, verifying layout adaptation to different window sizes and zoom levels.
  - 2.4 Document strengths, limitations, and any required workarounds for CustomTkinter with the 'Oceanix' theme regarding the UI specifications.
  - 2.5 Prepare a comparison matrix to facilitate framework selection for subsequent implementations.
- 3 **Implement Core Application**: Following `docs/Especificaciones_UI.md` specifications
- 4 **Add Testing**: Unit tests and framework-specific test utilities
- 5 **Repeat**: Implement same functionality in other frameworks for comparison

## ASCII Diagrams Reference

The `docs/Especificaciones_UI.md` contains detailed ASCII art diagrams showing:

- Complete window layout and component arrangement
- Collapsible section states (expanded/collapsed)
- Table structure with column specifications
- Responsive behavior requirements
- User interaction flows

Reference these diagrams when implementing any framework to ensure visual consistency across all implementations.
