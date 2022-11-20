# #from prueba_raster import gato
# # from qgis.core import *

# import sys
# import csv

# # NECESARIO PARA PODER SER EJECUTADO EN QGIS
# # Configuracion -> opciones -> general -> Default paths -> absoluto
# # Configuracion -> opciones -> Red -> cache settings (la de la carpeta dónde se trabaja)
# path = '/Users/paul/Desktop/CellularAutomata'
# if not path in sys.path:
#     sys.path.append(path)

# # print(sys.path)









# # IMPORTS
# import Automata as automata

# #from QgsAutomata import QgsAutomata
# import QgsAutomata as qgsAutomata

# from celula.transition_rule import transition_rule
# from celula.States import States
# from celula.statistics_functions import *

# from automata.Neighborhoods import Neighborhoods
# from automata.Borders import Borders
# from automata.initial_state import initial_state

# # from QgsData.States_to_color import states_color_dict
# # from QgsData.states_color_dict import states_color_dict

# import importlib
# importlib.reload(qgsAutomata)
# importlib.reload(automata)

# # ruta

# file_route = '/Users/paul/Desktop/CellularAutomata/QgsData/r_ini.tif'



# fi = QFileInfo(file_route)
# file_name = fi.baseName()   #nombre del archivo(sin extensión)
# print(file_name)













# #Se inicializa QgsAutomata
# print('se inicia el automata')
# qga = qgsAutomata.QgsAutomata( w=10, h=10, iface=iface, project_path=path, store_trace_back=True, initial_state_route=file_route)



# print(qga.route, qga.height, qga.width, qga.actual_iteration)
# print( qga.height, qga.width)
# qga.set_border(Borders.FIXED, States.Ignifugo)
# qga.set_neighborhood(Neighborhoods.MOORE)
# qga.set_transition_rule(transition_rule)

# id = qga.add_statistic( statistic_1_function, 'Esta ardiendo', [])
# id = qga.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])







# #driver = gdal.GetDriverByName('GTiff')
# #print(driver)
# #
# #ds = driver.Create(fn, xsize=x_sixe, ysize=y_size, bands=1, eType =gdal.GDT_Float32)
# #ds.GetRasterBand(1).WriteArray(rasterband)
# #
# #
# #geot = [500000, 10, 0, 4600000, 0, -10]
# #ds.SetGeoTransform(geot)


# # rlayer = QgsProject.instance().mapLayersByName('srtm')[0]
# # # get the resolution of the raster in layer unit
# # print(rlayer.width(), rlayer.height())





# #exec(open('/Users/paul/Documents/qgis/CellularAutomata/main.py'.encode('utf-8')).read())

# # cuadrado  Moore
# # rombo     von_Neumann




# # print(qga.actual_iteration)
# # for row in qga.get_matrix_state():
# #     print( row )
# # print()

# #
# #a = automata.Automata(width=10, height=5, store_trace_back=True)
# #
# #a.set_border(Borders.FIXED, States.Ignifugo)
# #
# #a.set_neighborhood(Neighborhoods.MOORE)
# #
# #a.set_initial_state(initial_state)
# #a.set_transition_rule(transition_rule)
# #
# #id = a.add_statistic( statistic_1_function, 'Esta ardiendo', [])
# #id = a.add_statistic( statistic_2_function, 'Esta celda es ignifuga', [])
# #

# # Imprime las iteraciones
# print(qga.actual_iteration)
# for row in qga.get_matrix_state():
#     print( row )
# print()
# for i in range(0, 4):
#     qga.next()
#     print(qga.actual_iteration)
#     for row in qga.get_matrix_state():
#         print( row )
#     print()




# # a.run_iterations(2, True)
# # a.store_data_in_json()
# #
# #states_color_dict = {
# #    States.Quemado: (255, 255, 255),
# #    States.Combustible: (0, 255, 0),
# #    States.Ardiendo: (255, 0, 0),
# #    States.Ignifugo: (0, 0, 255)
# #}
# #for s in states_color_dict:
# #    print(s.name, s.value)
# #print(states_color_dict)
# #
# #
# #print('-----')
# #qa = QgsAutomata(5, 5, True)
# #qa.gato()
# #print(qa.neighborhood, qa.neighborhood_list, qa.border)
# #
# print('\nFINAL\n')


