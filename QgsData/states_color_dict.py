
from celula.States import States


states_color_dict = {
    States.Quemado: (0, 0, 0),          # negro
    States.Combustible: (0, 255, 0),    # verde
    States.Ardiendo: (255, 0, 0),       # rojo
    States.Ignifugo: (0, 0, 255)        # azul
}

    # def __str__(self) -> str:
    #     return str(self.name)

    # def __repr__(self):
    #     return str(self.name)
