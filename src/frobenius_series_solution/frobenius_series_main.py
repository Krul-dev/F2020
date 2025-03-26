#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
import sys
from PyQt6.QtWidgets import QApplication
from frobenius_series_solution.frobenius_series_view import FrobeniusSeriesView
from frobenius_series_solution.frobenius_series_controller import FrobeniusSeriesController

def main():
    app = QApplication(sys.argv)  # Initialize the application

    # Create an instance of the view
    frobenius_series_view = FrobeniusSeriesView()

    # Create the controller and connect it to the view
    frobenius_series_controller=FrobeniusSeriesController(frobenius_series_view)

    # Show the view
    frobenius_series_view.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

