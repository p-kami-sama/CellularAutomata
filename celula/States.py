from enum import Enum

class States(str, Enum):

    Quemado = 'Quemado'
    Combustible = 'Combustible'
    Ardiendo = 'Ardiendo'
    Ignifugo = 'Ignifugo'



    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return str(self.name)


states_color_dict = {
    States.Quemado: (255, 255, 255),
    States.Combustible: (0, 255, 0),
    States.Ardiendo: (255, 0, 0),
    States.Ignifugo: (0, 0, 255)
}