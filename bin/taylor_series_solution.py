#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-19
Description: 
"""
from _taylor_recurrence_relation import NUMBER_OF_INITIAL_COEFFICIENTS, NUMBER_OF_EXTRA_COEFFICIENTS, recurrence_relation

from function_series import adjust_initial_coefficient_list, generate_coefficient_list, generate_function_series
from function_series import taylor_function as term_function

from _input_handler import get_user_input
from _output_handler import graph_generated_function

def main():
    print("""
¡Bienvenido!
Este script te ayudará a generar una solución en series de Taylor
a la ecuación diferencial planteada y visualizar su gráfica.""")

    while True:
        # Present options to the user
        choice=input("""
Indique lo que desea hacer:
    1. Introducir parámetros.
    2. Salir del programa.\n\n""")

        if choice =="1":
            # Handle the case where the user wants to enter data and generate the population growth model
            
            #Get user input
            (xmin,xmax,initial_coefficient_list,number_of_required_coefficients)=get_user_input(NUMBER_OF_INITIAL_COEFFICIENTS)

            #Contruct the required function using the data entered by the user 
            adjusted_initial_coefficient_list=adjust_initial_coefficient_list(initial_coefficient_list,NUMBER_OF_EXTRA_COEFFICIENTS)
            coefficient_list=generate_coefficient_list(recurrence_relation, adjusted_initial_coefficient_list, number_of_required_coefficients)
            f=generate_function_series(coefficient_list, term_function)
            
            #Generate the corresponding plot
            graph_generated_function(f,xmin,xmax,number_of_required_coefficients)
             
        elif choice == "2":
            # Handle the case where the user wants to exit
            print("\nSaliendo del programa.")
            break  # Break the loop and exit the program
        else:
            # Handle invalid input
            print("\nSu respuesta no es válida, por favor elija las opciones 1 o 2.")


if __name__ == "__main__":
    main()
