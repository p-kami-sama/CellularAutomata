import csv

from Automata import Automata
from qgis.core  import *
import qgis.utils
from PyQt5.QtCore import QFileInfo
from osgeo import gdal


from celula.States import States
from QgsData.states_color_dict import states_color_dict

class QgsAutomata(Automata):

    
    def __init__(self, w:int, h:int, iface, project_path:str, store_trace_back:bool=False, initial_state_route:str=None ):
        self.project_path = project_path

        self.iface = iface
        self.route = initial_state_route
    
        
        super().__init__( width=w, height=h, store_trace_back=store_trace_back)

        if initial_state_route != None:
            self.load_raster_layer_as_initial_state(initial_state_route)
        #    'QgsData/raster_initial_state.tif'


       
            
        
        
    def gato(self):
        print('gatito lindo')


    def load_raster_layer_as_initial_state(self, file_route: str):
        print('ini load', self.width, self.height)
        
        file_info = QFileInfo(file_route)
        file_name = file_info.baseName()   #nombre del archivo(sin extensión)
        print(file_name, '------')

        # Carga archivo y lo coloca como capa Raster
        rlayer = self.iface.addRasterLayer( file_route, file_name)
        ds = gdal.Open(rlayer.dataProvider().dataSourceUri())
        


        malla = []
        for j in range(0, self.height): # y -> recorre filas
            fila = []
            for i in range(0, self.width): # x -> recorre columnas

                red   = ds.GetRasterBand(1).ReadAsArray()[j][i]
                green = ds.GetRasterBand(2).ReadAsArray()[j][i]
                blue  = ds.GetRasterBand(3).ReadAsArray()[j][i]


                if (red is None) or (green is None) or (green is None):
                    message = 'Attempt to access positions (' + str(i) + ', ' + str(j) + \
                        ') where no valid data entry was found.'
                    raise ValueError(message)

                else:
                    value = (int(red), int(green), int(blue))

                    if not (value in list(states_color_dict.values()) ):
                        message = 'At the ('  + str(i) + ', ' + str(j) + ' position, the (' + \
                            str(red) + ', ' + str(green) + ', ' + str(blue) + ') ' + \
                            'color, is not related to any state in states_color_dict.'
                        raise ValueError(message)

                    data = list(states_color_dict.keys())[list(states_color_dict.values()).index(value)] 
                    print(data, i, j)
                    fila.append(data)

            malla.append(fila)

        self.set_initial_state(malla)
        print('end load', self.width, self.height)


        # with open('QgsData/info.csv', newline='') as f:
        #     reader = csv.reader(f)
        #     data = list(reader)

        # print(data)
        # print('ENDO')







    def save_raster_layer(self, route: str):
        pass

    
    def show_iteracion(self, iteration:int):
        pass