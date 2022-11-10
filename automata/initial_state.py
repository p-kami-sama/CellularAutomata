from celula.States import States

initial_state = [
    [{'state': States.Combustible, 'variables': {'Sol': 'rojo', 'Luna': 'azul'}}, States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Ignifugo, States.Combustible, States.Combustible, States.Combustible, States.Combustible],
    [States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Ignifugo, States.Combustible, States.Ardiendo, States.Ardiendo, States.Ardiendo],
    [States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Ignifugo, States.Combustible, States.Ardiendo, States.Combustible, States.Ardiendo],
    [States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Quemado, States.Combustible, States.Combustible, States.Ardiendo, States.Ardiendo, States.Ardiendo],
    [States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Quemado, States.Combustible, States.Combustible, States.Combustible, States.Combustible, States.Combustible],
]

initial_state2 = [
  [{'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Ignifugo}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}],
    [{'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Ignifugo}, {'state': States.Combustible}, {'state': States.Ardiendo}, {'state': States.Ardiendo}, {'state': States.Ardiendo}],
    [{'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Ignifugo}, {'state': States.Combustible}, {'state': States.Ardiendo}, {'state': States.Combustible}, {'state': States.Ardiendo}],
    [{'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Quemado}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Ardiendo}, {'state': States.Ardiendo}, {'state': States.Ardiendo}],
    [{'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Quemado}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}, {'state': States.Combustible}],
]