# qga.show_iteracion(1)

# #qga.show_iteracion(2)







from osgeo import gdal, osr
import numpy as np

fn = '/Users/paul/Desktop/CellularAutomata/results/R000.tif'

rasterband = np.zeros((10,10))
rasterband_eye = np.eye(10)*255
rasterband255 =  np.array([[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],

                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]])


rasterbandRed =  np.array([[255, 0, 0],
                            [255, 0, 0],
                            [255, 0, 255]])
                           
rasterbandGreen =  np.array([[255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255]])
                            
rasterbandBlue =  np.array([[0, 0, 255],
                            [0, 255, 255],
                            [255, 0, 255]])

rasterbandAlpha =  np.array([[255, 255, 255],
                            [255, 255, 120],
                            [255, 255, 255]])

# rasterbandGreen =  np.array([[0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],

#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255],
#                             [0, 0, 255, 255, 255, 255, 255, 255, 255, 255]])





driver = gdal.GetDriverByName('GTiff')
ds = driver.Create(fn, xsize=3, ysize=3, bands=3, eType=gdal.GDT_Float32)

# print(rlayer.rasterType())
ds.GetRasterBand(1).WriteArray(rasterbandRed)
# ds.GetRasterBand(1).setMin(0)
# ds.GetRasterBand(1).setMaximumValue(255)

ds.GetRasterBand(2).WriteArray(rasterbandGreen)
ds.GetRasterBand(3).WriteArray(rasterbandBlue)
# ds.GetRasterBand(4).WriteArray(rasterbandAlpha)




# [top-left x coord,   cell width,     0,     top-left y coord,   0,   cell height]
geot = [0, 0, 0, 0, 0, -10]
ds.SetGeoTransform(geot)
srs = osr.SpatialReference()
srs.SetUTM(12,1)
srs.SetWellKnownGeogCS('NAD83')
ds.SetProjection(srs.ExportToWkt())
ds = None


rlayer = iface.addRasterLayer(fn)


provider = rlayer.dataProvider()
# provider.setEditable(True)
# provider.writeBlock(block, 1, 0, 0)
# provider.setEditable(False)



# rmmo = provider.QgsRasterMinMaxOrigin()

print('rlayer.rasterType(): ', rlayer.rasterType())
print('rlayer.bandCount():', rlayer.bandCount())
print(rlayer.bandName(1))
print(rlayer.bandName(2))
print(rlayer.bandName(3))

print(rlayer.renderer().type())


#fnc = QgsColorRampShader()
#fnc.setColorRampType(QgsColorRampShader.Exact)
#

stats = rlayer.dataProvider().bandStatistics(3, QgsRasterBandStats.All)
min = stats.minimumValue
max = stats.maximumValue
print('min:', min,'    max', max)


# QgsSingleBandPseudoColorRenderer(input: QgsRasterInterface, band: int = -1, shader: QgsRasterShader = None)

print('rlayer', rlayer)
render = QgsMultiBandColorRenderer( provider, 1, 2, 3)



print('ContrastEnhancement:', render.redContrastEnhancement())
print(render.greenContrastEnhancement(), render.blueContrastEnhancement())

# Tampoco funciona
x = QgsContrastEnhancement()
z= QgsContrastEnhancement.ContrastEnhancementAlgorithm.NoEnhancement

x.setContrastEnhancementAlgorithm(z)

#cont_enh = QgsContrastEnhancement().setContrastEnhancementAlgorithm.NoEnhancement()

render.setRedContrastEnhancement( x )
render.setGreenContrastEnhancement( x )
render.setBlueContrastEnhancement( x  )
#QgsContrastEnhancement().NoEnhancement

print('ContrastEnhancement:', render.redContrastEnhancement())
print(render.greenContrastEnhancement(), render.blueContrastEnhancement())

print('render', render)


#rlayer.setRenderer(renderer)
print('rlayer.renderer().type()', rlayer.renderer().type())


#print(rlayer.GetBand(1).QgsContrastEnhancement.MaximumValue, QgsContrastEnhancement.MinimumValue)



print(QgsContrastEnhancement.NoEnhancement)


rlayer.triggerRepaint()
