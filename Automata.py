import math as math
import json
import typing

import Cell as cell
import Statistic as statistic

from celula.States import States

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders


class Automata:

    def __init__(self, width:int, height:int, store_trace_back:bool=False ):
        print('MALLLLLLLLLL')

        self.width = width      # ancho
        self.height = height    # altura

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





    def set_initial_state(self, mat:list):
        self.height = len(mat)
        self.width = len( mat[0])
        malla = []
        y = 0
        for fila in mat:
            mallaAux = []
            x = 0
            for elem in fila:

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

                elif isinstance(elem, States):
                    c = cell.Cell(self, xpos=x, ypos=y, state=elem, variables={})
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


    # neighborhoods:   von_Neumann , Moore , custom
    # devuelve el antiguo tipo de vecindad
    def set_neighborhood(self, new_neighborhood_type:Neighborhoods, radius_or_list_of_desp:typing.Union[int, typing.List[ typing.Tuple[int, int] ], None] = 1) -> Neighborhoods:
        old_neighborhood_type = self.neighborhood

        if not isinstance(new_neighborhood_type, Neighborhoods):
            message = 'ERROR: ' +str(new_neighborhood_type) + ' is not an accepted type of neighborhood. ' + \
                'The types of neighborhood accepted are: '
            first = True
            for n in Neighborhoods:
                if first:
                    message += '"' + str(n.name) + '"'
                    first = False
                else:
                    message += ', "' + str(n.name) + '"'
            message += '.'
            raise ValueError(message)

        if new_neighborhood_type == Neighborhoods.CUSTOM:
            # Comprueba que se ha pasado una lista
            if not isinstance(radius_or_list_of_desp, list):
                msg = 'ERROR: If the neighborhood type is "custom" the second parameter must be a list of integer pairs.'
                raise ValueError(msg)
            self.neighborhood_list = radius_or_list_of_desp
        else:
            # Comprueba que se ha pasado un entero mayor que 0
            if (not isinstance(radius_or_list_of_desp, int)) or (radius_or_list_of_desp <= 0):
                msg = 'ERROR: If the neighborhood type is "von_Neumann" or "Moore" the second parameter must be an integer greater than 0.'
                raise ValueError(msg)

            if new_neighborhood_type == Neighborhoods.VON_NEUMANN: # como un rombo
                self.neighborhood_list = self.von_Neumann_neighborhood(radius_or_list_of_desp)
            elif new_neighborhood_type == Neighborhoods.MOORE:   # cuadrado
                self.neighborhood_list = self.moore_neighborhood(radius_or_list_of_desp)

        self.neighborhood = new_neighborhood_type
        return old_neighborhood_type


    # cambia el tipo de frontera, y devuelve el tipo anterior
    # border:         border: periodic , fixed , reflective , adiabatic
    def set_border(self, new_border_type:Borders, fixed_cell:cell=None) -> Borders:
