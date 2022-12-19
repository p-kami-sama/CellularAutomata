from enum import Enum

class States(str, Enum):
   
    Combustible = 'Combustible'
    Ardiendo = 'Ardiendo'
    Quemado = 'Quemado'
    Ignifugo = 'Ignifugo'

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return str(self.name)


