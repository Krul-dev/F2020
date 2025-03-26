#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""
from PyQt6.QtWidgets import QMessageBox
import numpy as np

from frobenius_series_solution.frobenius_series_model import FrobeniusSeriesModel
from frobenius_series_solution.frobenius_series_view import FrobeniusSeriesView
from frobenius_series_solution._frobenius_recurrence_relation import NUMBER_OF_INITIAL_COEFFICIENTS

# Controller class for the application
class FrobeniusSeriesController:
    # Define the constructor
    def __init__(self, view : FrobeniusSeriesView):
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
            xmin = float(self.view.xmin_line_edit.text())
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None

        try:
            xmax= float(self.view.xmax_line_edit.text())
            if xmax <= xmin:
                self.show_error("Entrada inválida", "El valor de máximo de x debe ser mayor que el valor mínimo de x.")
                return None 
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None

        try:
            initial_coefficient_list = [float(self.view.coefficient_inputs[k].text()) for k in range(NUMBER_OF_INITIAL_COEFFICIENTS)]
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.") 
            return None

        try:
            number_of_required_coefficients = int(self.view.number_of_required_coefficients_line_edit.text())
            if number_of_required_coefficients < NUMBER_OF_INITIAL_COEFFICIENTS:
                self.show_error("Entrada inválida", f"El número de coeficientes requeridos debe ser mayor o igual a {NUMBER_OF_INITIAL_COEFFICIENTS}.")
                return None
        except ValueError:
            self.show_error("Entrada inválida", "Por favor ingrese un número válido.")
            return None


       
        return xmin, xmax, initial_coefficient_list, number_of_required_coefficients
   

    # Subroutine to update the view with the model values
    def update_view(self,frobenius_series_model):
        # Update the view with the current model values 
        # Get the results from the model 
        xmin = frobenius_series_model.get_xmin()
        xmax = frobenius_series_model.get_xmax()
        number_of_required_coefficients = frobenius_series_model.get_number_of_required_coefficients()
        frobenius_approximation_function = frobenius_series_model.get_frobenius_approximation_function()
        

        # Plot the charge as a function of time 
        self.plot_frobenius_approximation_function(frobenius_approximation_function, xmin, xmax, number_of_required_coefficients)


    def plot_frobenius_approximation_function(self, frobenius_approximation_function, xmin, xmax, number_of_required_coefficients):
        # Generate the data for the charge curve
        x_data = np.linspace(xmin, xmax, 1000)
        y_data= frobenius_approximation_function(x_data) 

        # Plot the charge curve
        self.view.ax.clear()  # Clear the current plot
        self.view.ax.plot(x_data, y_data, label=fr"$y = F_{{{number_of_required_coefficients-1}}}f(x)$")



        # Update the plot labels
        self.view.ax.set_title(fr"Gráfica de la solución obtenida utilizando series de Frobenius con ${number_of_required_coefficients}$ coeficientes", pad=20)
        self.view.ax.set_xlabel("x", labelpad=10)
        self.view.ax.set_ylabel("y", labelpad=10)
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
        xmin, xmax, initial_coefficient_list, number_of_required_coefficients = inputs

        # Create a new model with the user inputs
        frobenius_series_model = FrobeniusSeriesModel(xmin, xmax, initial_coefficient_list, number_of_required_coefficients)

        # Update the view with the new model values
        self.update_view(frobenius_series_model)



