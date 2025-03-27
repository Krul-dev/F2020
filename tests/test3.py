#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-27
Description: 
"""
import numpy as np 

import matplotlib.pyplot as plt 



x = np.linspace(-10, 10, 1000)
y1 = np.sin(x) 
y2 = np.cos(x)


lines=plt.plot(x, y1,x, y2)

lines[0].set_label('sin(x)')
lines[1].set_label('cos(x)')

plt.legend()
plt.title('Plot with Multiple NaN Gaps')
plt.show()

