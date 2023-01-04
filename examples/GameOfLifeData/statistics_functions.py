import Cell as cell



def statistic_function_count_30_iterations(c:cell):
    return ( ((c.automata.actual_iteration % 30) == 0) and (c.get_variable('resurrecciones') != 0))


statistics_message = {
    'statistic_function_count_30_iterations': 'Numero de resurrecciones',
}


statistics_variables = {
    'statistic_function_count_30_iterations': ['resurrecciones'],
}

