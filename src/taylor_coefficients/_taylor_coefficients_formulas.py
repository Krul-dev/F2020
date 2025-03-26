#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

from numpy import exp, sin, cos, log, abs, sqrt 
from scipy.special import factorial


def Analytic_Function(x):
    y= exp(x)
    return y

def Taylor_Coefficient_Function(k):
    c_k = 1/factorial(k)
    return c_k
