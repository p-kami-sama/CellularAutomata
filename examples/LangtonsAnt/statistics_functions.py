import Cell as cell

from States import States



statistics_message = {

    'has_ant': 'Hormiga',
}

statistics_variables = {
    'has_ant': ['orientacion_hormiga', 'colorBlanco'],
}

def has_ant(c:cell):
    return c.get_state() == States.Hormiga
