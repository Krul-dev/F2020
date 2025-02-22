#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:24:45 2025

@author: raul
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import function_series as fs
import population_growth_model as pgm
from taylor_series import taylor_function as term_function


def get_user_input():
    while True:
        try:
            lambda_value = float(input("\nIngrese la taza de crecimiento poblacional: "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    while True:
        try:
            first_coefficient_value=float(input("Ingrese la población inicial (que corresponde al tiempo inicial x=0): "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    while True:
        try:
            xmin=float(input("Ingrese el valor mínimo de la variable independiente x (que corresponde al tiempo): "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")
            
    while True:
        try:
            xmax=float(input("Ingrese el valor máximo de la variable independiente x (que corresponde al tiempo): "))
            if xmax > xmin:
                break
            else:
                print("\n Entrada inválida. Por favor ingrese un número mayor of igual al valor mínimo de x.\n")            
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    while True:
        try:
            number_of_coefficients=int(input("Ingrese el número de coeficientes que se utilizarán en la aproximación en series de Taylor: "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    return (lambda_value,first_coefficient_value,xmin,xmax,number_of_coefficients)

def graph_generated_function(f,lambda_value,first_coefficient_value,xmin,xmax,number_of_coefficients):
    #Generate the required data to graph the constructed function
    xdata = np.linspace(xmin, xmax, (math.floor(xmax-xmin))*50)
    ydata_approximated = f(xdata)
    ydata_exact=first_coefficient_value*np.exp(lambda_value*xdata)

    #print(xdata, ydata_approximated, ydata_exact)
    #Generate the corresponding plot
    fig, (ax_approximated,ax_exact)=plt.subplots(1,2,figsize=(10,4.5))
    fig.suptitle("Comparación del modelo de población aproximado contra el modelo exacto")

    ax_approximated.set_title("Modelo aproximado")
    ax_approximated.set_xlabel("x")
    ax_approximated.set_ylabel("y")
    ax_approximated.plot(xdata, ydata_approximated,label=f"\n $y=T_{{{number_of_coefficients}}}f(x)$\n")
    ax_approximated.legend(loc='upper left')

    ax_exact.set_title("Modelo exacto")
    ax_exact.set_xlabel("x")
    ax_exact.set_ylabel("y")
    ax_exact.plot(xdata, ydata_exact,label="\n $y=f(x)$\n")
    ax_exact.legend(loc='upper left')

    fig.subplots_adjust(top=0.84,hspace=0.5, wspace=0.3)
    plt.pause(0.1)




def main():
    print("""
¡Bienvenido!
Este script te ayudará a generar un modelo para el crecimiento poblacional a partir de cierto parámetros.""")

    while True:
        # Present options to the user
        choice=input("""
Indique lo que desea hacer:
    1. Introducir parámetros.
    2. Salir del programa.\n\n""")

        if choice =="1":
            # Handle the case where the user wants to enter data and generate the population growth model
            
            #Get user input
            (lambda_value,first_coefficient_value,xmin,xmax,number_of_coefficients)=get_user_input()

            #Contruct the required function using the data entered by the user 
            coefficient_list=pgm.generate_population_growth_coefficients(number_of_coefficients, lambda_value,first_coefficient_value)
            f=fs.generate_function_series(coefficient_list, term_function)
            
            #Generate the corresponding plot
            graph_generated_function(f,lambda_value,first_coefficient_value,xmin,xmax,number_of_coefficients)
             
        elif choice == "2":
            # Handle the case where the user wants to exit
            print("\nSaliendo del programa.")
            break  # Break the loop and exit the program
        else:
            # Handle invalid input
            print("\nSu respuesta no es válida, por favor elija las opciones 1 o 2.")


if __name__ == "__main__":
    main()