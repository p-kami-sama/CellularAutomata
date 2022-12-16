# IMPORTS
import InteractiveAutomata as interactiveAutomata
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders


# from examples.GameOfLifeData.statistics_functions import *
def cosa():
    pass

# obtiene lista de nombres de estadisticos
import examples.GameOfLifeData.statistics_functions as sss
functions_list = [name for name, val in sss.__dict__.items() if callable(val) and  isinstance(val, type(cosa))]

print(functions_list)

for func in functions_list:
    print(func)

func = getattr(sss, 'States')
print( type(func), isinstance(func, type(cosa)))


ia = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_data_file_path='/Users/paul/Desktop/CellularAutomata/examples/GameOfLifeData')
ia.set_border(Borders.PERIODIC)
ia.set_neighborhood(Neighborhoods.MOORE)
ia.open_interface()
ia.store_data_in_json()

# ia2 = interactiveAutomata.InteractiveAutomata()
# ia2.open_initial_interface()
# ia2.open_interface()
# ia2.store_data_in_json()