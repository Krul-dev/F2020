#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-22
Description: 
"""

import numpy as np


# Define the functions to compute the dependent variables

# Function to compute the max charge 
def compute_max_charge(capacitance, input_voltage):
    C = capacitance 
    epsilon = input_voltage 
    max_charge = epsilon * C
    return max_charge

# Function to compute the time constant 
def compute_time_constant(capacitance, resistance):
    C = capacitance 
    R = resistance 
    time_constant = R * C 
    return time_constant

# Function to generate the charge function 
def generate_charge_function(capacitance, resistance, input_voltage):
    def charge_function(time):
        C = capacitance
        R = resistance
        epsilon = input_voltage
        t = time
        charge = epsilon * C * (1 - np.exp(-t / (R * C)))
        return charge
    return charge_function


# Define the RCCircuitModel class 
class RCCircuitModel:
    def __init__(self, capacitance, resistance, input_voltage):
        # Set the values of the capacitance, resistance, and input voltage (Independent variables)
        self.capacitance = capacitance 
        self.resistance = resistance
        self.input_voltage = input_voltage

        # Calculate the max charge, time constant and charge function (Dependent variables)
        self.max_charge = compute_max_charge(capacitance, input_voltage)
        self.time_constant = compute_time_constant(capacitance, resistance)
        self.charge_function = generate_charge_function(capacitance, resistance, input_voltage)

        # Set the default values for the time range and the x-axis limits
        self.xmin = 0 
        self.xmax = 5 * self.time_constant

    # Define the methods to get the dependent variables
    def get_max_charge(self):
        return self.max_charge

    def get_time_constant(self):
        return self.time_constant

    def get_charge_function(self):
        return self.charge_function 

    # Define the methods to get the x-axis limits 
    def get_xmin(self):
        return self.xmin 

    def get_xmax(self): 
        return self.xmax 

