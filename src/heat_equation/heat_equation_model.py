#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""
import numpy as np

from heat_equation._heat_equation_coefficients_formulas import (
        Heat_Coefficient_Function,
        )


from function_series import (
        generate_function_series,
        generate_fourier_function
        )


fourier_function = generate_fourier_function(1)

def heat_term_function(k, xt ):
    x, t = xt 
    u = np.exp(-(k*(np.pi**2)*t)) * fourier_function(k, x) 
    return u
        


# Define the functions to compute the dependent variables



# Function to generate the Heat approximation function 
def generate_heat_approximation_function(heat_coefficient_function, number_of_required_coefficients):
    # Adjust the initial coefficient list 
    coefficient_list = [heat_coefficient_function(k) for k in range(number_of_required_coefficients)]
    heat_approximation_function = generate_function_series(coefficient_list, heat_term_function)
    return heat_approximation_function 


# Define the HeatEquationModel class 
class HeatEquationModel:
    def __init__(self, tmin, tmax, number_of_required_coefficients):
       # Set the default values for the time range and the x-axis limits
        self.tmin = tmin     
        self.tmax = tmax
        self.number_of_required_coefficients = number_of_required_coefficients
        self.heat_approximation_function = generate_heat_approximation_function(Heat_Coefficient_Function, number_of_required_coefficients)
        def initial_heat_approximation_function(x):
            return self.heat_approximation_function((x,0))
        self.initial_heat_approximation_function = initial_heat_approximation_function 

    # Define the methods to get the x-axis limits 
    def get_tmin(self):
        return self.tmin 

    def get_tmax(self): 
        return self.tmax 

    def get_number_of_required_coefficients(self):
        return self.number_of_required_coefficients

    def get_heat_approximation_function(self):
        return self.heat_approximation_function

    def get_initial_heat_approximation_function(self):
        return self.initial_heat_approximation_function

     
