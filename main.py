# IMPORTS
from InteractiveAutomata import InteractiveAutomata
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders


# game_of_life = InteractiveAutomata(store_trace_back=True, initial_data_file_path='./examples/GameOfLifeData')
# game_of_life.clear_results_file()
# game_of_life.add_all_statistics()
# game_of_life.set_border( Borders.PERIODIC )
# game_of_life.set_neighborhood( Neighborhoods.MOORE, 1 )
# game_of_life.open_interface()
# game_of_life.store_data_in_json()



#####   Incendio

# import sys
# sys.path.append('./examples/incendio')
# from States import States as IncendioStates

# incendio = InteractiveAutomata(True, './examples/incendio')
# incendio.clear_results_file()
# incendio.add_all_statistics()
# incendio.set_border(Borders.FIXED, IncendioStates.Ignifugo)
# incendio.set_neighborhood(Neighborhoods.MOORE)
# incendio.open_interface()



#####   Brian'n Brain

# brians_brain = InteractiveAutomata(False)
# brians_brain.clear_results_file()
# brians_brain.set_border(Borders.PERIODIC)
# brians_brain.set_neighborhood(Neighborhoods.MOORE, 1)
# brians_brain.open_interface()


#####   Langton's ant

# langtons_ant = InteractiveAutomata(False, './examples/LangtonsAnt')
# langtons_ant.clear_results_file()
# langtons_ant.add_all_statistics()
# langtons_ant.set_border(Borders.PERIODIC)
# langtons_ant.set_neighborhood(Neighborhoods.VON_NEUMANN)
# langtons_ant.open_interface()


#####   Load automata from file
# automata_from_file = InteractiveAutomata()
# automata_from_file.clear_results_file()
# automata_from_file.open_initial_interface()
# automata_from_file.open_interface()
# automata_from_file.store_data_in_json()
