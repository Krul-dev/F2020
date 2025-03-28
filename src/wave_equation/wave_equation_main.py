#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
import sys
from PyQt6.QtWidgets import QApplication
from wave_equation.wave_equation_view import WaveEquationView
from wave_equation.wave_equation_controller import WaveEquationController

def main():
    app = QApplication(sys.argv)  # Initialize the application

    # Create an instance of the view
    wave_equation_view = WaveEquationView()

    # Create the controller and connect it to the view
    wave_equation_controller=WaveEquationController(wave_equation_view)

    # Show the view
    wave_equation_view.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