#    def set_border(self, new_border_type:Borders, fixed_cell:typing.Union[str, typing.Type[cell.Cell] ]=None) -> typing.Union[Borders, None]:

        if not isinstance(new_border_type, Borders):
            message = 'ERROR: ' +str(new_border_type) + ' is not an accepted type of border. ' + \
                'The types of border accepted are: '
            first = True
            for b in Borders:
                if first:
                    message += '"' + str(b.name) + '"'
                    first = False
                else:
                    message += ', "' + str(b.name) + '"'
            message += '.'
            raise ValueError(message)

        old_border_type = self.border
        self.border = new_border_type

        if new_border_type == Borders.FIXED:
            if isinstance(fixed_cell, States):
                self.fixed_cell = cell.Cell(self, -1, -1, fixed_cell)
            elif isinstance(fixed_cell, cell.Cell):
                self.fixed_cell = fixed_cell
           
            else:
                message = 'ERROR: the second parameter "fixed_cell" must be an object of type Cell '+\
                    'or part of the States enumeration.'
                raise ValueError(message)

        return old_border_type


    def set_transition_rule(self, transition_rule):
        self.transition_rule = transition_rule

    # Borra todas las iteraciones guardadas (excepto la 0)
    def reset_automata(self):
        for elem_key in range(1, self.last_iteration_calculated+1):
            if elem_key != 0:
                del self.iterations[elem_key]
        
    
        # Pone los contadores a 0
        self.data = {}
        self.last_iteration_calculated = 0
        self.actual_iteration = 0


    def get_cell(self, x:int, y:int, iteration:int=None)-> cell:
        if (not isinstance(x, int)) or (x < 0) or (not isinstance(y, int)) or (y < 0):
            msg = 'ERROR: The first and second parameters "x" and "y" must be an integers greater than or equal to 0.'
            raise ValueError(msg)
        elif iteration == None:
            return self.iterations[self.actual_iteration][y][x]
        elif (not isinstance(iteration, int)) or (iteration < 0) or (self.last_iteration_calculated < iteration):
            msg = 'ERROR: The third parameter "iteration" must be an integer greater than or equal to 0 and '+\
                'less than or equal to "last_iteration_calculated".'
            raise ValueError(msg)
        else:
            return self.iterations[iteration][y][x]


    # ['periodic' , 'fixed' , 'reflective' , 'adiabatic']
    def get_neighbour_cell(self, orig_x:int, orig_y:int, desp_x:int, desp_y:int) -> cell:

        if self.border == Borders.PERIODIC: # (ini + (desp % size))%size)
            if desp_x < 0:
                obj_x = (orig_x + (desp_x %  self.width)) %  self.width
            else:
                obj_x = (orig_x + desp_x) %  self.width

            if desp_y < 0:
                obj_y = (orig_y + (desp_y %  self.height)) %  self.height
            else:
                obj_y = (orig_y + desp_y) %  self.height

            return self.get_cell(obj_x, obj_y)

        elif self.border == Borders.FIXED:
            obj_x = orig_x + desp_x
            obj_y = orig_y + desp_y
            if (obj_x < 0) or (self.width <= obj_x) or \
                (obj_y < 0) or (self.height <= obj_y):
                return self.fixed_cell
            else:
                return self.get_cell(obj_x, obj_y)

        elif self.border == Borders.REFLECTIVE:
            obj_x = self.reflexion_lineal(orig_x, desp_x, self.width)
            obj_y = self.reflexion_lineal(orig_y, desp_y, self.height)
            return self.get_cell(obj_x, obj_y)

        elif self.border == Borders.ADIABATIC:    # usa la celula del borde como células vecinas
            obj_x = orig_x + desp_x
            obj_y = orig_y + desp_y
            if obj_x >= self.width:
                obj_x = self.width -1
            elif obj_x < 0:
                obj_x = 0
            if obj_y >= self.height:
                obj_y = self.height -1
            elif obj_y < 0:
                obj_y = 0

            return self.get_cell(obj_x, obj_y)


