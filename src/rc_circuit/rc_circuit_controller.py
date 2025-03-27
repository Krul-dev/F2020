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
from matplotlib.animation import FuncAnimation


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
        self.animate_charge_curve(charge_function, max_charge, xmin, xmax)






    def animate_charge_curve(self, charge_function, max_charge, xmin, xmax):
        # Set the rate in Frames Per Second (FPS) and partition the time interval into the total number of frames
        FPS = 60  # Frames per Second
        time_interval = (xmax - xmin)  # Total time interval
        frame_interval =1000 / FPS  # Time interval between frames   
        number_of_frames = int((xmax - xmin) * FPS)  # Total number of frames to animate 
        frames=range(number_of_frames)



        # Generate the data for the charge curve
        time_data = np.linspace(xmin, xmax, number_of_frames)  # Time data for the charge curve
        charge_data = charge_function(time_data)               # Charge data for the charge curve 
        max_charge_data = np.full_like(time_data, max_charge)  # Maximum charge data for the charge curve 

        # Set up the lines for the charge curve and the maximum charge curve 
        self.view.ax.clear()  # Clear the current plot 
        lines=self.view.ax.plot([], [], [], [], lw=2)
        lines[0].set_label("Capacitor Charge")
        lines[1].set_label("Maximum Charge")

        # Animate the charge curve
        def animate(frame):
            lines[0].set_data(time_data[:frame], charge_data[:frame])
            lines[1].set_data(time_data[:frame], max_charge_data[:frame])
            return lines

        # Create the animation
        animation = FuncAnimation(self.view.fig, animate, frames=frames, interval=frame_interval, blit=False)


        # Update the axis information
        self.view.ax.set_xlim(xmin-time_interval*0.1, xmax+time_interval*0.1)       # Set the x-axis limits
        self.view.ax.set_ylim(-max_charge*0.1, max_charge*1.1)                      # Set the y-axis limits 
        self.view.ax.set_title("Capacitor Charge vs. Time", pad=20)                 # Set the plot title
        self.view.ax.set_xlabel("Time", labelpad=5)                                 # Set the x-axis label
        self.view.ax.set_ylabel("Charge", labelpad=10)                              # Set the y-axis label
        self.view.ax.legend(loc="lower right")                                      # Set the legend location

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



