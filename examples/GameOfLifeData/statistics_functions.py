
def statistic_function_count_30_iterations(cell):
    return ( ((cell.automata.actual_iteration % 30) == 0) and 
        (cell.get_variable('resurrecciones') != 0) )


statistics_message = {
    'statistic_function_count_30_iterations': 'Numero de resurrecciones',
}

statistics_variables = {
    'statistic_function_count_30_iterations': ['resurrecciones'],
}

