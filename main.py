
import sys
import csv


# IMPORTS
import InteractiveAutomata as interactiveAutomata

from initialData.transition_rule import transition_rule_GameOfLife
from initialData.States import States
from celula.statistics_functions import *

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders
from initialData.initial_state import initial_state_GameOfLife




print('Se inicia el automata')




ia = interactiveAutomata.InteractiveAutomata(store_trace_back=True, initial_state=None)


ia.set_border(Borders.FIXED, States.Muerto)
ia.set_neighborhood(Neighborhoods.MOORE, 1)

# ia.set_initial_state(initial_state_GameOfLife)
ia.set_initial_state_from_image_and_csv()

ia.set_transition_rule(transition_rule_GameOfLife)
ia.add_statistic(statistic_function_count_10_iterations, '', ['tiempo_vivo', 'tiempo_muerto'])


ia.open_initial_interface()

# ia.open_interface()
# ia.store_data_in_json()



