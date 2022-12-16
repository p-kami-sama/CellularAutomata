import Automata as automata
import Cell as cell
import typing


class Statistic:
    def __init__(self, automata:automata, check_function, message:str='', variables_to_print:typing.List[str]=[]):
        self.message = message
        self.check_function = check_function
        self.automata = automata
        self.variables_to_print = variables_to_print

    def valid(self, c:cell):
        return self.check_function(c)

    def get_json_entry(self, c:cell):

        if self.variables_to_print == []:
            data = {
                    'state': c.get_state(),
                    'message': self.message,
                }
        else:
            vars_info = {}

            for var in self.variables_to_print:
                vars_info[var] = c.get_variable(var)

            data = {
                'message': self.message,
                'state': c.get_state(),
                'variables': vars_info
            }

        return data
