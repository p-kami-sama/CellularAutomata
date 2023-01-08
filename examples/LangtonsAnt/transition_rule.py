from States import States as s



def transition_rule(cell):
    if cell.get_state() == s.Hormiga:
        colorBlanco = cell.get_variable('colorBlanco')
        if colorBlanco:
            return {
                'state': s.Negro, 
                'colorBlanco': (not colorBlanco),
                'orientacion_hormiga': '-'
            }
        else:
            return {
                'state': s.Blanco, 
                'colorBlanco': (not colorBlanco),
                'orientacion_hormiga': '-'
            }


    elif cell.any_neighbor_has_state(s.Hormiga):   # Comprovar si la hormiga acaba en esta casilla
        xpos, ypos = cell.get_pos()
        celula_N = cell.automata.get_neighbour_cell(xpos, ypos, 0, -1)

        celula_E = cell.automata.get_neighbour_cell(xpos, ypos, 1, 0)

        celula_S = cell.automata.get_neighbour_cell(xpos, ypos, 0 , 1)

        celula_O = cell.automata.get_neighbour_cell(xpos, ypos, -1, 0)


        if celula_N.get_state() == s.Hormiga and (
            (celula_N.get_variable('colorBlanco') and celula_N.get_variable('orientacion_hormiga') == 'E') or
            (not celula_N.get_variable('colorBlanco') and celula_N.get_variable('orientacion_hormiga') == 'O')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': cell.get_variable('colorBlanco'),
                'orientacion_hormiga': 'S'
            }

        elif celula_E.get_state() == s.Hormiga and (
            (celula_E.get_variable('colorBlanco') and celula_E.get_variable('orientacion_hormiga') == 'S') or
            (not celula_E.get_variable('colorBlanco') and celula_E.get_variable('orientacion_hormiga') == 'N')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': cell.get_variable('colorBlanco'),
                'orientacion_hormiga': 'O'
            }

        elif celula_S.get_state() == s.Hormiga and (
            (celula_S.get_variable('colorBlanco') and celula_S.get_variable('orientacion_hormiga') == 'O') or
            (not celula_S.get_variable('colorBlanco') and celula_S.get_variable('orientacion_hormiga') == 'E')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': cell.get_variable('colorBlanco'),
                'orientacion_hormiga': 'N'
            }

        elif celula_O.get_state() == s.Hormiga and (
            (celula_O.get_variable('colorBlanco') and celula_O.get_variable('orientacion_hormiga') == 'N') or
            (not celula_O.get_variable('colorBlanco') and celula_O.get_variable('orientacion_hormiga') == 'S')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': cell.get_variable('colorBlanco'),
                'orientacion_hormiga': 'E'
            }
        else:
            return {
                'state': cell.get_state(), 
                'colorBlanco': cell.get_variable('colorBlanco'),
                'orientacion_hormiga': cell.get_variable('orientacion_hormiga')
            }



    else: # casilla normal sin hormiga se conserva
        return {
            'state': cell.get_state(), 
            'colorBlanco': cell.get_variable('colorBlanco'),
            'orientacion_hormiga': cell.get_variable('orientacion_hormiga')
        }


### Regla
# Si hormiga
#   1
#     Si casilla Blanca -> Giro horario
#     Si casilla Negra -> Giro antihorario
#   2
#     cambiar color de casilla y mover hormiga
# Sino
#    Se mantiene igual
