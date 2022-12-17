# IMPORTS
import InteractiveAutomata as interactiveAutomata
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders

import Automata as automata



game_of_life = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_data_file_path='./examples/GameOfLifeData')
game_of_life.clear_results_file()
game_of_life.add_all_statistics()
game_of_life.set_border(Borders.PERIODIC)
game_of_life.set_neighborhood(Neighborhoods.MOORE)
game_of_life.open_interface()
game_of_life.store_data_in_json()



# ia2 = interactiveAutomata.InteractiveAutomata()
# ia2.open_initial_interface()
# ia2.open_interface()
# ia2.store_data_in_json()