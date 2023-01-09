import Automata as automata

from typing import Any, List, Tuple
from enum import Enum

class Cell:
    def __init__(self, automata:automata, xpos:int, ypos:int, state:Any, variables:dict=None):
        if variables is None:
            variables = dict()
            
        self.automata = automata
        if state not in self.automata.valid_states:
            message = 'A cell with state ' + str(state)+\
                ' cannot be created because it is not included in the States enumeration.'
            raise ValueError(message)

        self.state = state
        self.xpos = xpos
        self.ypos = ypos
        self.variables = variables

    # imprime la celula
    def __str__(self) -> str:
        s = 'xpos: '+str(self.xpos)+', ypos: '+str(self.ypos)+ \
            ', state: '+str(self.state) +', variables: '+str(self.variables)
        return s
    
    def __repr__(self):
        return self.__str__()


    def get_pos(self) -> Tuple[int, int]:
        pos = self.xpos, self.ypos
        return pos


    def get_state(self) -> Enum:
        return self.state


    def set_state(self, new_state:Enum) -> Any:
        if new_state not in self . automata . valid_states:
            message = 'The given state is not included in the "valid_states" list.'
            raise ValueError(message)
        else:
            self.state = new_state


    # Apartir del nombre, obtiene el valor de la variable, en caso de no existir devuelve None
    def get_variable(self, variable_name:str) -> Any:
        if variable_name in self.variables:
            return self.variables[variable_name]
        else: # en caso de que var no exista
            return None

    # asigna el valor variable_value, a la variable con nombre variable_name y devuelve su antiguo valor
    # en caso de no existir previamente la añade a la lista de variables y devuelve None
    def set_variable(self, variable_name:str, variable_value) -> Any:
        if variable_name in self.variables:
            aux = self.variables[variable_name]
            self.variables[variable_name] = variable_value
            return aux
        else:   # devuelve None si no existia previamente
            self.variables[variable_name] = variable_value
            return None




# funciones a nivel de Cell que contactarána a Automata para obtener la informacion que requieren

    def get_automata_num_cell(self) -> int:
        return self.automata.get_num_cell()



#   obtener lista de estados de todos los vecinos
    def get_list_of_states_of_all_neighbors(self) -> List[Enum]:
        lista = []
        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            lista.append(elem.state)
        return lista

# state
    def any_neighbor_has_state(self, state:Enum) -> bool:
        if state not in self.automata.valid_states:
            message = 'The given state is not included in the enumeration of states'
            raise ValueError(message)

        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if elem.state == state:
                return True
        return False

    def all_neighbours_has_state(self, state:Enum)-> bool:
        if state not in self.automata.valid_states:
            message = 'The given state is not included in the enumeration of states.'
            raise ValueError(message)
            
        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if elem.state != state:
                return False
        return True

    def count_neighbors_with_state(self, state:Enum) -> int:
        if state not in self.automata.valid_states:
            message = 'The given state is not included in the enumeration of states.'
            raise ValueError(message)

        contador = 0
        for x, y in self.automata.neighborhood_list:
            if state == self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y).state:
                contador += 1

        return contador


# variables
    def get_values_of_variable_from_all_neighbors(self, variable_name:str) -> List[Any]:
        list_of_values = []
        for x, y in self.automata.neighborhood_list:
            variable_value = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y).get_variable(variable_name)
            list_of_values.append(variable_value)
        
        return list_of_values


    def get_values_of_variable_from_neighbors_that_satisfy(self, variable_name:str, func) -> List[Any]:
        list_of_values = []
        for x, y in self.automata.neighborhood_list:
            celula = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if func(celula):
                list_of_values.append( celula.get_variable(variable_name) )
        return list_of_values

# condition
    def all_neighbours_satisfy(self, func)-> bool:
        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if not func(elem):
                return False
        return True

    def any_neighbor_satisfy(self, func) -> bool:
        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if func(elem):
                return True
        return False

    def count_neighbors_satisfy(self, func) -> int:
        contador = 0
        for x, y in self.automata.neighborhood_list:
            elem = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if func(elem):
                contador += 1
        return contador

    def get__neighbors_that_satisfy(self, func) -> list:
        list_of_neighbors = []
        for x, y in self.automata.neighborhood_list:
            celula = self.automata.get_neighbour_cell(self.xpos, self.ypos, x, y)
            if func(celula):
                list_of_neighbors.append( celula )
        return list_of_neighbors

