import Cell as cell
import Automata as automata

from Neighborhoods import Neighborhoods
from Borders import Borders

from celula.transition_rule import transition_rule
from celula.States import States as s

from automata.initial_state import initial_state





def statistic_1_function(c):
    if c.state == s.Ardiendo:
        return True
    else:
        return False


# cuadrado  Moore
# rombo     von_Neumann
if __name__ == '__main__':   
    
    

    a = automata.Automata(width=10, height=5, store_trace_back=True)

    a.set_border(Borders.FIXED, s.Ignifugo)

    a.set_neighborhood(Neighborhoods.MOORE)

    a.set_initial_state(initial_state)
    a.set_transition_rule(transition_rule)

    id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])

# Imprime las iteraciones
    print(a.actual_iteration)
    for row in a.get_matrix_state():
        print( row )
    print()
    for i in range(0, 4):
        a.next()
        print(a.actual_iteration)
        for row in a.get_matrix_state():
            print( row )
        print()


    a.store_data_in_json()
