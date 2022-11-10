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