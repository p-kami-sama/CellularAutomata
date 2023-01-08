import Cell as cell
from States import States as s



def transition_rule(c:cell):
    if c.get_state() == s.Night and (c.count_neighbors_with_state(s.Day) in [3, 6, 7, 8]):
        return s.Day

    elif c.get_state() == s.Day and (c.count_neighbors_with_state(s.Day) in [3, 4, 6, 7, 8]):
        return s.Day

    else:
        return s.Night





# Night cell becomes Day (is born) if it has 3, 6, 7, or 8 Day neighbors,
#  a Day cell remains Day (survives) if it has 3, 4, 6, 7, or 8 Day neighbors
#  else -> Night
    

