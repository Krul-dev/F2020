# src/function_series/__init__.py

# Importing constants and functions for public use
from .function_series import (
    adjust_initial_coefficient_list,
    generate_coefficient_list,
    generate_function_series,
    taylor_function,
    generate_frobenius_function,
    generate_fourier_function
)

# Define public API
__all__ = [
    "adjust_initial_coefficient_list",
    "generate_coefficient_list",
    "generate_function_series",
    "taylor_function",
    "generate_frobenius_function",
    "generate_fourier_function"
]

