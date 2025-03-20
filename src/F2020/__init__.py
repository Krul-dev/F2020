# src/F2020/__init__.py

# Importing constants and functions for public use
from ._taylor_recurrence_relation import (
    NUMBER_OF_INITIAL_COEFFICIENTS,
    NUMBER_OF_EXTRA_COEFFICIENTS,
    recurrence_relation,
)

from .function_series import (
    adjust_initial_coefficient_list,
    generate_coefficient_list,
    generate_function_series,
    taylor_function as term_function,
)

from ._input_handler import get_user_input
from ._output_handler import graph_generated_function

# Define public API
__all__ = [
    "NUMBER_OF_INITIAL_COEFFICIENTS",
    "NUMBER_OF_EXTRA_COEFFICIENTS",
    "recurrence_relation",
    "adjust_initial_coefficient_list",
    "generate_coefficient_list",
    "generate_function_series",
    "term_function",
    "get_user_input",
    "graph_generated_function",
]

