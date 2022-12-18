from enum import Enum

class States(str, Enum):

    Hormiga = 'Hormiga'
    Blanco  = 'Blanco'
    Negro   = 'Negro'

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return str(self.name)


