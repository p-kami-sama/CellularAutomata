
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