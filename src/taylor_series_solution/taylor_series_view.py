#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QFrame
)
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtCore import Qt


from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from taylor_series_solution._taylor_recurrence_relation import NUMBER_OF_INITIAL_COEFFICIENTS


class TaylorSeriesView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Sets the Title and Geometry of the window
        # Set the window title
        self.setWindowTitle("Soluciones en series de Taylor")
        # Width: 1200, Height: 700
        self.setFixedSize(1200, 700)
        # self.setGeometry(100, 100, 1200, 700)         # Set the window geometry (x, y, width, height)

        # Main Layout
        main_layout = QHBoxLayout()  # Create a horizontal layout

        # Left panel - Instructions, input fields and results
        left_panel = QVBoxLayout()  # Create a vertical layout
        # Align everything in the left panel to the top
        left_panel.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Right panel - Image and plot
        right_panel = QVBoxLayout()  # Create a vertical layout
        # Align everything in the left panel to the top
        right_panel.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add a QLabel with instructions to the left panel
        left_text = """  
            <h2>Instrucciones</h2>
            <p>Esta aplicación nos muestra la gráfica de la solución aproximada a nuestra ecuación diferencial utilizando series de Taylor.</p>
            <p> Para generar la gráfica, necesitamos el rango de los valores de <i>x,</i> el rango de los valores de <i>y,</i> los coeficientes iniciales y el número de coeficientes requeridos.</p>
            <p> Usando la relación de recurrencia y los valores de los coeficientes iniciales, este programa calcula el número de coeficientes requeridos para generar una aproximación a nuestra solución a la ecuación diferencial utilizando series de Taylor.</p>
            """                                            # Text with instructions to display in the left panel
        instructions_label = QLabel(
            left_text)                     # Create a QLabel with the text
        instructions_label.setAlignment(
            Qt.AlignmentFlag.AlignTop)  # Align the text to the top
        # Enable text wrapping
        instructions_label.setWordWrap(True)
        # Add the QLabel to the left panel
        left_panel.addWidget(instructions_label)

        # Add a QFrame separator to the left panel
        separator1 = QFrame()
        # Horizontal line separator
        separator1.setFrameShape(QFrame.Shape.HLine)
        separator1.setFrameShadow(QFrame.Shadow.Sunken)    # Make it sunken
        # Add the separator to the layout
        left_panel.addWidget(separator1)

        # Add an QLabel asking for input data to the left panel
        input_label = QLabel(
            """<h2>Datos de Entrada</h2>""")  # Create a QLabel with the Text
        left_panel.addWidget(input_label)  # Add the QLabel to the left panel

        # Add a form layout to the left panel to display the input fields
        input_form_layout = QFormLayout()  # Create a form layout
        input_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        # Create a QLabel for the xmin input field
        xmin_label = QLabel("<p>Valor mínimo de x:</p>")
        self.xmin_line_edit = QLineEdit("-5")
        self.xmin_line_edit.setValidator(
            QDoubleValidator())  # Only allow numeric input
        # Add the label and input field to the layout
        input_form_layout.addRow(xmin_label, self.xmin_line_edit)
        # Create a QLabel for the xmax input field
        xmax_label = QLabel("<p>Valor máximo de x:</p>")
        self.xmax_line_edit = QLineEdit("5")
        self.xmax_line_edit.setValidator(
            QDoubleValidator())  # Only allow numeric input
        # Add the label and input field to the layout
        input_form_layout.addRow(xmax_label, self.xmax_line_edit)
        ymin_label = QLabel("<p>Valor mínimo de y:</p>")
        self.ymin_line_edit = QLineEdit("-5")
        self.ymin_line_edit.setValidator(
            QDoubleValidator())  # Only allow numeric input
        # Add the label and input field to the layout
        input_form_layout.addRow(ymin_label, self.ymin_line_edit)
        # Create a QLabel for the xmax input field
        ymax_label = QLabel("<p>Valor máximo de y:</p>")
        self.ymax_line_edit = QLineEdit("5")
        self.ymax_line_edit.setValidator(
            QDoubleValidator())  # Only allow numeric input
        # Add the label and input field to the layout
        input_form_layout.addRow(ymax_label, self.ymax_line_edit)

        self.coefficient_inputs = []  # Create a list to store the input widgets
        coefficient_input_labels = [
            f"<p>c<sub>{k}</sub>:</p>" for k in range(NUMBER_OF_INITIAL_COEFFICIENTS)
        ]  # Labels for the input fields
        # Default values for the input fields
        default_values = ["0" for _ in range(NUMBER_OF_INITIAL_COEFFICIENTS)]
        # Add input fields to the form layout
        for label, default_value in zip(coefficient_input_labels, default_values):
            lbl = QLabel(label, self)  # Create a QLabel with the text
            line_edit = QLineEdit(self)  # Create a QLineEdit() widget
            # Only allow numeric input
            line_edit.setValidator(QDoubleValidator())
            line_edit.setText(default_value)  # Set default value
            # Add the label and input field to the layout
            input_form_layout.addRow(lbl, line_edit)
            # Store the input widget in the list
            self.coefficient_inputs.append(line_edit)
        # Create a QLabel for the number of coefficients input field
        number_of_required_coefficients_label = QLabel(
            "<p>Número de coeficientes:</p>")
        self.number_of_required_coefficients_line_edit = QLineEdit(
            f"{NUMBER_OF_INITIAL_COEFFICIENTS}")  # Create a QLineEdit() widget
        self.number_of_required_coefficients_line_edit.setValidator(
            QIntValidator())  # Only allow numeric input
        # Add the label and input field to the layout
        input_form_layout.addRow(
            number_of_required_coefficients_label, self.number_of_required_coefficients_line_edit)

        # Add a submit button to the form layout
        self.submit_button = QPushButton("Calcular")  # Create a QPushButton
        # self.submit_button.setObjectName("Submit")  # Set the object name to "Submit"
        # Add the button to the layout
        input_form_layout.addRow(self.submit_button)
        # Add the form layout to the left panel
        left_panel.addLayout(input_form_layout)

        # Add a matplotlib plot to the right panel
        self.fig, self.ax = plt.subplots(
            figsize=(12, 8))  # Create a figure and axis
        # Create a canvas to display the figure
        self.canvas = FigureCanvas(self.fig)
        # Add the canvas to the layout
        right_panel.addWidget(self.canvas)

        # Add the panels to the main layout to display them in the window
        # Add the left panel to the main layout
        main_layout.addLayout(left_panel, 2)
        separator4 = QFrame()                             # Create a QFrame
        # Vertical line separator
        separator4.setFrameShape(QFrame.Shape.VLine)
        # Make it sunken (optional)
        separator4.setFrameShadow(QFrame.Shadow.Sunken)
        # Add the separator to the layout
        main_layout.addWidget(separator4)
        # Add the right panel to the main layout
        main_layout.addLayout(right_panel, 4)
        # Set the main layout to the window
        self.setLayout(main_layout)
