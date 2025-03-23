#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-02-24
Description: 
"""

import sys

import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QFormLayout, QFrame
)
from PyQt6.QtGui import QDoubleValidator
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation


class NewtonCoolingGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RC circuit")
        self.setGeometry(100, 100, 1200, 600)

        # Main Layout
        main_layout = QHBoxLayout()

        # Left panel - Instruction and Input Fields
        left_panel = QVBoxLayout()

        # Instruction Label
        instructions = QLabel("""This application models the charge of a capacitor in a RC circuit. \n
To initialize the model, enter the values of the capacitance, the resistance and the voltage applied to the circuit.\n
This application will also show the maximum charge of the capacitor and the time constant.\n 
A capacitor is usually considered to be fully charged after waiting for 5 times the time constant.""")
        instructions.setWordWrap(True)
        left_panel.addWidget(instructions)

        # Add a divider (frame)
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        left_panel.addWidget(divider)

        # Input form
        form_layout = QFormLayout()
        self.inputs = {}
        input_labels = [
            "Capacitance:", "Resistance:", "Input voltage:"
        ]
        
        for label, default_value in zip(input_labels, ["1", "1", "1"]):
            lbl = QLabel(label, self)
            form_layout.addRow(lbl)
            line_edit = QLineEdit(self)
            line_edit.setValidator(QDoubleValidator())  # Only allow numeric input
            line_edit.setText(default_value)  # Set default value
            form_layout.addRow(line_edit)
            self.inputs[label] = line_edit

        # Add form layout to left panel
        left_panel.addLayout(form_layout)

        # Compute Button
        self.compute_button = QPushButton("Submit", self)
        self.compute_button.clicked.connect(self.compute_temperature)
        left_panel.addWidget(self.compute_button)

        # Result Display
        self.result_label = QLabel("Maximum charge: ", self)
        left_panel.addWidget(self.result_label)

        self.result2_label = QLabel("Time constant: ", self)
        left_panel.addWidget(self.result2_label)



        # Right panel - Animation
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        right_panel = QVBoxLayout()
        right_panel.addWidget(self.canvas)

        # Add panels to main layout
        main_layout.addLayout(left_panel, 2)  # Left panel takes 2/3 of space
        main_layout.addLayout(right_panel, 3) # Right panel takes 3/3 of space
        self.setLayout(main_layout)

        # To keep track of the current animation object
        self.ani = None

        # Initialize the animation 
        self.compute_temperature()

    def compute_temperature(self):
        try:
            capacitance= float(self.inputs["Capacitance:"].text())
            resistance = float(self.inputs["Resistance:"].text())
            input_voltage= float(self.inputs["Input voltage:"].text())

            if capacitance <= 0:
                raise ValueError("Capacitance should be positive.")
            if resistance <= 0:
                raise ValueError("Resistance should be positive.")
            if input_voltage<= 0:
                raise ValueError("Input voltage should be positive.")


            # Compute Temperature at Final Time
            self.RC_circuit_function = self.RC_circuit_law(capacitance,resistance,input_voltage
            )

            max_charge=input_voltage*capacitance
            time_constant=resistance*capacitance

            self.result_label.setText(f"Maximum charge: {max_charge:.2f}")
            self.result2_label.setText(f"Time constant: {time_constant:.2f}")

            # Stop the previous animation (if any) before starting a new one
            if self.ani is not None:
                self.ani.event_source.stop()  # Stop the animation
                self.ax.clear()  # Clear the previous axes

            # Start new animation
            self.animate_charge_change(capacitance, resistance, input_voltage)

        except ValueError as e:
            QMessageBox.critical(self, "Input Error", str(e))

    def RC_circuit_law(self, capacitance, resistance, input_voltage):
        def RC_circuit_function(t):
            C=capacitance
            R=resistance
            epsilon=input_voltage
            q=epsilon*C*(1-np.exp(-t/(R*C)))
            return q 

        return RC_circuit_function 

    def animate_charge_change(self, capacitance, resistance, input_voltage):
        self.ax.clear()

        max_charge=input_voltage*capacitance
        time_constant=resistance*capacitance 
        first_time=0 
        final_time=5*time_constant

        self.time_data = np.linspace(first_time, final_time, 100)
        self.charge_data = self.RC_circuit_function(self.time_data)
        self.max_charge_data= np.full(100, max_charge)

        self.charge_line, = self.ax.plot([], [], lw=2, label="Capacitor Charge")
        self.max_charge_line, = self.ax.plot([], [], lw=2, label="Maximum Charge")

        # Set axis limits
        time_interval = final_time - first_time
        self.ax.set_xlim(first_time - 0.1 * time_interval, final_time + 0.1 * time_interval)
        self.ax.set_ylim(0,max_charge*1.1)

        # Labels & Title
        self.ax.set_xlabel("Time",labelpad=15)
        self.ax.set_ylabel("Charge",labelpad=10)
        self.ax.set_title("RC circuit Simulation")


        # Set legend
        self.ax.legend(
        frameon=True,
        fancybox=False,
        loc= "lower right",
        labelspacing=1.2)


        # Matplotlib Animation
        self.ani = FuncAnimation(self.figure, self.update_animation, frames=len(self.time_data), interval=50, blit=True)

        # Redraw canvas
        self.canvas.draw()

    def update_animation(self, frame):
        self.charge_line.set_data(self.time_data[:frame], self.charge_data[:frame]) 
        self.max_charge_line.set_data(self.time_data[:frame], self.max_charge_data[:frame])  
        return self.charge_line, self.max_charge_line


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewtonCoolingGUI()
    window.show()
    sys.exit(app.exec())

