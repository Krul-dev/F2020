#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

from numpy import exp, sin, cos, log, abs, sqrt, random 
from scipy.special import factorial



def Wave_Coefficient_Function(k):
    c_k = ((5**k) * random.uniform(-1, 1))/factorial(k)
    return c_k
