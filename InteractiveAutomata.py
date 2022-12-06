import csv
import math as math
import sys
import typing
import os
import glob

from platform import system
from PIL import Image, ImageTk


import Cell as cell
from Automata import Automata
from Interface import Interface
from InitialDataInterface import InitialDataInterface

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders




#from pandas import read_csv, concat



class InteractiveAutomata(Automata):

    
    def __init__(self, store_trace_back:bool=False, initial_state:typing.Union[str, list]=None):
        # valores propios: initial_state_route:str
        # el resto son heredados de Automata

        self.height = 0
        self.width = 0

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
        self.initial_state_route = None
        self.initial_data_file_path = None

        if system() == 'Windows':
            self.initial_data_file_path = '.\\initialData'
        elif system() == 'Darwin' or system() == 'Linux':
            self.initial_data_file_path = './initialData/'

        # saber si el directorio self.initial_data_file_path existe


        if os.path.exists(self.initial_data_file_path):
            from initialData.States import States
            from initialData.states_color_dict import states_color_dict
            from initialData.variables_dict import variables_dict
            self.States = States
            self.states_color_dict = states_color_dict
            self.variables_dict = variables_dict
        else:
            self.States = None
            self.states_color_dict = None
            self.variables_dict = None


        # BORRAR ???
        if isinstance(initial_state, str):
            # Hacerlo en la funcion adecuada 
            self.set_initial_state_from_image_and_csv()
        elif isinstance(initial_state, list):
            self.set_initial_state(mat=initial_state)
        elif initial_state is None:
            pass
        else:
            message = 'The first parameter "initial_state" must be the path of a .tif file, "None", or a list ' + \
                    'composed of valid states or dictionaries with the values of the cells to create.'
            raise ValueError(message)
            


    # LISTA de (celulas o de estado)
    # CREA LA FOTO DEL ESTADO INICIAL Y LA GUARDA EN -> /RESULTS
    def set_initial_state(self, mat:list):
        lista_de_color_de_pixeles = []
        malla = []
        y = 0
        for fila in mat:
            mallaAux = []
            x = 0
            for elem in fila:
                # elem es un diccionario
                if isinstance(elem, dict):
                    if not 'state' in elem:
                        message = 'if the initial information of a cell is a dictionary, it must have a key called '\
                                '"state", with the state that the cell will have before applying the transition rule.'
                        raise ValueError(message)
                    else:
                        vars = elem.copy()
                        del vars['state'] 
                        c = cell.Cell(self, xpos=x, ypos=y, state=elem['state'], variables=vars)
                        color = self.states_color_dict[elem['state']]
                        lista_de_color_de_pixeles.append(color)

                # elem es States
                elif isinstance(elem, self.States):
                    c = cell.Cell(self, xpos=x, ypos=y, state=elem, variables={})
                    color = self.states_color_dict[elem]
                    lista_de_color_de_pixeles.append(color)
                else:
                    message = 'The input to create the cell with coordinates (' +\
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
        img = Image.new('RGB', (self.width, self.height))

        if system() == 'Windows':
            self.initial_state_route = '.\\results\\initial_state.tif'
        elif system() == 'Darwin' or system() == 'Linux':
            self.initial_state_route = './results/initial_state.tif'
        # por filas de arriba a abajo.

        img.putdata(lista_de_color_de_pixeles)
        img.save(self.initial_state_route)

        return self.height, self.width




    def open_interface(self):
        app = Interface(img=self.initial_state_route, automata=self)
        app.mainloop()


    def open_initial_interface(self):
        result = InitialDataInterface()
        result.mainloop()
        dictionary = result.get_data()

        # 'border', 'neighborhood', 'radius', 'initial_data_file_path', 'store_trace_back'
        print('dictionary:\n\n', dictionary)

        self.set_border(dictionary['border'])
        self.set_neighborhood(dictionary['neighborhood'], dictionary['radius'])
        self.initial_data_file_path = dictionary['initial_data_file_path']
        self.store_trace_back = dictionary['store_trace_back']

        # import de todos los archivos necesarios
        sys.path.append(dictionary['initial_data_file_path'])
       
        from States import States
        from states_color_dict import states_color_dict
        from variables_dict import variables_dict
        self.States = States
        self.states_color_dict = states_color_dict
        self.variables_dict = variables_dict

        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'

        # extraer, initial_state
        if os.path.exists(self.initial_data_file_path + path_separator + 'initial_state.py'):
            from initial_state import initial_state
            self.set_initial_state(initial_state)

        else:   # cargar cosas de csv e imagen
            pass
                # SEPARAR set_initial_state_from_image_and_csv EN 2 COSAS




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
        self.initial_state_route = tif_initial_image



        img = Image.open( tif_initial_image ) # Can be many different formats.
        pix = img.load()
        x, y = img.size  # Get the width and hight of the image for iterating over
        self.width = x
        self.height = y
        matrix = []
        for y in range(0, self.height):
            row_list = []
            for x in range(0, self.width):
                r, g, b = pix[x, y]
                state = self._get_state_from_color(r, g, b)
                row_list.append({'state': state})
            matrix.append(row_list)

        # leer archivos csv
        if len(csv_files) != 0:
            for route_to_file in csv_files:
                file_name = os.path.basename(route_to_file).split('.')[0]
                if not (file_name in self.variables_dict):
                    message = 'In "variables_dict.py" there is no type of ' + \
                        'variable assigned to file "' +route_to_file +'".'
                    raise ValueError(message)

                var_type = self.variables_dict[file_name]
                with open(route_to_file, newline='') as f:
                    reader = csv.reader(f)
                    y = 0
                    for row in reader:
                        x = 0
                        for elem in row:
                            if var_type == 'int':
                                value = int(elem)
                            elif var_type == 'float':
                                value = float(elem)
                            elif var_type == 'str':
                                value = str(elem)
                            elif var_type == 'bool':
                                value = bool(elem)
                            matrix[y][x][file_name] = value
                            x += 1
                        y += 1

        # Pasa de diccionario a celulas
        malla = []
        y = 0
        for fila in matrix:
            mallaAux = []
            x = 0
            for elem in fila:
                vars = elem.copy()
                del vars['state'] 
                c = cell.Cell(self, xpos=x, ypos=y, state=elem['state'], variables=vars)
                mallaAux.append(c)
                x = x+1
                
            malla.append(mallaAux)
            y = y+1

        self.iterations = {}
        self.iterations[0] = malla
        self.actual_iteration = 0
        self.last_iteration_calculated = 0


    

    # hace la nueva iteración y crea la nueva foto
    # devuelve el path de la nueva imagen
    def next_image_iteration(self):
        self.next()

        abs_path = os.path.dirname( os.path.abspath(__file__) )
        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'

        route_to_image = abs_path + path_separator + 'results'+ path_separator + \
            'iteration_' + str(self.actual_iteration) + '.tif'

        # Se comprueba si existe
        if os.path.exists(route_to_image):
            return route_to_image
        else:   # Se crea la imagen

            lista_de_color_de_pixeles = []
            for fila in self.iterations[self.actual_iteration]:
                for elem in fila: # elem es un objeto de tipo Cell
                    state = elem.get_state()
                    color = self.states_color_dict[state]
                    lista_de_color_de_pixeles.append(color)

            img = Image.new('RGB', (self.width, self.height))            
            img.putdata(lista_de_color_de_pixeles)
            img.save(route_to_image)

            # Se crean los archivos csv

            folder_path = abs_path + path_separator + 'initialData'
            csv_files = glob.glob(folder_path + "/*.csv")
            tif_initial_image = glob.glob(folder_path + "/*.tif")[0]
            self.initial_state_route = tif_initial_image

            for var_name, var_type in self.variables_dict.items():

                # se hace un csv por cada variable
                route_to_csv = abs_path + path_separator + 'results'+ path_separator + \
                    'iteration_' + str(self.actual_iteration)+'_'+var_name + '.csv'

                
                with open(route_to_csv, 'w', encoding='UTF8', newline='') as f:
                
                    writer = csv.writer(f)
                    data_list = []
                    for fila in self.iterations[self.actual_iteration]:
                        data_row = []
                        for elem in fila:
                            var = elem.get_variable(var_name)

                            if var_type == 'int':
                                var = int(var)
                            elif var_type == 'float':
                                var = float(var)
                            elif var_type == 'str':
                                var = str(var)
                            elif var_type == 'bool':
                                var = bool(var)
                    
                            data_row.append(var)

                        data_list.append(data_row)
                           
                           

                        # write a row to the csv file
                    writer.writerows(data_list)

            return route_to_image



    def back_image_iteration(self):
        if self.actual_iteration <= 0:
            return None
        else:
            self.actual_iteration -= 1

        # Se obtiene la ruta de la imagen
        abs_path = os.path.dirname( os.path.abspath(__file__) )
        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'

        route_to_image = abs_path + path_separator+'iteration_' + str(self.actual_iteration) + '.tif'

        route_to_image = abs_path + path_separator + 'results'+ path_separator + \
            'iteration_' + str(self.actual_iteration) + '.tif'

        # Se comprueba si existe
        if os.path.exists(route_to_image):
            return route_to_image
        else:   # Se crea la imagen

            lista_de_color_de_pixeles = []
            for fila in self.iterations[self.actual_iteration]:
                for elem in fila: # elem es un objeto de tipo Cell
                    state = elem.get_state()
                    color = self.states_color_dict[state]
                    lista_de_color_de_pixeles.append(color)

            img = Image.new('RGB', (self.width, self.height))            
            img.putdata(lista_de_color_de_pixeles)
            img.save(route_to_image)

            return route_to_image

# HACER
    def run_image_iterations(self, num_iterations:int, print_data:bool=False):
        pass
    # ajecutar x iteraciones (desde el inicio)


# revisar -> i, j mal (pasar como parámetro ???)
    def _get_state_from_color(self, red:int, green:int, blue:int):
        i = -1
        j = -1
        value = (int(red), int(green), int(blue))

        if not (value in list(self.states_color_dict.values()) ):
            message = 'At the ('  + str(i) + ', ' + str(j) + ' position, the (' + \
                str(red) + ', ' + str(green) + ', ' + str(blue) + ') ' + \
                'color, is not related to any state in states_color_dict.'
            raise ValueError(message)

        state = list(self.states_color_dict.keys())[list(self.states_color_dict.values()).index(value)] 
        return state