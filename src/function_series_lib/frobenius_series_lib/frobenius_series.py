#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:43:47 2025

@author: raul
"""
import numpy as np

def frobenius_function(r):
    def f(k,x):
      return np.power(x,k+r)
    return f
