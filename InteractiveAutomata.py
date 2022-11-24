import csv
import math as math
import json
import typing
import os
import glob

from platform import system
from PIL import Image, ImageTk


import Cell as cell
from Automata import Automata


from celula.States import States


from InteractiveAutomataData.states_color_dict import states_color_dict
from InteractiveAutomataData.variables_dict import variables_dict



import automata.Statistic as statistic
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders




from pandas import read_csv, concat

class InteractiveAutomata(Automata):

# Definir que hace exactamente
    
    def __init__(self, initial_state:typing.Union[str, list], store_trace_back:bool=False):
        # valores propios: initial_state_route:str
        # el resto son heredados de Automata

        if isinstance(initial_state, str):
            # Hacerlo en la funcion adecuada 
            self.initial_state_route = initial_state
            self.set_initial_state_from_image_and_csv()

        elif isinstance(initial_state, list):
            self.set_initial_state(mat=initial_state)
        else: # ERROR
            message = 'The first parameter "initial_state" must be the path of a .tif file or a list ' + \
                    'composed of valid states or dictionaries with the values of the cells to create.'
            raise ValueError(message)
            

        self.neighborhood = Neighborhoods.VON_NEUMANN
        self.neighborhood_list = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        self.border = Borders.PERIODIC
        self.fixed_cell = None    # solo si border == 'periodic' será usada

        self.actual_iteration = 0
        self.last_iteration_calculated = 0
        self.transition_rule = None
        self.iterations = {}

        self.store_trace_back = store_trace_back
        self.data = {}
        self.statistics = {} # id:int, statistics



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

        if system() == 'Windows':
            self.initial_state_route = '.\\results\\initial_state.tif'
        elif system() == 'Darwin' or system() == 'Linux':
            self.initial_state_route = './results/initial_state.tif'
        # por filas de arriba a abajo.

        im.putdata(lista_de_color_de_pixeles)
        im.save(self.initial_state_route)

        return self.height, self.width





# Pendiente de hacer


    def set_initial_state_from_image_and_csv(self):
        # obtiene ruta absoluta del directorio donde esta
        abs_path = os.path.dirname( os.path.abspath(__file__) )
        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'

        folder_path = abs_path + path_separator + 'initialData'

        csv_files = glob.glob(folder_path + "/*.csv")
        tif_initial_image = glob.glob(folder_path + "/*.tif")[0]
        print('csv_files:', csv_files)
        print('tif_initial_image:', tif_initial_image)


        im = Image.open( tif_initial_image ) # Can be many different formats.
        pix = im.load()
        print (im.size)  # Get the width and hight of the image for iterating over
        print (pix[0,0])
        print (pix[1,0])
        pix[1,1] = (255, 0, 0)  # Set the RGBA Value of the image (tuple)
        im.save('results/alive_parrot.tif')  # Save the modified pixels as .png

        # AQUI FALTA LEER .tif
        # meterlo en un diccionario con 'state'
        # luego enlacarlo con tif usando file_name, 
        #   evitandovar_list y var_row


        # leer archivos csv
        if len(csv_files) != 0:
            for route_to_file in csv_files:
                var_list = []
                file_name = os.path.basename(route_to_file).split('.')[0]
                if not (file_name in variables_dict):   # ERROR
                    message = 'In "variables_dict.py" there is no type of ' + \
                        'variable assigned to file "' +route_to_file +'".'
                    raise ValueError(message)

                var_type = variables_dict[file_name]
                with open(route_to_file, newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        var_row = []
                        for elem in row:
                            if var_type == 'int':
                                elem = int(elem)
                            elif var_type == 'float':
                                elem = float(elem)
                            elif var_type == 'str':
                                elem = str(elem)
                            elif var_type == 'bool':
                                elem = bool(elem)
                            var_row.append(elem)

                        var_list.append(var_row)
                print('++++++++++\n', var_list)
                # var_list contiene las variables de X.csv file
                # en 2 listas ordenadas

            
            # converting content to data frame


        print('------\n', 'END', '\n------')




        # system.path()
        # initial_state_image = Image.open(route)
    
        # # directory = os.path.join("c:\\","path")
        # directory = route

        # files = glob.glob(route + "/*.csv")
        # for root,dirs,files in os.walk(directory):
        #     for file in files:

        #         if file.endswith(".csv"):
        #             f=open(file, 'r')
        #             #  perform calculation
        #             f.close()







    
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