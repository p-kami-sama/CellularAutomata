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

#from QgsAutomata import QgsAutomata
import QgsAutomata as qgsAutomata

from celula.transition_rule import transition_rule
from celula.States import States
from celula.statistics_functions import *

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders
from automata.initial_state import initial_state

# from QgsData.States_to_color import states_color_dict
# from QgsData.states_color_dict import states_color_dict

import importlib
importlib.reload(qgsAutomata)
importlib.reload(automata)

# ruta

file_route = '/Users/paul/Desktop/CellularAutomata/QgsData/raster_v2.tif'



fi = QFileInfo(file_route)
file_name = fi.baseName()   #nombre del archivo(sin extensión)
print(file_name)













#Se inicializa QgsAutomata
print('se inicia el automata')
qga = qgsAutomata.QgsAutomata( w=10, h=10, iface=iface, project_path=path, store_trace_back=True, initial_state_route=file_route)



print(qga.route, qga.height, qga.width, qga.actual_iteration)
print( qga.height, qga.width)
qga.set_border(Borders.FIXED, States.Ignifugo)
qga.set_neighborhood(Neighborhoods.MOORE)
qga.set_transition_rule(transition_rule)

id = qga.add_statistic( statistic_1_function, 'Esta ardiendo', [])
id = qga.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])







#driver = gdal.GetDriverByName('GTiff')
#print(driver)
#
#ds = driver.Create(fn, xsize=x_sixe, ysize=y_size, bands=1, eType =gdal.GDT_Float32)
#ds.GetRasterBand(1).WriteArray(rasterband)
#
#
#geot = [500000, 10, 0, 4600000, 0, -10]
#ds.SetGeoTransform(geot)


# rlayer = QgsProject.instance().mapLayersByName('srtm')[0]
# # get the resolution of the raster in layer unit
# print(rlayer.width(), rlayer.height())





#exec(open('/Users/paul/Documents/qgis/CellularAutomata/main.py'.encode('utf-8')).read())

# cuadrado  Moore
# rombo     von_Neumann




# print(qga.actual_iteration)
# for row in qga.get_matrix_state():
#     print( row )
# print()

#
#a = automata.Automata(width=10, height=5, store_trace_back=True)
#
#a.set_border(Borders.FIXED, States.Ignifugo)
#
#a.set_neighborhood(Neighborhoods.MOORE)
#
#a.set_initial_state(initial_state)
#a.set_transition_rule(transition_rule)
#
#id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])
#id = a.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])
#

# Imprime las iteraciones
print(qga.actual_iteration)
for row in qga.get_matrix_state():
    print( row )
print()
for i in range(0, 4):
    qga.next()
    print(qga.actual_iteration)
    for row in qga.get_matrix_state():
        print( row )
    print()




# a.run_iterations(2, True)
# a.store_data_in_json()
#
#states_color_dict = {
#    States.Quemado: (255, 255, 255),
#    States.Combustible: (0, 255, 0),
#    States.Ardiendo: (255, 0, 0),
#    States.Ignifugo: (0, 0, 255)
#}
#for s in states_color_dict:
#    print(s.name, s.value)
#print(states_color_dict)
#
#
#print('-----')
#qa = QgsAutomata(5, 5, True)
#qa.gato()
#print(qa.neighborhood, qa.neighborhood_list, qa.border)
#
print('\nFINAL\n')


