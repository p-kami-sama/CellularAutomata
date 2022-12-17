import Cell as cell

from States import States



statistics_message = {
    'statistic_function_count_30_iterations': 'Resurrecciones',
}

statistics_variables = {
    'statistic_function_count_30_iterations': ['resurrecciones'],
}

def statistic_function_count_30_iterations(c:cell):
    return ( (c.automata.actual_iteration % 30) == 0)