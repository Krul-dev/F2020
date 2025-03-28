#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""
from PyQt6.QtWidgets import QMessageBox
import numpy as np

from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection

from wave_equation.wave_equation_model import WaveEquationModel
from wave_equation.wave_equation_view import WaveEquationView


# Define the colormap for the plot 
colors = [(0, 1, 1), (0, 0, 0), (1, 0, 0)] # Cyan -> Black -> Red
cmap = mcolors.LinearSegmentedColormap.from_list("CustomRedCyan", colors)



# Controller class for the application
class WaveEquationController:
    # Define the constructor
    def __init__(self, view : WaveEquationView):
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
            tmin = 0
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None

        try:
            tmax= float(self.view.xmax_line_edit.text())
            if tmax <= tmin:
                self.show_error("Entrada inválida", "El tiempor final debe ser mayor que el tiempo inicial.") 
                return None 
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None

        try:
            number_of_required_coefficients = int(self.view.number_of_required_coefficients_line_edit.text())
            if number_of_required_coefficients < 0:
                self.show_error("Entrada inválida", f"El número de coeficientes requeridos debe ser mayor o igual a 0.")
                return None
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None


       
        return tmin, tmax, number_of_required_coefficients
   

    # Subroutine to update the view with the model values
    def update_view(self,wave_equation_model):
        # Update the view with the current model values 
        # Get the results from the model 
        tmin = wave_equation_model.get_tmin()
        tmax = wave_equation_model.get_tmax()
        number_of_required_coefficients = wave_equation_model.get_number_of_required_coefficients()
        wave_approximation_function = wave_equation_model.get_wave_approximation_function()
        initial_wave_approximation_function = wave_equation_model.get_initial_wave_approximation_function()

        # Plot the charge as a function of time 
        self.animate_wave_approximation_function(wave_approximation_function, initial_wave_approximation_function, tmin, tmax)






    def animate_wave_approximation_function(self, wave_approximation_function,  initial_wave_approximation_function, tmin, tmax):
        alpha=initial_wave_approximation_function 
        f=wave_approximation_function

        # Generate the data for the charge curve
        x_data = np.linspace(0, 1,350)
        y_data = np.zeros_like(x_data)
        z_data=np.array([alpha(x_data[k]) for k in range(len(x_data)-1)])

        # Plot the wave approximation curve
        self.view.ax.clear()  # Clear the current plot
        self.view.ax.set_title("Aproximación de la ecuación de calor")
        bound = 10
        norm = mcolors.Normalize(vmin=-bound, vmax=bound)
        segments = [np.array([[x_data[k], y_data[k]], [x_data[k+1], y_data[k+1]]]) 
            for k in range(len(x_data)-1)]
        line_collection = LineCollection(segments, cmap=cmap, norm=norm, lw=10)
        line_collection.set_array(z_data) # Set initial colors
        self.view.ax.add_collection(line_collection)
        self.view.ax.set_xlim(0, 1)
        self.view.ax.set_ylim(-1, 1)
        self.view.ax.axis("off")

        if not hasattr(self, 'colorbar') or self.colorbar is None:
            self.colorbar = self.view.fig.colorbar(line_collection, ax=self.view.ax, label="Temperatura")

        def update(frame):
            dynamic_colors = np.array([f((x_data[k], frame/1000)) for k in range(len(x_data)-1)])
            line_collection.set_array(dynamic_colors)
            return line_collection,

        FPS = 60
        interval = 1000/FPS # Interval in milliseconds
        frames = int((tmax-tmin)*FPS)

        self.wave_animation = FuncAnimation(self.view.fig, update, frames=frames, interval=interval, blit=False)

 
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
        xmin, xmax, number_of_required_coefficients = inputs

        # Create a new model with the user inputs
        wave_equation_model = WaveEquationModel(xmin, xmax, number_of_required_coefficients)

        # Update the view with the new model values
        self.update_view(wave_equation_model)



