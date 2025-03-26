#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""

import numpy as np

from taylor_series_solution._taylor_recurrence_relation import (
        NUMBER_OF_EXTRA_COEFFICIENTS,
        recurrence_relation 
        )

from function_series import (
        adjust_initial_coefficient_list,
        generate_coefficient_list,
        generate_function_series
        )

from function_series import taylor_function as term_function
        


# Define the functions to compute the dependent variables



# Function to generate the Taylor approximation function 
def generate_taylor_approximation_function(initial_coefficient_list, number_of_required_coefficients):
    # Adjust the initial coefficient list 
    adjusted_initial_coefficient_list = adjust_initial_coefficient_list(initial_coefficient_list, NUMBER_OF_EXTRA_COEFFICIENTS)
    extended_coefficient_list = generate_coefficient_list(recurrence_relation, adjusted_initial_coefficient_list, number_of_required_coefficients, NUMBER_OF_EXTRA_COEFFICIENTS) 
    coefficient_list = extended_coefficient_list[NUMBER_OF_EXTRA_COEFFICIENTS:]
    taylor_approximation_function = generate_function_series(coefficient_list, term_function)
    return taylor_approximation_function 


# Define the TaylorSeriesModel class 
class TaylorSeriesModel:
    def __init__(self, xmin, xmax, initial_coefficient_list, number_of_required_coefficients):
       # Set the default values for the time range and the x-axis limits
        self.xmin = xmin     
        self.xmax = xmax
        self.number_of_required_coefficients = number_of_required_coefficients
        self.taylor_approximation_function = generate_taylor_approximation_function(initial_coefficient_list, number_of_required_coefficients)

    # Define the methods to get the x-axis limits 
    def get_xmin(self):
        return self.xmin 

    def get_xmax(self): 
        return self.xmax 

    def get_number_of_required_coefficients(self):
        return self.number_of_required_coefficients

    def get_taylor_approximation_function(self):
        return self.taylor_approximation_function
