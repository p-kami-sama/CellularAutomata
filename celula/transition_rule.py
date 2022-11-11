import Cell as cell
from .States import States

def transition_rule(c:cell):

    if c.get_variable('Sol') != None:
        return {'state': States.Ignifugo, 'Sol': c.automata.actual_iteration}

    if c.state == States.Quemado or c.state == States.Ignifugo:
        return c.state
    elif c.state == States.Ardiendo:
        return States.Quemado
    elif c.state == States.Combustible and c.all_neighbours_has_state(States.Ardiendo):
        return States.Quemado
    elif  c.state == States.Combustible and c.any_neighbor_has_state(States.Ardiendo):
        return States.Ardiendo
    else:
        return c.state