#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

import matplotlib 
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
import numpy as np 

def graph_generated_function(f,xmin,xmax,number_of_required_coefficients):
    #Generate the required data to graph the constructed function
    xdata = np.linspace(xmin, xmax, int(np.max([1,np.floor(xmax-xmin)])*50))
    ydata = f(xdata)

    #Generate the figure and the axis to plot the data
    fig, ax=plt.subplots(figsize=(10,4.5))

    #Plot the data and set the title and labels of the graph 
    ax.plot(xdata, ydata,label=f"\n $y=f(x)$\n")
    ax.set_title(f"Modelo aproximado utilizando {number_of_required_coefficients} coeficientes", pad=15)
    ax.set_xlabel("x", labelpad=15)
    ax.set_ylabel("y", labelpad=10)
    ax.legend(loc='upper left')

    #Adjust the layout of the graph and display it
    #fig.subplots_adjust(top=0.84,hspace=0.5, wspace=0.3)
#    plt.pause(0.1)
#    plt.show()
    plt.tight_layout()
    plt.show(block=False)

