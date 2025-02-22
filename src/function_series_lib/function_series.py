#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:30:41 2025

@author: raul
"""

def generate_function_series(coefficient_list, term_function):
    def f(x):
        y=0
        for k in range(len(coefficient_list)):
            y+=coefficient_list[k]*term_function(k,x)
        return y
    return f