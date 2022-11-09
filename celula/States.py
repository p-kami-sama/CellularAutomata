from enum import Enum

class States(str, Enum):

    Quemado = 1
    Combustible = 2
    Ardiendo = 3
    Ignifugo = 4



    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return str(self.name)
