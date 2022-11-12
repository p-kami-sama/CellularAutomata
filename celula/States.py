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
