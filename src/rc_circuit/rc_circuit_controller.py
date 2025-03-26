#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""
from PyQt6.QtWidgets import QMessageBox
from rc_circuit.rc_circuit_model import RCCircuitModel
from rc_circuit.rc_circuit_view import RCCircuitView
import numpy as np

# Controller class for the application
class RCCircuitController:
    # Define the constructor
    def __init__(self, view : RCCircuitView):
        # Initialize the controller with the view
        self.view = view

        # Connect the submit button to the submit subroutine
        self.view.submit_button.clicked.connect(self.submit)

        # Initialize the model with default values
        self.submit()


    # Subroutine to get the user input  
    def get_user_input(self):
        # Validate inputs before using them

        # Validate capacitance
        try:
            capacitance = float(self.view.inputs["<p>Capacitance:</p>"].text())
            if capacitance <= 0:
                self.show_error("Invalid input", "Capacitance must be a positive number.")
                return None
        except ValueError:
            self.show_error("Invalid input", "Please enter a valid number.")
            return None

        # Validate resistance 
        try: 
            resistance = float(self.view.inputs["<p>Resistance:</p>"].text())
            if resistance <= 0:
                self.show_error("Invalid input", "Resistance must be a positive number.")
                return None
        except ValueError:
            self.show_error("Invalid input", "Please enter a valid number.")
            return None 

        # Validate input voltage 
        try:
            input_voltage = float(self.view.inputs["<p>Input Voltage:</p>"].text())
            if input_voltage <= 0:
                self.show_error("Invalid input", "Input voltage must be a positive number.")
                return None 
        except ValueError:
            self.show_error("Invalid input", "Please enter a valid number.")
            return None
        
        return capacitance, resistance, input_voltage
   

    # Subroutine to update the view with the model values
    def update_view(self,rc_circuit_model):
        # Update the view with the current model values 
        # Get the results from the model 
        max_charge = rc_circuit_model.get_max_charge()
        time_constant = rc_circuit_model.get_time_constant()
        charge_function = rc_circuit_model.get_charge_function()
        xmin = rc_circuit_model.get_xmin()
        xmax = rc_circuit_model.get_xmax()

        # Update the maximum charge and time constant labels
        self.view.maximum_charge_label.setText(f"{max_charge:}") # update the maximum charge label 
        self.view.time_constant_label.setText(f"{time_constant:}") # update the time constant label 

        # Plot the charge as a function of time 
        self.plot_charge_curve(charge_function, max_charge, xmin, xmax)


    def plot_charge_curve(self, charge_function, max_charge, xmin, xmax):
        # Generate the data for the charge curve
        time_data = np.linspace(xmin, xmax, 100)
        charge_data = charge_function(time_data) 
        max_charge_data = np.full_like(time_data, max_charge)

        # Plot the charge curve
        self.view.ax.clear()  # Clear the current plot
        self.view.ax.plot(time_data, charge_data, label="Capacitor Charge")
        self.view.ax.plot(time_data, max_charge_data, label="Maximum Charge")

        # Update the plot labels
        self.view.ax.set_title("Capacitor Charge vs. Time", pad=20)
        self.view.ax.set_xlabel("Time", labelpad=5)
        self.view.ax.set_ylabel("Charge", labelpad=10)
        self.view.ax.legend()
        self.view.canvas.draw()

    def show_error(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()


    def submit(self):
        # Validate the user input
        inputs = self.get_user_input()
        if inputs is None:
            return

        # Get the user inputs 
        capacitance, resistance, input_voltage = inputs

        # Create a new model with the user inputs
        rc_circuit_model = RCCircuitModel(capacitance, resistance, input_voltage)

        # Update the view with the new model values
        self.update_view(rc_circuit_model)



