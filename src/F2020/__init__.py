# __init__.py
# This file makes the F2020 directory a package
# You can optionally import key functions or variables here
__version__ = "0.1.0"

from ._input_handler import get_user_input
from ._output_handler import graph_generated_function
from ._taylor_recurrence_relation import NUMBER_OF_INITIAL_COEFFICIENTS, NUMBER_OF_EXTRA_COEFFICIENTS, recurrence_relation
from .function_series import adjust_initial_coefficient_list, generate_coefficient_list, generate_function_series, taylor_function as term_function

