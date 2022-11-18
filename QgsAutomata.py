from Automata import Automata
from qgis.core  import *
import qgis.utils
from PyQt5.QtCore import QFileInfo


from celula.States import States
from QgsData.states_color_dict import states_color_dict

class QgsAutomata(Automata):

    
    def __init__(self, w:int, h:int, iface, store_trace_back:bool=False, route:str=None, upper_left_corner_x:float=0, upper_left_corner_y:float=0, cell_size:float = 1.0):
        
        self.iface = iface
        self.upper_left_corner_x = upper_left_corner_x
        self.upper_left_corner_y = upper_left_corner_y
        self.cell_size = cell_size
        


        super().__init__( width=w, height=h, store_trace_back=store_trace_back)
#        super().__init__(width=width, height=height, store_trace_back=store_trace_back)
        self.route = route

        if route != None:
            self.load_raster_layer_as_initial_state(route, upper_left_corner_x, upper_left_corner_y, cell_size)
        #    'QgsData/raster_initial_state.tif'

       
            
        
        
    def gato(self):
        print('gatito lindo')


    def load_raster_layer_as_initial_state(self, file_route: str, upper_left_corner_x:float=0, upper_left_corner_y:float=0, cell_size:float = 1.0):
        print('ini load')
        
        fi = QFileInfo(file_route)
        file_name = fi.baseName()   #nombre del archivo(sin extensión)

        # Carga archivo y lo coloca como capa Raster
        rlayer = self.iface.addRasterLayer( file_route, file_name)

        # Pregunta el color en un punto del mapa

        # x+0.5
        # -y-0.5
        # upper_left_corner_x = 0
        # upper_left_corner_y = 0
        medio = cell_size/2
        malla = []
        for j in range(0, self.height): # y
            fila = []
            for i in range(0, self.width): # x
                x = upper_left_corner_x + i + medio
                y = upper_left_corner_y -j - medio
                ident = rlayer.dataProvider().identify(QgsPointXY( x , y), QgsRaster.IdentifyFormatValue )
                if ident.isValid():
                    # ACABAR -> AQUÍ RECOGER DATOS 
                    print('----\n', ident.results()[1], '\n-------')
                    red   = ident.results()[1]
                    green = ident.results()[2]
                    blue  = ident.results()[3]

                    if (red is None) or (green is None) or (green is None):
                        message = 'Attempt to access positions (' + str(x) + ', ' + str(y) + \
                            ') where no valid data entry was found.'
                        raise ValueError(message)

                    else:
                        value = (int(red), int(green), int(blue))

                        if not (value in list(states_color_dict.values()) ):

                            message = 'At the ('  + str(x) + ', ' + str(y) + ' position, the (' + \
                                str(red) + ', ' + str(green) + ', ' + str(blue) + ') ' + \
                                'color, is not related to any state in states_color_dict.'
                            raise ValueError(message)



                        data = list(states_color_dict.keys())[list(states_color_dict.values()).index(value)] 
                        print(data, x, y)
                        fila.append(data)
                else:
                    # ACABAR -> añadir mensaje de ERROR en caso de obtener una ident no valida
                    message = 'ttempt to access positions (' + str(x) + ', ' + str(y) + \
                        ') where no valid data entry was found.'
                    raise ValueError(message)
            
            malla.append(fila)

        # The results method in this case returns a dictionary, with band indices as keys, and band values as values.
        # {1: 17, 2: 220}
        print('end load')
        #  LLAMAR A self.set_initial_state(), con los datos obtenidos del raster
        self.set_initial_state(malla)




    def save_raster_layer(self, route: str):
        pass

    
    def show_iteracion(self, iteration:int):
        pass