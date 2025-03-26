#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-21
Description: 
"""
from pathlib import Path

from PyQt6.QtWidgets import (
        QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QFrame
        )
from PyQt6.QtGui import QDoubleValidator, QPixmap
from PyQt6.QtCore import Qt



from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class RCCircuitView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Sets the Title and Geometry of the window
        self.setWindowTitle("RC circuit")              # Set the window title
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
            <h2>Instructions</h2>
            <p>This application models the charge of a capacitor in an RC circuit, like the one shown in the figure on the right.</p>
            <p>To initialize the model, simply enter the values of the capacitance, resitance, and input voltage applied to the circuit and then press the submit buttom.</p>
            <p>The panel on the right will then display the charge of the capacitor as a function of time.</p>
            <p>The application will also compute the maximum charge of the capacitor at the end of the charging process and its associated time constant.</p>
            <p>A capacitor is usually considered fully charged after 5 time constants.</p>
            <p><strong>Note:</strong> We will be implicitly assuming that the capacitance is measured in farads, the resistance in ohms, the voltage in volts and the time in seconds.</p>
            """                                            # Text with instructions to display in the left panel
        instructions_label= QLabel(left_text)                     # Create a QLabel with the text
        instructions_label.setAlignment(Qt.AlignmentFlag.AlignTop) # Align the text to the top
        instructions_label.setWordWrap(True)                       # Enable text wrapping
        left_panel.addWidget(instructions_label,2)                 # Add the QLabel to the left panel 

        # Add a QFrame separator to the left panel 
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)       # Horizontal line separator
        separator1.setFrameShadow(QFrame.Shadow.Sunken)    # Make it sunken 
        left_panel.addWidget(separator1)                   # Add the separator to the layout 

        # Add an QLabel asking for input data to the left panel       
        input_label= QLabel("""<h2>Input data</h2>""") # Create a QLabel with the Text
        left_panel.addWidget(input_label,1) # Add the QLabel to the left panel 


        # Add a form layout to the left panel to display the input fields 
        input_form_layout = QFormLayout() # Create a form layout
        self.inputs = {} # Create a dictionary to store the input widgets 
        input_labels = [
            "<p>Capacitance:</p>", "<p>Resistance:</p>", "<p>Input Voltage:</p>"
        ] # Labels for the input fields
        default_values = ["1", "1", "1"] # Default values for the input fields
        for label, default_value in zip(input_labels, default_values): # Add input fields to the form layout
            lbl = QLabel(label, self) # Create a QLabel with the text
            line_edit = QLineEdit(self) # Create a QLineEdit() widget 
            line_edit.setValidator(QDoubleValidator())  # Only allow numeric input
            line_edit.setText(default_value)  # Set default value
            input_form_layout.addRow(lbl,line_edit) # Add the label and input field to the layout 
            self.inputs[label] = line_edit  # Store the input widget in the dictionary 

        # Add a submit button to the form layout
        self.submit_button = QPushButton("Submit")  # Create a QPushButton
        # self.submit_button.setObjectName("Submit")  # Set the object name to "Submit"
        input_form_layout.addRow(self.submit_button)      # Add the button to the layout
        left_panel.addLayout(input_form_layout,1) # Add the form layout to the left panel

        # Add a QFrame separator to the left panel 
        separator2 = QFrame()                            # Create a QFrame
        separator2.setFrameShape(QFrame.Shape.HLine)     # Horizontal line separator
        separator2.setFrameShadow(QFrame.Shadow.Sunken)  # Make it sunken (optional)
        left_panel.addWidget(separator2)                 # Add the separator to the layout 

        # Add a QLabel indicating the results to the left panel 
        result_text = """
        <h2>Results</h2>
        """ # Text to display the results 
        results_label = QLabel(result_text) # Create a QLabel with the results 
        results_label.setAlignment(Qt.AlignmentFlag.AlignTop) # Align the text to the top 
        results_label.setWordWrap(True)  # Enable text wrapping
        left_panel.addWidget(results_label,1) # Add the QLabel to the left panel

        # Add a form layout to the left panel to display the results 
        results_form_layout = QFormLayout() # Create a form Layout
        self.maximum_charge_label = QLabel() # Create a QLabel to display the maximum charge
        self.time_constant_label = QLabel() # Create a QLabel to display the time constant
        results_form_layout.addRow(QLabel("""<p>Maximum Charge:</p>"""),self.maximum_charge_label) 
        results_form_layout.addRow(QLabel("""<p>Time Constant:</p>"""),self.time_constant_label) 
        left_panel.addLayout(results_form_layout,1) # Add the form layout to the left panel 

        # Add an image to the right panel
        image_path = Path(__file__).parent / 'images' / 'RC_circuit.jpg' #Get the path to the image file
        image_label = QLabel()  # Create a QLabel to display the image
        pixmap = QPixmap(str(image_path))  # Load the image using QPixmap
        image_label.setPixmap(pixmap)  # Set the image to the QLabel
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
        right_panel.addWidget(image_label)  # Add the image to the right panel

        # Add a QFrame separator to the right panel 
        separator3 = QFrame()                            # Create a QFrame
        separator3.setFrameShape(QFrame.Shape.HLine)     # Horizontal line separator
        separator3.setFrameShadow(QFrame.Shadow.Sunken)  # Make it sunken (optional)
        right_panel.addWidget(separator3)                 # Add the separator to the layout 

        # Add a matplotlib plot to the right panel       
        self.fig, self.ax = plt.subplots(figsize=(9, 6)) # Create a figure and axis
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


