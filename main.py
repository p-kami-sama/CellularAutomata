#from prueba_raster import gato
# from qgis.core import *

import sys
import csv

# NECESARIO PARA PODER SER EJECUTADO EN QGIS
# Configuracion -> opciones -> general -> Default paths -> absoluto
# Configuracion -> opciones -> Red -> cache settings (la de la carpeta dónde se trabaja)
path = '/Users/paul/Desktop/CellularAutomata'
if not path in sys.path:
    sys.path.append(path)

# print(sys.path)


# IMPORTS
import Automata as automata

#import QgsAutomata as qgsAutomata

from celula.transition_rule import transition_rule, transition_rule_GameOfLife
from celula.States import States, States_GameOfLife
from celula.statistics_functions import *

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders
from automata.initial_state import initial_state, initial_state_GameOfLife

from QgsData.states_color_dict import states_color_dict #, states_color_dict_GameOfLife


# ruta

file_route = '/Users/paul/Desktop/CellularAutomata/QgsData/raster_v2.tif'


#Se inicializa QgsAutomata
print('se inicia el automata')




# cuadrado  Moore
# rombo     von_Neumann


a = automata.Automata(width=10, height=5, store_trace_back=True)
a.set_border(Borders.FIXED, States.Ignifugo)
a.set_neighborhood(Neighborhoods.MOORE)
a.set_initial_state(initial_state)
a.set_transition_rule(transition_rule)
id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])
id = a.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])

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
print(str(States.Ardiendo) == 'Ardiendo')



gol = automata.Automata(10, 10, True)
gol.set_border(Borders.FIXED, States.Muerto)
gol.set_neighborhood(Neighborhoods.MOORE, 1)
gol.set_initial_state(initial_state_GameOfLife)
gol.set_transition_rule(transition_rule_GameOfLife)

gol.run_iterations(3, True)