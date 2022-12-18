import Cell as cell
from States import States as s



def transition_rule(c:cell):
    if c.get_state() == s.Vivo:
        return s.Moribundo

    elif c.get_state() == s.Moribundo:
        return s.Muerto

    else: # c.get_state() == s.Muerto
        if c.count_neighbors_with_state(s.Vivo) == 2:
            return s.Vivo
        else:
            return s.Muerto



    




# Todas las celulas en estado Vivo pasan al estado Moribundo
# Todas las celulas en Moribundo Vivo pasan al estado Muerto
# Una celula en estado Muerto pasa al estado Vivo si tiene 2 vecinos en estado Vivo
