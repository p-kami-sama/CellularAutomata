from Automata import Automata


class QgsAutomata(Automata):
    def __init__(self, w:int, h:int, store_trace_back:bool=False, route:str=None):
        print('bien')
        self.prueba = 'ESTO VA BIEN'

        super().__init__( width=w, height=h, store_trace_back=store_trace_back)
#        super().__init__(width=width, height=height, store_trace_back=store_trace_back)
        self.route = route

        if route != None:
            print('ok')
            self.load_raster_layer_as_initial_state(file_route=route)
            print('okey')
        #    'QgsData/raster_initial_state.tif'

       
            
        
        
    def gato(self):
        print('gatito lindo')


    def load_raster_layer_as_initial_state(self, file_route: str):
        print('ini load')

        # fi = QFileInfo(file_route)
        # file_name = fi.baseName()   #nombre del archivo(sin extensión)
        # print(file_name)

        # # Carga archivo y lo coloca como capa Raster
        # rlayer = iface.addRasterLayer(file_route, file_name)

        # # Pregunta el color en un punto del mapa

        # # x+0.5
        # # -y-0.5
        # x_corner = 0
        # y_corner = 0
        # medio = 0.5
        # for j in range(0, self.height): # y
        #     for i in range(0, self.width): # x
        #         x = x_corner + i + medio
        #         y = y_corner -j - medio
        #         ident = rlayer.dataProvider().identify(QgsPointXY( x , y), QgsRaster.IdentifyFormatValue )
        #         if ident.isValid():
        #             print( ident.results() )
        #         # The results method in this case returns a dictionary, with band indices as keys, and band values as values.

        # # {1: 17, 2: 220}
        print('end load')



    def save_raster_layer(self, route: str):
        pass

    
    def show_iteracion(self, iteration:int):
        pass