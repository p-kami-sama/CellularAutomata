from Automata import Automata


class QgsAutomata(Automata):
    def __init__(self, width:int, height:int, store_trace_back:bool=False):
        super().__init__(width, height, store_trace_back)
        
        
    def gato(self):
        print('gatito lindo')


    def load_raster_layer_as_initial_state(self, route: str):
        pass


    def save_raster_layer(self, route: str):
        pass

    
    def show_iteracion(self, iteration:int):
        pass