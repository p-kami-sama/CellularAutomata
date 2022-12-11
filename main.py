# IMPORTS
import InteractiveAutomata as interactiveAutomata
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders


ia = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_data_file_path='/Users/paul/Desktop/CellularAutomata/1_GameOfLifeData')
ia.set_border(Borders.PERIODIC)
ia.set_neighborhood(Neighborhoods.MOORE)
ia.open_interface()
ia.store_data_in_json()
