import csv
import platform
import math as math
import json
import typing
from PIL import Image, ImageTk

import Cell as cell
from Automata import Automata


from celula.States import States


from InteractiveAutomataData.states_color_dict import states_color_dict
from InteractiveAutomataData.variables_dict import variables_dict


import automata.Statistic as statistic
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders




class InteractiveAutomata(Automata):

    def __init__(self, w:int, h:int, store_trace_back:bool=False, initial_state_route:str=None):

        print()

        self.initial_state_route = initial_state_route # a de ser una ruta obsoluta

        super().__init__( width=w, height=h, store_trace_back=store_trace_back)

        # if initial_state_route != None:
        #     self.load_raster_layer_as_initial_state(initial_state_route)



    # LISTA de (celulas o de estado)
    # CREA LA FOTO DEL ESTADO INICIAL Y LA GUARDA EN -> /RESULTS
    def set_initial_state(self, mat:list):
#        load_initial_state(self, route:str):
        print('REESCRITURA')
        lista_de_color_de_pixeles = []

        malla = []
        y = 0
        for fila in mat:
            mallaAux = []
            x = 0
            for elem in fila:
                # elem es diccionario
                if isinstance(elem, dict):
#                    if 'variables' in elem:
                    if not 'state' in elem:
                        message = 'ERROR: if the initial information of a cell is a dictionary, it must have a key called '\
                                '"state", with the state that the cell will have before applying the transition rule.'
                        raise ValueError(message)
                    else:
                        vars = elem.copy()
                        del vars['state'] 
                        c = cell.Cell(self, xpos=x, ypos=y, state=elem['state'], variables=vars)
                        color = states_color_dict[elem['state']]
                        lista_de_color_de_pixeles.append(color)

                # elem es States
                elif isinstance(elem, States):
                    c = cell.Cell(self, xpos=x, ypos=y, state=elem, variables={})
                    color = states_color_dict[elem]
                    lista_de_color_de_pixeles.append(color)
                else:
                    message = '(ERROR the input to create the cell with coordinates (' +\
                        str(x) + ', ' + str(y) + ') is not correct. The imput must be a "state" included in '+\
                        '"States" enumeration or a dictionary.'
                    raise ValueError(message)
                    
                mallaAux.append(c)
                x = x+1
                
            malla.append(mallaAux)
            y = y+1

        self.iterations = {}
        self.iterations[0] = malla
        self.initial_state = malla
        self.actual_iteration = 0
        self.last_iteration_calculated = 0
        self.data = {}

        # Aquí se hace la imagen

        self.height = len(mat)      # y
        self.width = len(mat[0])    # x
        im = Image.new('RGB', (self.width, self.height))

        # adaptar al SO
        route = './results/initial_state.tif'



        # por filas de arriba a abajo.

        im.putdata(lista_de_color_de_pixeles)
        im.save(route)











# Pendiente de hacer

    def load_initial_state_from_image(self, ruta:str):
        pass
    
    def open_interface(self):
        pass



    def next_image_iteration(self):
        pass

    def back_image_iteration(self):
        pass

    def run_image_iterations(self, num_iterations:int, print_data:bool=False):
        pass
    # ajecutar x iteraciones (desde el inicio)


# revisar -> i, j mal (pasar como parámetro ???)
    def _get_state_from_color(self, red:int, green:int, blue:int):
        i = -1
        j = -1
        value = (int(red), int(green), int(blue))

        if not (value in list(states_color_dict.values()) ):
            message = 'At the ('  + str(i) + ', ' + str(j) + ' position, the (' + \
                str(red) + ', ' + str(green) + ', ' + str(blue) + ') ' + \
                'color, is not related to any state in states_color_dict.'
            raise ValueError(message)

        state = list(states_color_dict.keys())[list(states_color_dict.values()).index(value)] 
        return state