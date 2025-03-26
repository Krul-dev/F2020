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

from frobenius_series_solution._frobenius_recurrence_relation import NUMBER_OF_INITIAL_COEFFICIENTS


class FrobeniusSeriesView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Sets the Title and Geometry of the window
        self.setWindowTitle("Soluciones en series de Frobenius")              # Set the window title
        self.setFixedSize(1200, 700)                   # Width: 1200, Height: 700
        #self.setGeometry(100, 100, 1200, 700)         # Set the window geometry (x, y, width, height)

        # Main Layout 
        main_layout = QHBoxLayout() # Create a horizontal layout 

        # Left panel - Instructions, input fields and results
        left_panel = QVBoxLayout() # Create a vertical layout 
        left_panel.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align everything in the left panel to the top


        # Right panel - Image and plot 
        right_panel = QVBoxLayout() # Create a vertical layout 
        right_panel.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align everything in the left panel to the top

        # Add a QLabel with instructions to the left panel
        left_text = """  
            <h2>Instrucciones</h2>
            <p>Esta aplicación nos muestra la gráfica de la solución aproximada a nuestra ecuación diferencial utilizando series de Frobenius.</p>
            <p> Para generar la gráfica, necesitamos el rango de los valores de <i>x</i>, los coeficientes iniciales y el número de coeficientes requeridos.</p>
            <p> Usando el índice obtenido al resolver la ecuación indicial, la relación de recurrencia y los valores de los coeficientes iniciales, este programa calcula el número de coeficientes requeridos para generar una aproximación a nuestra solución a la ecuación diferencial utilizando series de Frobenius.</p>
            """                                            # Text with instructions to display in the left panel
        instructions_label= QLabel(left_text)                     # Create a QLabel with the text
        instructions_label.setAlignment(Qt.AlignmentFlag.AlignTop) # Align the text to the top
        instructions_label.setWordWrap(True)                       # Enable text wrapping
        left_panel.addWidget(instructions_label)                 # Add the QLabel to the left panel 

        # Add a QFrame separator to the left panel 
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)       # Horizontal line separator
        separator1.setFrameShadow(QFrame.Shadow.Sunken)    # Make it sunken 
        left_panel.addWidget(separator1)                   # Add the separator to the layout 

        # Add an QLabel asking for input data to the left panel       
        input_label= QLabel("""<h2>Datos de Entrada</h2>""") # Create a QLabel with the Text
        left_panel.addWidget(input_label) # Add the QLabel to the left panel 


        # Add a form layout to the left panel to display the input fields 
        input_form_layout = QFormLayout() # Create a form layout
        input_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        xmin_label = QLabel("<p>Valor mínimo de x:</p>") # Create a QLabel for the xmin input field 
        self.xmin_line_edit = QLineEdit("-5")
        self.xmin_line_edit.setValidator(QDoubleValidator())  # Only allow numeric input 
        input_form_layout.addRow(xmin_label, self.xmin_line_edit) # Add the label and input field to the layout 
        xmax_label = QLabel("<p>Valor máximo de x:</p>") # Create a QLabel for the xmax input field 
        self.xmax_line_edit = QLineEdit("5") 
        self.xmax_line_edit.setValidator(QDoubleValidator())  # Only allow numeric input 
        input_form_layout.addRow(xmax_label, self.xmax_line_edit) # Add the label and input field to the layout 
        self.coefficient_inputs = [] # Create a list to store the input widgets 
        coefficient_input_labels = [
            f"<p>c<sub>{k}</sub>:</p>" for k in range(NUMBER_OF_INITIAL_COEFFICIENTS)
        ] # Labels for the input fields
        default_values = ["0" for _ in range(NUMBER_OF_INITIAL_COEFFICIENTS)] # Default values for the input fields
        for label, default_value in zip(coefficient_input_labels, default_values): # Add input fields to the form layout
            lbl = QLabel(label, self) # Create a QLabel with the text
            line_edit = QLineEdit(self) # Create a QLineEdit() widget 
            line_edit.setValidator(QDoubleValidator())  # Only allow numeric input
            line_edit.setText(default_value)  # Set default value
            input_form_layout.addRow(lbl,line_edit) # Add the label and input field to the layout 
            self.coefficient_inputs.append(line_edit)  # Store the input widget in the list
        number_of_required_coefficients_label = QLabel("<p>Número de coeficientes:</p>") # Create a QLabel for the number of coefficients input field 
        self.number_of_required_coefficients_line_edit = QLineEdit(f"{NUMBER_OF_INITIAL_COEFFICIENTS}") # Create a QLineEdit() widget
        self.number_of_required_coefficients_line_edit.setValidator(QIntValidator())  # Only allow numeric input 
        input_form_layout.addRow(number_of_required_coefficients_label, self.number_of_required_coefficients_line_edit) # Add the label and input field to the layout 


        # Add a submit button to the form layout
        self.submit_button = QPushButton("Calcular")  # Create a QPushButton
        # self.submit_button.setObjectName("Submit")  # Set the object name to "Submit"
        input_form_layout.addRow(self.submit_button)      # Add the button to the layout
        left_panel.addLayout(input_form_layout) # Add the form layout to the left panel

        # Add a matplotlib plot to the right panel       
        self.fig, self.ax = plt.subplots(figsize=(12, 8)) # Create a figure and axis
        self.canvas = FigureCanvas(self.fig)             # Create a canvas to display the figure 
        right_panel.addWidget(self.canvas)                  # Add the canvas to the layout


        # Add the panels to the main layout to display them in the window 
        main_layout.addLayout(left_panel,2)               # Add the left panel to the main layout
        separator4 = QFrame()                             # Create a QFrame
        separator4.setFrameShape(QFrame.Shape.VLine)      # Vertical line separator
        separator4.setFrameShadow(QFrame.Shadow.Sunken)   # Make it sunken (optional)
        main_layout.addWidget(separator4)                 # Add the separator to the layout 
        main_layout.addLayout(right_panel,4)              # Add the right panel to the main layout 
        self.setLayout(main_layout)                       # Set the main layout to the window 


