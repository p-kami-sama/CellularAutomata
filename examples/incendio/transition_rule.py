import Cell as cell
from States import States

def aux_estado_ardiendo(c:cell) -> bool:
    return c.get_state() == States.Ardiendo

def transition_rule(c:cell):

    state = c.get_state()
    combustible = c.get_variable('combustible')
    tiempo_de_regeneracion = c.get_variable('tiempo_de_regeneracion')
    intensidad_del_fuego = c.get_variable('intensidad_del_fuego')


    if c.get_state() == States.Quemado:
        if tiempo_de_regeneracion <= 1:
            vecinos_Ignifugo = c.count_neighbors_with_state(States.Ignifugo)
            vecinos_Quemado = c.count_neighbors_with_state(States.Quemado)

            state = States.Combustible
            combustible = 10 + 3* (vecinos_Ignifugo + vecinos_Quemado)
            tiempo_de_regeneracion = 0


        else:
            tiempo_de_regeneracion -= 1
        
    elif c.get_state() == States.Combustible:
        if c.any_neighbor_has_state(States.Ardiendo):
            state = States.Ardiendo
            intensidad_del_fuego = c.count_neighbors_with_state(States.Ardiendo)
        else:
            pass
    elif c.get_state() == States.Ardiendo:
        suma_intensidad_del_fuego_de_vecinos = sum( c.get_values_of_variable_from_neighbors_that_satisfy('intensidad_del_fuego', aux_estado_ardiendo) )
        combustible = combustible - (intensidad_del_fuego + suma_intensidad_del_fuego_de_vecinos )
        if combustible <= 0:
            state = States.Quemado
            combustible = 0
            tiempo_de_regeneracion = 10
            intensidad_del_fuego = 0   

    else: # c.get_state() == States.Ignifugo
        pass
        


    return {
        'state': state,
        'combustible': combustible,
        'tiempo_de_regeneracion': tiempo_de_regeneracion,
        'intensidad_del_fuego': intensidad_del_fuego,
    }

    
# Las celulas Ignifugas se conservan en el tiempo.
# Si una celda con combustible tiene un vecino Ardiendo, pasa a estar Ardiendo.
#   La intensidad del fuego, es la cantidad de tiempo que la casilla lleva ardiendo.
# Una celda Ardiendo reduce su combustible en (su intensidad_del_fuego + la suma de intensidad_del_fuego de los vecinos Ardiendo)
# Si una celda Ardiendo se queda con combustible, pasa a Quemado.
# Una celda Quemada pasa a Combustible tras 10 iteraciones. Y Obtine un combustible igual (10 + 3 * (numero de vecinos Ignifugos o Quemado))

