
# def get_path(func):  
#      if type(func).__name__ == 'function' : 
#          return func.__code__.co_filename
#      else: 
#          raise ValueError("'func' must be a function") 


# print( get_path('itransition_rule') )





print('/Users/paul/Desktop/PRUEBA')

# import os

# os.chdir("**Put here the directory where you have the file with your function**")

# from file import function

# os.chdir("**Put here the directory where you were working**")



# esto sirve para a partir de la carpeta,
#  lee el archivo adecuado (a partir del nombre)
import sys

sys.path.append('/Users/paul/Desktop/PRUEBA')

from GATITOS import gato

gato()

import os 
print( os.path.exists('./initialData/') )


print('.......')
from initialData.States import States


from enum import Enum

estado = States.Muerto
print( type(estado))
print(estado)
print( isinstance(estado, States), isinstance(estado, Enum))
print( issubclass(type(estado), Enum))

print ('->',  issubclass(type(estado), Enum) and issubclass(type(estado), str))


elem = 0
print(  issubclass(type(elem), str) and issubclass(type(elem), Enum)  )



# Automata  -> States.py                                    OK
# Cell      -> States.py    / SOLO Para controles de error  OK
# InitialDataInterface    ->  ----              
# InteractiveAutomata ->  ----
# Interface   ->  from variables_dict.py    OK?

# CANVIAR TODA CREACION DE OBJETO Cell

import math as math
a = math.trunc(5/2)
b=math.trunc(2.99)
c= int(5/2)
d = int(2.99)
e=5//2
print(a, b, c, d, e)