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
    y = sin(x)
    return y


def Taylor_Coefficient_Function(k):
    if k % 2 == 0:
        c_k = 0
    else:
        c_k = ((-1)**((k - 1) / 2)) / factorial(k)
    return c_k
