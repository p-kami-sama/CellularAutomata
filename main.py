
import sys
import csv

# IMPORTS
import Automata as automata

from celula.transition_rule import transition_rule_GameOfLife
from celula.States import States
from celula.statistics_functions import *

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders
from automata.initial_state import initial_state_GameOfLife

# para colores
# from QgsData.states_color_dict import states_color_dict


# ruta



#Se inicializa QgsAutomata
print('se inicia el automata')


# cuadrado  Moore
# rombo     von_Neumann

a = automata.Automata(width=10, height=5, store_trace_back=True)
a.set_border(Borders.FIXED, States.Muerto)
a.set_neighborhood(Neighborhoods.MOORE)
a.set_initial_state(initial_state_GameOfLife)
a.set_transition_rule(transition_rule_GameOfLife)
id = a.add_statistic( statistic_function_revived_cell, 'Ha vuelto a la vida.', [])

print('id', id)

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




# a.run_iterations(2, True)
a.store_data_in_json()


print('\nFINAL\n')



# funciona con el States.Ardiendo.name
# print(str(States.Ardiendo) == 'Ardiendo')



gol = automata.Automata(10, 10, True)
gol.set_border(Borders.FIXED, States.Muerto)
gol.set_neighborhood(Neighborhoods.MOORE, 1)
gol.set_initial_state(initial_state_GameOfLife)
gol.set_transition_rule(transition_rule_GameOfLife)

gol.run_iterations(3, True)