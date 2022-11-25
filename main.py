
import sys
import csv


# IMPORTS
import Automata as automata
import InteractiveAutomata as interactiveAutomata

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

# a = automata.Automata(width=10, height=5, store_trace_back=True)
# a.set_border(Borders.FIXED, States.Muerto)
# a.set_neighborhood(Neighborhoods.MOORE)
# a.set_initial_state(initial_state_GameOfLife)
# a.set_transition_rule(transition_rule_GameOfLife)
# id = a.add_statistic( statistic_function_revived_cell, 'Ha vuelto a la vida.', [])







# a.run_iterations(2, True)
# a.store_data_in_json()






# funciona con el States.Ardiendo.name
# print(str(States.Ardiendo) == 'Ardiendo')




ia = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_state=None)


ia.set_border(Borders.FIXED, States.Muerto)
ia.set_neighborhood(Neighborhoods.MOORE, 1)
# ia.set_initial_state(initial_state_GameOfLife)
ia.set_initial_state_from_image_and_csv()
ia.set_transition_rule(transition_rule_GameOfLife)


# Imprime las iteraciones
# print('actual_iteration', ia.actual_iteration)
# print(ia.actual_iteration, ia.last_iteration_calculated)
# for row in ia.get_matrix_state():
#     print( row )
# print()
# ia.run_iterations(1, True)
# for i in range(0, 2):
#     ia.next()
#     print(ia.actual_iteration)
#     for row in ia.get_matrix_state():
#         print( row )
#     print()

for x in range(1,6):
    ia.next_image_iteration()

for x in range(1,4):
    ia.back()

for x in range(1,3):
    ia.next_image_iteration()


print(ia.last_iteration_calculated)

# print('it 0:\n', ia.iterations[0])
# print('\nit 1:\n', ia.iterations[1])

print('\nFINAL\n')
