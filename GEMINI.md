# Project Overview

This project aims to compare and implement the same desktop application using different Python UI frameworks. The goal is to analyze the capabilities, advantages, and disadvantages of each framework.

The application will be implemented in the following frameworks:

* CustomTkinter
* Flet
* Kivy
* PySide6
* QtQuick
* Tkinter + ttk
* wxPython

The core of the project is to build a product quoting application. The UI specifications are detailed in `docs/Especificaciones_UI.md`.

## Building and Running

The project is structured to have a separate implementation for each UI framework. While there are no specific build commands defined yet, the following steps can be inferred from the project structure and dependencies:

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

2. **Run the application for a specific framework:**

    ```bash
    # TODO: Add the command to run the application for each framework
    # For example, for CustomTkinter:
    # python src/customtkinter_app/main.py
    ```

3. **Run tests:**

    ```bash
    pytest
    ```

## Development Conventions

The development conventions are described in the `docs/Especificaciones_UI.md` file. Here are some of the key conventions:

* **UI Design:** The UI must be intuitive, easy to use, and follow the best practices of UI/UX. It should be responsive and adapt to different window sizes.
* **Accessibility:** The UI must be accessible to people with disabilities, following the WCAG 2.1 level AA guidelines.
* **Code Style:** The code should be clean, readable, and well-documented.
* **Testing:** The project should have a comprehensive test suite, including unit tests and integration tests.
* **Framework-specific implementations:** Each framework implementation should be self-contained and not depend on other framework implementations.
