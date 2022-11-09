import Cell as cell
import Automata as automata

from Neighborhoods import Neighborhoods
from Borders import Borders

from celula.transition_rule import transition_rule
from celula.States import States as s

from automata.initial_state import initial_state

'''
    ['0', '0', '0', '4', '0', '0', '4', '4', '1', '1', '5', '2']
    con frontera von_neumann y radio 2
    0 -> 5 (izq o arriba)
    1 -> 2 (der)
    4 -> 3 (abajo)
    5 -> (esquina abajo derecha)
'''



inicial_1 =[
        [{'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}],
        [{'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}],
        [{'state': 'M'}, {'state': 'V'}, {'state': 'V'}, {'state': 'V'}, {'state': 'M'}],
        [{'state': 'M'}, {'state': 'V'}, {'state': 'M'}, {'state': 'V'}, {'state': 'ZZ', 'variables':['sol', 'luna']}],
        [{'state': 'M'}, {'state': 'V'}, {'state': 'V'}, {'state': 'V'}, {'state': 'YY'}],
        [{'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}],
        [{'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}, {'state': 'M'}]
    ]


def func_t(c: cell):
    if c.state == 'V':
        return 'M'
    elif c.state == 'M':
        return 'v'
    else:
        return 'AAAAA'









def statistic_1_function(c):
    if c.state == s.Ardiendo:
        return True
    else:
        return False


# cuadrado  Moore
# rombo     von_Neumann
if __name__ == '__main__':   
    
    

    a = automata.Automata(width=10, height=5, store_trace_back=True)    #   , neighborhood='von_Neumann', border='adiabatic'


    a.set_border(Borders.FIXED, s.Ignifugo)

    a.set_neighborhood(Neighborhoods.MOORE)

    a.set_initial_state(initial_state)
    a.set_transition_rule(transition_rule)

    id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])

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
