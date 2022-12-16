import Cell as cell

from States import States as s



def transition_rule(c:cell):
    t_vivo = c.get_variable('tiempo_vivo')
    t_muerto = c.get_variable('tiempo_muerto')
    state = None

    if c.get_state() == s.Vivo:
        n = c.count_neighbors_with_state(s.Vivo)
        if n == 2 or n == 3:
            t_vivo +=1
            state = s.Vivo
        else:
            t_muerto +=1
            state = s.Muerto

    else: # c.get_state() == s.Muerto:
        if  c.count_neighbors_with_state(s.Vivo) == 3:
            t_vivo +=1
            state = s.Vivo
        else:
            t_muerto +=1
            state = s.Muerto

    return {'state':state, 'tiempo_vivo': t_vivo, 'tiempo_muerto': t_muerto}

    



# Una célula muerta con exactamente 3 células vecinas vivas "nace" (en el turno siguiente estará viva).
# Una célula viva con 2 o 3 células vecinas vivas sigue viva,
#     en otro caso muere (por "soledad" o "superpoblación").