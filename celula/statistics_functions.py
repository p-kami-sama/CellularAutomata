import Cell as cell
from .States import States


def statistic_1_function(c:cell):
    if c.state == States.Ardiendo:
        return True
    else:
        return False


def statistic_2_function(c:cell):
    if c.state == States.Ignifugo:
        return True
    else:
        return False

def statistic_function_revived_cell(c:cell):
    if c.state == States.Vivo and \
        (c.automata.get_cell(c.xpos, c.ypos, c.automata.actual_iteration -1).state == States.Muerto):
        return True
    else:
        return False