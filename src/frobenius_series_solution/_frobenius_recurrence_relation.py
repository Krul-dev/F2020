#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

R_INDEX = 1
NUMBER_OF_INITIAL_COEFFICIENTS = 1
NUMBER_OF_EXTRA_COEFFICIENTS = 1 

def recurrence_relation(k,required_coefficient_list):
    next_coefficient = -(required_coefficient_list[0])/(k * (k + 2))
    return next_coefficient

