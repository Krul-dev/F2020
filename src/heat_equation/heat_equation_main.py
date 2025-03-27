#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
import sys
from PyQt6.QtWidgets import QApplication
from heat_equation.heat_equation_view import HeatEquationView
from heat_equation.heat_equation_controller import HeatEquationController

def main():
    app = QApplication(sys.argv)  # Initialize the application

    # Create an instance of the view
    heat_equation_view = HeatEquationView()

    # Create the controller and connect it to the view
    heat_equation_controller=HeatEquationController(heat_equation_view)

    # Show the view
    heat_equation_view.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

