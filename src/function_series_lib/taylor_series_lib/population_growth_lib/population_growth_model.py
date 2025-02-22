#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=import-error
"""
Created on Wed Jan 29 20:00:53 2025

@author: raul
"""


import numpy as np
from scipy.special import factorial

def generate_population_growth_coefficients(number_of_coefficients,lambda_value,first_coefficient_value):
    k=np.arange(number_of_coefficients)
    population_growth_coefficient_list=first_coefficient_value*(np.power(lambda_value,k)/factorial(k))
    return population_growth_coefficient_list
    