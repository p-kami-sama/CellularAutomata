import Automata as automata
import typing


class Statistic:
    def __init__(self, automata:automata, check_function, message:str='', variables_to_print:typing.List[str]=[]):
        self.message = message
        self.check_function = check_function
        self.automata = automata
        self.variables_to_print = variables_to_print

    def valid(self, cell):
        return self.check_function(cell)

    def get_json_entry(self, cell):

        data = { 'state': cell.get_state() }

        if (self.message is not None) and (self.message != ''):
            data['message'] = self.message

        if (self.variables_to_print is not None) and (self.variables_to_print != []):
            vars_info = {}
            for var in self.variables_to_print:
                vars_info[var] = cell.get_variable(var)
                data['variables'] = vars_info

        return data
