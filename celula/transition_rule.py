import Cell as cell
from .States import States

def transition_rule(c:cell):
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

from .States import States as s

def transition_rule_GameOfLife(c:cell):
    if c.get_state() == s.Vivo:
        n = c.count_neighbors_with_state(s.Vivo)
        if n == 2 or n == 3:
            return s.Vivo
        else:
            return s.Muerto

    elif c.get_state() == s.Muerto:
        if  c.count_neighbors_with_state(s.Vivo) == 3:
            return s.Vivo
        else:
            return s.Muerto

# Una célula muerta con exactamente 3 células vecinas vivas "nace" (en el turno siguiente estará viva).
# Una célula viva con 2 o 3 células vecinas vivas sigue viva,
#     en otro caso muere (por "soledad" o "superpoblación").