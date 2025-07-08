#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
import sys
from PyQt6.QtWidgets import QApplication
from taylor_series_solution.taylor_series_view import TaylorSeriesView
from taylor_series_solution.taylor_series_controller import TaylorSeriesController


def main():
    app = QApplication(sys.argv)  # Initialize the application

    # Create an instance of the view
    taylor_series_view = TaylorSeriesView()

    # Create the controller and connect it to the view
    taylor_series_controller = TaylorSeriesController(taylor_series_view)

    # Show the view
    taylor_series_view.show()

    # Start the application's event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
