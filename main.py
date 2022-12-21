# IMPORTS
import InteractiveAutomata as interactiveAutomata
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders




# Cada bloque de codigo crea un automata celular a partir de cada uno de los archivos de ejemplo
# NOTA: evitar usar más de un autómata a la vez, dado que se generan conflictos con las rutas.


#####   Game of Life

# game_of_life = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_data_file_path='./examples/GameOfLifeData')
# game_of_life.clear_results_file()
# game_of_life.add_all_statistics()
# game_of_life.set_border(Borders.PERIODIC)
# game_of_life.set_neighborhood(Neighborhoods.MOORE)
# game_of_life.open_interface()
# game_of_life.store_data_in_json()



#####   Incendio

# import sys
# sys.path.append('./examples/incendio')
# from States import States as IncendioStates

# incendio = interactiveAutomata.InteractiveAutomata(True, './examples/incendio')
# incendio.clear_results_file()
# incendio.add_all_statistics()
# incendio.set_border(Borders.FIXED, IncendioStates.Ignifugo)
# incendio.set_neighborhood(Neighborhoods.MOORE)
# incendio.open_interface()



#####   Brian'n Brain

# brians_brain = interactiveAutomata.InteractiveAutomata(False, './examples/BriansBrain')
# brians_brain.clear_results_file()
# brians_brain.set_border(Borders.PERIODIC)
# brians_brain.set_neighborhood(Neighborhoods.MOORE, 1)
# brians_brain.open_interface()



#####   Langton's ant

# langtons_ant = interactiveAutomata.InteractiveAutomata(False, './examples/LangtonsAnt')
# langtons_ant.clear_results_file()
# langtons_ant.add_all_statistics()
# langtons_ant.set_border(Borders.PERIODIC)
# langtons_ant.set_neighborhood(Neighborhoods.VON_NEUMANN)
# langtons_ant.open_interface()