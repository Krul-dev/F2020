#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""

# Function to get user input
def get_user_input(number_of_initial_coefficients):
    while True:
        try:
            xmin=float(input("Ingrese el valor mínimo de la variable independiente x: "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")
            
    while True:
        try:
            xmax=float(input("Ingrese el valor máximo de la variable independiente x: "))
            if xmax > xmin:
                break
            else:
                print("\n Entrada inválida. Por favor ingrese un número mayor al valor mínimo de x.\n")            
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")
    
    initial_coefficient_list=[]
    for i in range(number_of_initial_coefficients):
        while True:
            try:
                next_coefficient=float(input(f"Ingrese el valor del coeficiente c_{i}: "))
                initial_coefficient_list.append(next_coefficient)
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")

    while True:
        try:
            number_of_required_coefficients=int(input("Ingrese el número de coeficientes que se utilizarán en la aproximación en series de funciones: "))
            if number_of_required_coefficients >= number_of_initial_coefficients:
                break
            else:
                print("\n Entrada inválida. Por favor ingrese un número mayor al número de coeficientes iniciales.\n")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    return (xmin,xmax,initial_coefficient_list,number_of_required_coefficients)


