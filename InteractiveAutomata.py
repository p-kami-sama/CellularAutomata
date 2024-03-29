import csv
import sys
import os
import glob

from platform import system
from PIL import Image

import Cell as cell
from Automata import Automata
from Interface import Interface
from InitialDataInterface import InitialDataInterface

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders



class InteractiveAutomata(Automata):
    
    def __init__(self, store_trace_back:bool=False, initial_data_file_path:str=None):

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

        self.initial_data_file_path = None
        self.valid_states = []

        # new
        self.states_color_dict = {}
        self.variables_dict = {}
        self.initial_state_route = None

        # saber si el directorio self.initial_data_file_path existe

        self.__set_data_from_file(initial_data_file_path)
     


    # LISTA de (celulas o de estado)
    # CREA LA FOTO DEL ESTADO INICIAL Y LA GUARDA EN -> /RESULTS
    def set_initial_state(self, mat:list):
        lista_de_color_de_pixeles = []
        malla = []
        y = 0
        for fila in mat:
            malla_aux = []
            x = 0
            for elem in fila:
                # elem es un diccionario
                if isinstance(elem, dict):
                    if 'state' not in elem:
                        message = 'if the initial information of a cell is a dictionary, it must have a key called '\
                                '"state", with the state that the cell will have before applying the transition rule.'
                        raise ValueError(message)
                    else:
                        variables = elem.copy()
                        del variables['state'] 
                        c = cell.Cell(self, xpos=x, ypos=y, state=elem['state'], variables=variables)
                        color = self.states_color_dict[elem['state']]
                        lista_de_color_de_pixeles.append(color)

                # elem es States
                elif elem in self.valid_states:
                    c = cell.Cell(self, xpos=x, ypos=y, state=elem, variables={})
                    color = self.states_color_dict[elem]
                    lista_de_color_de_pixeles.append(color)
                else:
                    message = 'The input to create the cell with coordinates (' +\
                        str(x) + ', ' + str(y) + ') is not correct. The imput must be a "state" included in '+\
                        '"States" enumeration or a dictionary.'
                    raise ValueError(message)
                    
                malla_aux.append(c)
                x = x+1
                
            malla.append(malla_aux)
            y = y+1

        self.iterations = {}
        self.iterations[0] = malla
        self.actual_iteration = 0
        self.last_iteration_calculated = 0
        self.data = {}

        # Aquí se hace la imagen
        self.height = len(mat)      # y
        self.width = len(mat[0])    # x
        img = Image.new('RGB', (self.width, self.height))

        if system() == 'Windows':
            
            try:
                os.stat('.\\results')
            except:
                os.mkdir('.\\results')
            
            self.initial_state_route = '.\\results\\initial_state.tif'
        elif system() == 'Darwin' or system() == 'Linux':
            try:
                os.stat('./results')
            except:
                os.mkdir('./results')
            self.initial_state_route = './results/initial_state.tif'
       
        # por filas de arriba a abajo.
        img.putdata(lista_de_color_de_pixeles)
        img.save(self.initial_state_route)
        return self.height, self.width



    def open_interface(self):
        app = Interface(img=self.initial_state_route, automata=self, variables_dict=self.variables_dict)
        app.mainloop()



    def open_initial_interface(self):
        result = InitialDataInterface()
        result.mainloop()
        dictionary = result.get_data()
        # dictionary -> 'border', 'neighborhood', 'radius', 'initial_data_file_path', 'store_trace_back'
       
        self.set_border(dictionary['border'])
        self.set_neighborhood(dictionary['neighborhood'], dictionary['radius'])
        self.initial_data_file_path = dictionary['initial_data_file_path']
        self.store_trace_back = dictionary['store_trace_back']

        self.__set_data_from_file( initial_data_file_path=dictionary['initial_data_file_path'] )



    def set_initial_state_from_image_and_csv(self):
        # obtiene ruta absoluta del directorio donde esta
        abs_path = os.path.dirname( os.path.abspath(__file__) )
        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'

        folder_path = abs_path + path_separator + 'initialData'
        csv_files = glob.glob(folder_path + "/*.csv")               # obtiene todos los csv,

        tif  = glob.glob(self.initial_data_file_path + '/*.tif')
        tiff = glob.glob(self.initial_data_file_path + '/*.tiff')
        if len(tif + tiff) == 0:
            message = 'There is no ".tif" or ".tiff" file to use as the initial state of the cellular automaton.'
            raise IndexError(message)
        else:
            tif_initial_image = (tif + tiff)[0]

        self.__set_initial_state_image_csv(tif_initial_image, csv_files)
        


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
        if os.path.exists(route_to_image):      # Se comprueba si existe
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
                                
                    writer.writerows(data_list) # Escribe todas las filas en archivo .csv

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

        route_to_image = abs_path + path_separator + 'results'+ path_separator + \
            'iteration_' + str(self.actual_iteration) + '.tif'

        
        if os.path.exists(route_to_image):  # Se comprueba si existe
            return route_to_image
        else:                               # Se crea la imagen
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



    def __set_initial_state_image_csv(self, tif_initial_image, csv_files):
        self.initial_state_route = tif_initial_image

        img = Image.open( tif_initial_image )
        pix = img.load()
        x, y = img.size
        self.width = x
        self.height = y
        matrix = []
        for y in range(0, self.height):
            row_list = []
            for x in range(0, self.width):
                if (len(pix[x, y]) == 3):
                    r, g, b = pix[x, y]
                    state = self.__get_state_from_color(r, g, b, x, y)

                elif (len(pix[x, y]) == 4):
                    r, g, b, a = pix[x, y]
                    state = self.__get_state_from_color(r, g, b, x, y)

                row_list.append({'state': state})
            matrix.append(row_list)

        # leer archivos csv
        if len(csv_files) != 0:
            for route_to_file in csv_files:
                file_name = os.path.basename(route_to_file).split('.')[0]
                if file_name not in self.variables_dict:
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
            malla_aux = []
            x = 0
            for elem in fila:
                variables = elem.copy()
                del variables['state'] 
                c = cell.Cell(self, xpos=x, ypos=y, state=elem['state'], variables=variables)
                malla_aux.append(c)
                x = x+1
                
            malla.append(malla_aux)
            y = y+1

        self.iterations = {}
        self.iterations[0] = malla
        self.actual_iteration = 0
        self.last_iteration_calculated = 0

    

    def __get_state_from_color(self, red:int, green:int, blue:int, xpos:int, ypos:int):
        value = (int(red), int(green), int(blue))

        if value not in list(self.states_color_dict.values()):
            message = 'At the ('  + str(xpos) + ', ' + str(ypos) + ' position, the (' + \
                str(red) + ', ' + str(green) + ', ' + str(blue) + ') ' + \
                'color, is not related to any state in states_color_dict.'
            raise ValueError(message)

        state = list(self.states_color_dict.keys())[list(self.states_color_dict.values()).index(value)] 
        return state



    def __set_data_from_file(self, initial_data_file_path:str):
        if system() == 'Windows':
            path_separator ='\\'
        elif system() == 'Darwin' or system() == 'Linux':
            path_separator ='/'
        
        if initial_data_file_path is None:  # Se busca ./initialData/
            if system() == 'Windows':
                self.initial_data_file_path = '.\\initialData'
            elif system() == 'Darwin' or system() == 'Linux':
                self.initial_data_file_path = './initialData'

      
            if os.path.exists(self.initial_data_file_path): # comprueba que existe carpeta "initialData"

                if os.path.exists(self.initial_data_file_path + path_separator + 'States.py'):   
                    from initialData.States import States
                    self.valid_states = []
                    for s in States:
                        self.valid_states.append(s)
                else:
                    message = '"States.py" file not found in initialData folder.'
                    raise ModuleNotFoundError(message)
                
                if os.path.exists(self.initial_data_file_path + path_separator + 'states_color_dict.py'):   
                    from initialData.states_color_dict import states_color_dict
                    self.states_color_dict = states_color_dict
                else:
                    message = '"states_color_dict.py" file not found in initialData folder.'
                    raise ModuleNotFoundError(message)
                
                if os.path.exists(self.initial_data_file_path + path_separator + 'variables_dict.py'):   
                    from initialData.variables_dict import variables_dict
                    self.variables_dict = variables_dict
                else:
                    self.variables_dict = {}

                if os.path.exists(self.initial_data_file_path + path_separator + 'transition_rule.py'):   
                    from initialData.transition_rule import transition_rule
                    self.set_transition_rule(transition_rule)
                else:
                    self.transition_rule = None

                # extraer, initial_state de archivo Python
                if os.path.exists(self.initial_data_file_path + path_separator + 'initial_state.py'):
                    from initialData.initial_state import initial_state
                    self.set_initial_state(initial_state)
                else:   # cargar estado inicial de csv e imagen
                    csv_files = glob.glob(self.initial_data_file_path + '/*.csv')               # obtiene todos los csv,
                    # obtiene primera imagen .tif o .tiff como estado inicial.
                    tif  = glob.glob(self.initial_data_file_path + '/*.tif')
                    tiff = glob.glob(self.initial_data_file_path + '/*.tiff')
                    if len(tif + tiff) == 0:
                        message = 'There is no "initial_state.py", ".tif" or ".tiff" file to use as the initial state in the initialData folder.'
                        raise IndexError(message)
                    else:
                        tif_initial_image = (tif + tiff)[0]
                    self.__set_initial_state_image_csv( tif_initial_image, csv_files)

            else:   # en caso de que no exista ./initialData
                self.valid_states = []
                self.states_color_dict = {}
                self.variables_dict = None


        else:   # El usuario especifica una ruta inicial diferente a 
            self.initial_data_file_path = initial_data_file_path
            if os.path.exists(self.initial_data_file_path):
                sys.path.append( self.initial_data_file_path)
                if os.path.exists(self.initial_data_file_path + path_separator + 'States.py'):   
                    from States import States
                    self.valid_states = []
                    for s in States:
                        self.valid_states.append(s)
                else:
                    message = '"States.py" file not found in the spicified folder.'
                    raise ModuleNotFoundError(message)
                
                if os.path.exists(self.initial_data_file_path + path_separator + 'states_color_dict.py'):   
                    from states_color_dict import states_color_dict
                    self.states_color_dict = states_color_dict
                else:
                    message = '"states_color_dict.py" file not found in the spicified folder.'
                    raise ModuleNotFoundError(message)
                
                if os.path.exists(self.initial_data_file_path + path_separator + 'variables_dict.py'):   
                    from variables_dict import variables_dict
                    self.variables_dict = variables_dict
                else:
                    self.variables_dict = {}

                if os.path.exists(self.initial_data_file_path + path_separator + 'transition_rule.py'):   
                    from transition_rule import transition_rule
                    self.set_transition_rule(transition_rule)
                else:
                    self.transition_rule = None

                # extraer, initial_state de archivo Python
                if os.path.exists(self.initial_data_file_path + path_separator + 'initial_state.py'):
                    from initial_state import initial_state
                    self.set_initial_state(initial_state)
                else:   # cargar estado inicial de csv e imagen
                    csv_files = glob.glob(self.initial_data_file_path + '/*.csv')               # obtiene todos los csv,
                    # obtiene primera imagen .tif o .tiff como estado inicial.
                    tif  = glob.glob(self.initial_data_file_path + '/*.tif')
                    tiff = glob.glob(self.initial_data_file_path + '/*.tiff')
                    if len(tif + tiff) == 0:
                        message = 'There is no "initial_state.py", ".tif" or ".tiff" file to use as the initial state in the spicified folder.'
                        raise IndexError(message)
                    else:
                        tif_initial_image = (tif + tiff)[0]
                    self.__set_initial_state_image_csv( tif_initial_image, csv_files)

            else:   # No existe el estado inicial dado
                self.valid_states = []
                self.states_color_dict = {}
                self.variables_dict = None
