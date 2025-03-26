#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""

from taylor_coefficients._taylor_coefficients_formulas import (
        Analytic_Function, 
        Taylor_Coefficient_Function,
        )


from function_series import (
        generate_function_series
        )

from function_series import taylor_function as term_function
        


# Define the functions to compute the dependent variables



# Function to generate the Taylor approximation function 
def generate_taylor_approximation_function(taylor_coefficient_function, number_of_required_coefficients):
    # Adjust the initial coefficient list 
    coefficient_list = [taylor_coefficient_function(k) for k in range(number_of_required_coefficients)]
    taylor_approximation_function = generate_function_series(coefficient_list, term_function)
    return taylor_approximation_function 


# Define the TaylorCoefficientsModel class 
class TaylorCoefficientsModel:
    def __init__(self, xmin, xmax, number_of_required_coefficients):
       # Set the default values for the time range and the x-axis limits
        self.xmin = xmin     
        self.xmax = xmax
        self.number_of_required_coefficients = number_of_required_coefficients
        self.taylor_approximation_function = generate_taylor_approximation_function(Taylor_Coefficient_Function, number_of_required_coefficients)
        self.analytic_function = Analytic_Function
    # Define the methods to get the x-axis limits 
    def get_xmin(self):
        return self.xmin 

    def get_xmax(self): 
        return self.xmax 

    def get_number_of_required_coefficients(self):
        return self.number_of_required_coefficients

    def get_taylor_approximation_function(self):
        return self.taylor_approximation_function