# Avanza el autómata una iteración
    def next(self):
        if self.actual_iteration < self.last_iteration_calculated:
            # significa que ya se ha calculado previamente esa iteración y se tiene guardada
            pass
        else: # self.actual_iteration == self.last_iteration_calculated
            malla = []
            for fila in self.iterations[self.actual_iteration]:
                fila_nueva = []
                for elem in fila:
                    result_transition_rule = self.transition_rule(elem)

                    if isinstance(result_transition_rule, States):
                        new_state = result_transition_rule
                        c = cell.Cell(self, xpos=elem.xpos, ypos=elem.ypos, state=new_state, variables=elem.variables.copy())

                    elif type(result_transition_rule) is dict: # se reescriben las variables adecuadamente
                        if  'state' in result_transition_rule.keys():
                            new_state = result_transition_rule['state']
                            del result_transition_rule['state']
                            c = cell.Cell(self, xpos=elem.xpos, ypos=elem.ypos, state=new_state, variables=result_transition_rule)
                        else:
                            message = 'ERROR: If the result of transition_rule is a dictionary, it must have a key called '\
                                    '"state", with the state that the cell will have after applying the transition rule.'
                            raise ValueError(message)
                    
                    fila_nueva.append(c)

                malla.append(fila_nueva)

            self.iterations[self.actual_iteration+1] = malla
            self.last_iteration_calculated += 1

            # Se añaden estadísticos a self.data
            if self.store_trace_back:
                dict_iteration = {}
                states_counter_dict = {}
                for s in States:
                    states_counter_dict[s.name] = 0

                #AQUI SE PUEDEN AÑADIR ESTADISTICOS GLOBALES
                for fila in self.iterations[self.actual_iteration]:
                    x = 0
                    for elem in fila:
                        states_counter_dict[elem.state.name] +=1
                        dict_elem = {}
                        for statistic_id, statistic in self.statistics.items():
                            if statistic.valid(elem):
                                dict_elem[statistic_id] = statistic.get_json_entry(elem)
                        if (dict_elem != {}):
                            elem_key = '('+str(elem.xpos)+', '+str(elem.ypos)+')'
                            dict_iteration[elem_key] = dict_elem

                dict_aux = {'Cell state counter': states_counter_dict}
                dict_aux.update(dict_iteration)
                self.data[self.actual_iteration+1] = dict_aux
                            
        self.actual_iteration += 1
        return self.actual_iteration


    def run_iterations(self, num_iterations:int, print_data:bool=False):
        self.reset_automata()
        for iteration in range(0, num_iterations):
            self.next()

        if print_data:
            print( json.dumps(self.data, sort_keys=True, indent=4) )


# Devuelve una matriz con los estados de la iteración especificada.
# Si 'iteration es None, devuelve los estados de la matrix actual
    def get_matrix_state(self, iteration:int=None) -> list:

        if iteration == None:
            it = self.actual_iteration
        elif (not isinstance(iteration, int)) or (iteration < 0) or (self.last_iteration_calculated < iteration):
            msg = 'ERROR: The parameter "iteration" must be None, or an integer greater than or equal to 0 and '+\
                'less than or equal to "last_iteration_calculated".'
            raise ValueError(msg)
        else:
            it = iteration
        mat = []
        for fila in self.iterations[it]:
            row = []
            for elem in fila:
                row.append(elem.state)
            mat.append(row)
        return mat



    def add_statistic(self, check_function, message:str, variables_to_print:typing.List[str]) -> int:
        # Buscar otra forma de asignar id
        id = 0
        for index in range(1, len(self.statistics)+2):
            if not index in self.statistics.keys():
                id = index
                break

        self.statistics[id]=statistic.Statistic(self, check_function, message, variables_to_print)
        return id


# Devuelve True si se ha eliminado el estadistico correctamente y False cuando no hay un estadistico con el id dado
    def delete_statistic(self, id:int) -> bool:
        if id in self.statistics.keys():
            del self.statistics[id]
            return True
        else: # en caso de que var no exista
            return False


    def store_data_in_json(self, route:str='data.json'):
        with open(route, 'w') as file:
            json.dump(self.data, file, indent=4)


# Funciones auxiliares
    def moore_neighborhood(self, radius:int)-> list:
        l = []
        for x in range (-radius, radius+1):
            for y in range (-radius, radius+1):
                l.append( (x, y) )

        l.remove( (0, 0) )
        return l

    def von_Neumann_neighborhood(self, radius:int):
        l = []
        for x in range (-radius, radius+1):
            for y in range (-radius, radius+1):
                if abs(x) + abs(y) <= radius:
                    l.append( (x, y) )

        l.remove( (0, 0) )
        return l


    def reflexion_lineal(self, ini:int, desp:int, size:int) -> int:
        size_1 = size - 1
        if 0 <= ini+desp and ini+desp < size:
            return ini+desp

        else:
            if desp > 0: # positivo
                despAux = desp-(size_1 - ini)
                if math.trunc( despAux / size_1 ) % 2 == 0:    # par
                    return size_1 - (despAux % size_1)
                else: # impar
                    return despAux % size_1

            else: # negativo
                despAux = -desp - ini
                if math.trunc( despAux / size_1 ) % 2 == 0:    # par
                    return despAux % size_1
                else: # impar
                    return size_1 - (despAux % size_1 )
