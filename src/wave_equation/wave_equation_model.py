#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""
import numpy as np

from wave_equation._wave_equation_coefficients_formulas import (
        Wave_Position_Coefficient_Function,
        Wave_Velocity_Coefficient_Function
        )


from function_series import (
        generate_function_series,
        generate_fourier_function
        )


fourier_function = generate_fourier_function(1)

def wave_position_term_function(k, xt ):
    x, t = xt 
    u =  np.cos(k* np.pi* t)* fourier_function(k, x) 
    return u
        
def wave_velocity_term_function(k, xt):
    x, t = xt 
    u = np.sin(k* np.pi* t)* fourier_function(k, x) 
    return u

# Define the functions to compute the dependent variables



# Function to generate the Wave approximation function 
def generate_wave_approximation_function(wave_position_coefficient_function, wave_velocity_coefficient_function ,number_of_required_coefficients):
    # Adjust the initial coefficient list 
    position_coefficient_list = [wave_position_coefficient_function(k) for k in range(number_of_required_coefficients)]

    velocity_coefficient_list = [wave_velocity_coefficient_function(k) for k in range(number_of_required_coefficients)]

    wave_position_approximation_function = generate_function_series(position_coefficient_list, wave_position_term_function)
    wave_velocity_approximation_function = generate_function_series(velocity_coefficient_list, wave_velocity_term_function)
    def wave_approximation_function(x,t): 
        u = wave_position_approximation_function((x,t)) + wave_velocity_approximation_function((x,t))
        return u
    return wave_approximation_function 


# Define the WaveEquationModel class 
class WaveEquationModel:
    def __init__(self, number_of_required_coefficients):
       # Set the default values for the time range and the x-axis limits
        self.tmin = 0
        self.tmax = 2
        self.xmin = 0 
        self.xmax = 1
        self.number_of_required_coefficients = number_of_required_coefficients
        self.wave_approximation_function = generate_wave_approximation_function(Wave_Position_Coefficient_Function, Wave_Velocity_Coefficient_Function, number_of_required_coefficients)
        def initial_wave_approximation_function(x):
            return self.wave_approximation_function(x,0)
        self.initial_wave_approximation_function = initial_wave_approximation_function 

    # Define the methods to get the x-axis limits 
    def get_tmin(self):
        return self.tmin 

    def get_tmax(self): 
        return self.tmax 

    def get_xmin(self):
        return self.xmin

    def get_xmax(self):
        return self.xmax 

    def get_number_of_required_coefficients(self):
        return self.number_of_required_coefficients

    def get_wave_approximation_function(self):
        return self.wave_approximation_function

    def get_initial_wave_approximation_function(self):
        return self.initial_wave_approximation_function

     
