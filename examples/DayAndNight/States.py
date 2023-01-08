from enum import Enum

class States(str, Enum):

    Day = 'Day'
    Night = 'Night'

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return str(self.name)


