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

from wave_equation.wave_equation_model import WaveEquationModel
from wave_equation.wave_equation_view import WaveEquationView



import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams.update({
    'text.usetex': True,
    'font.size': 16,             # General font size
    'axes.titlesize': 20,        # Title font size
    'axes.labelsize': 18,        # X and Y label font size
    'xtick.labelsize': 14,       # X tick label font size
    'ytick.labelsize': 14,       # Y tick label font size
    'legend.fontsize': 14        # Legend font size
})


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

        try:
            number_of_required_coefficients = int(self.view.number_of_required_coefficients_line_edit.text())
            if number_of_required_coefficients < 0:
                self.show_error("Entrada inválida", f"El número de coeficientes requeridos debe ser mayor o igual a 0.")
                return None
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None


       
        return number_of_required_coefficients
   

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
        # Get the wave approximation function and the initial wave approximation function
        f=wave_approximation_function
        alpha=initial_wave_approximation_function 
        
        # Generate the data for the charge curve
        x_data = np.linspace(0, 1,350)
        u_initial_data = np.array([alpha(x) for x in x_data])

        # Plot the wave approximation curve
        self.view.ax.clear()  # Clear the current plot
        self.view.ax.set_title(r"\textbf{Aproximación de la ecuación de onda}", pad=20)
        self.view.ax.set_xlim(-0.1, 1.1)
        self.view.ax.set_xlabel(r"Posición", labelpad=7.5)
        self.view.ax.set_ylabel(r"Desplazamiento", labelpad=7.5)
        
        # Generate the initial wave approximation curve
        line,=self.view.ax.plot(x_data, u_initial_data, lw=2)

        # Define the animation data 
        FPS = 60
        interval = 1000/FPS # Interval in milliseconds
        frames = int((tmax-tmin)*FPS) 

        # Define the animation function
        def animate(frame):
            line.set_ydata([f(x_data[k], frame/60) for k in range(len(x_data))])
            return line,


        self.wave_animation = FuncAnimation(self.view.fig, animate, frames=frames, interval=interval, blit=False)

 
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
        number_of_required_coefficients = inputs

        # Create a new model with the user inputs
        wave_equation_model = WaveEquationModel(number_of_required_coefficients)

        # Update the view with the new model values
        self.update_view(wave_equation_model)



