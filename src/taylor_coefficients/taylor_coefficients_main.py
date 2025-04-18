#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
import sys
from PyQt6.QtWidgets import QApplication
from taylor_coefficients.taylor_coefficients_view import TaylorCoefficientsView
from taylor_coefficients.taylor_coefficients_controller import TaylorCoefficientsController

def main():
    app = QApplication(sys.argv)  # Initialize the application

    # Create an instance of the view
    taylor_coefficients_view = TaylorCoefficientsView()

    # Create the controller and connect it to the view
    taylor_coefficients_controller = TaylorCoefficientsController(taylor_coefficients_view)

    # Show the view
    taylor_coefficients_view.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
