import Cell as cell
from States import States as s


def funcion(c:cell):
    return c.get_state() == s.Hormiga

def get_nueva_orientacion(orientacion_hormiga:str,  colorBlanco:bool):
    if colorBlanco: # Giro Horario
        if orientacion_hormiga == 'N':
            return 'E'
        elif orientacion_hormiga == 'E':
            return 'S'
        elif orientacion_hormiga == 'S':
            return 'O'
        else: # orientacion_hormiga == 'O'
            return 'N'
    else:
        if orientacion_hormiga == 'N':
            return 'O'
        elif orientacion_hormiga == 'E':
            return 'N'
        elif orientacion_hormiga == 'S':
            return 'E'
        else: # orientacion_hormiga == 'O'
            return 'S'



def transition_rule(c:cell):
    if c.get_state() == s.Hormiga:
        colorBlanco = c.get_variable('colorBlanco')
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


    elif c.any_neighbor_has_state(s.Hormiga):   # Comprovar si la hormiga acaba en esta casilla
        xpos, ypos = c.get_pos()
        celula_N = c.automata.get_neighbour_cell(xpos, ypos, 0, -1)

        celula_E = c.automata.get_neighbour_cell(xpos, ypos, 1, 0)

        celula_S = c.automata.get_neighbour_cell(xpos, ypos, 0 , 1)

        celula_O = c.automata.get_neighbour_cell(xpos, ypos, -1, 0)


        if celula_N.get_state() == s.Hormiga and (
            (celula_N.get_variable('colorBlanco') and celula_N.get_variable('orientacion_hormiga') == 'E') or
            (not celula_N.get_variable('colorBlanco') and celula_N.get_variable('orientacion_hormiga') == 'O')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': c.get_variable('colorBlanco'),
                'orientacion_hormiga': 'S'
            }

        elif celula_E.get_state() == s.Hormiga and (
            (celula_E.get_variable('colorBlanco') and celula_E.get_variable('orientacion_hormiga') == 'S') or
            (not celula_E.get_variable('colorBlanco') and celula_E.get_variable('orientacion_hormiga') == 'N')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': c.get_variable('colorBlanco'),
                'orientacion_hormiga': 'O'
            }

        elif celula_S.get_state() == s.Hormiga and (
            (celula_S.get_variable('colorBlanco') and celula_S.get_variable('orientacion_hormiga') == 'O') or
            (not celula_S.get_variable('colorBlanco') and celula_S.get_variable('orientacion_hormiga') == 'E')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': c.get_variable('colorBlanco'),
                'orientacion_hormiga': 'N'
            }

        elif celula_O.get_state() == s.Hormiga and (
            (celula_O.get_variable('colorBlanco') and celula_O.get_variable('orientacion_hormiga') == 'N') or
            (not celula_O.get_variable('colorBlanco') and celula_O.get_variable('orientacion_hormiga') == 'S')):
            return {
                'state': s.Hormiga, 
                'colorBlanco': c.get_variable('colorBlanco'),
                'orientacion_hormiga': 'E'
            }
        else:
            return {
                'state': c.get_state(), 
                'colorBlanco': c.get_variable('colorBlanco'),
                'orientacion_hormiga': c.get_variable('orientacion_hormiga')
            }



    else: # casilla normal sin hormiga se conserva
        return {
            'state': c.get_state(), 
            'colorBlanco': c.get_variable('colorBlanco'),
            'orientacion_hormiga': c.get_variable('orientacion_hormiga')
        }


### Regla
# 1 Si hormiga
#     Si casilla Blanca -> Giro horario
#     Si casilla Negra -> Giro antihorario
# 2
#     cambiar color de casilla y mover hormiga
