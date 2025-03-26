#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

import numpy as np

def generate_function_series(coefficient_list, term_function):
    def f(x):
        y=0
        for k in range(len(coefficient_list)):
            y+=coefficient_list[k]*term_function(k,x)
        return y
    return f


def adjust_initial_coefficient_list(initial_coefficient_list,number_of_extra_coefficients):
    extra_coefficient_list=[0]*number_of_extra_coefficients
    adjusted_initial_coefficient_list=extra_coefficient_list+initial_coefficient_list
    return adjusted_initial_coefficient_list



def generate_coefficient_list(recurrence_relation,adjusted_initial_coefficient_list,number_of_required_coefficients,number_of_extra_coefficients):
    #initialize coefficient_list and set up the number of initial coefficients
    extended_coefficient_list = adjusted_initial_coefficient_list.copy()
    number_of_adjusted_initial_coefficients = len(adjusted_initial_coefficient_list)
    number_of_initial_coefficients = number_of_adjusted_initial_coefficients - number_of_extra_coefficients
    
    #generate the remaining coefficients and append them to the coefficient_list
    for k in range(number_of_required_coefficients - number_of_initial_coefficients):
        next_coefficient=recurrence_relation(k + number_of_initial_coefficients, 
        extended_coefficient_list[k:k + number_of_initial_coefficients])
        extended_coefficient_list.append(next_coefficient)
    
    return extended_coefficient_list




def taylor_function(k,x):
    return np.power(x,k)

def generate_frobenius_function(r):
    def f(k,x):
      return np.power(x,k+r)
    return f

def generate_fourier_function(l):
    def f(k,x):
      return np.sin((k * np.pi * x)/l)
    return f


