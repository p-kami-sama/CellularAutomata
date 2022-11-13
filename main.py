#from prueba_raster import gato
# from qgis.core import *

print(1)
import sys
print(2)
tools = "./celula/transition_rule.py" #variable#
print(3)
if not tools in sys.path:
    sys.path.append(tools)
print(4)

print(sys.path)




print(5)

tools = '/Users/paul/Desktop/CellularAutomata'
print(6)
if not tools in sys.path:
    sys.path.append(tools)
print(7)




from celula.transition_rule import transition_rule
print(8)
from celula.States import States
from celula.statistics_functions import *

print(9)
import Cell as cell

import Automata as automata

from Neighborhoods import Neighborhoods
from Borders import Borders


from automata.initial_state import initial_state



from QgsAutomata import QgsAutomata

print(10)
#exec(open('/Users/paul/Documents/qgis/CellularAutomata/main.py'.encode('utf-8')).read())

# cuadrado  Moore
# rombo     von_Neumann
print(11)
#if __name__ == '__main__':
print(12)



a = automata.Automata(width=10, height=5, store_trace_back=True)

print(a)
a.set_border(Borders.FIXED, States.Ignifugo)

print(a.border)
a.set_neighborhood(Neighborhoods.MOORE)

a.set_initial_state(initial_state)
a.set_transition_rule(transition_rule)

id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])
id = a.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])

print('gato')

# Imprime las iteraciones
# print(a.actual_iteration)
# for row in a.get_matrix_state():
#     print( row )
# print()
# for i in range(0, 4):
#     a.next()
#     print(a.actual_iteration)
#     for row in a.get_matrix_state():
#         print( row )
#     print()




# a.run_iterations(2, True)
# a.store_data_in_json()

states_color_dict = {
    States.Quemado: (255, 255, 255),
    States.Combustible: (0, 255, 0),
    States.Ardiendo: (255, 0, 0),
    States.Ignifugo: (0, 0, 255)
}
for s in states_color_dict:
    print(s.name, s.value)
print(states_color_dict)


print('-----')
qa = QgsAutomata(5, 5, True)
qa.gato()
print(qa.neighborhood, qa.neighborhood_list, qa.border)
print('\nFINAL\n')