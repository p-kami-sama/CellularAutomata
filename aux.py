# # #from initialData.States import States
# # import sys

# # print('1 gato')
# # print('2 gato')
# # print('3 gato')
# # print('4 gato')

# # #print(States.Ardiendo)

# # print('5 gato')

# # from QgsData.variables_dict import variables_dict 
# # # exec('/Users/paul/Desktop/CellularAutomata/aux.py', $output);
# # # print_r($output);

# # # exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'.encode('utf-8')).read())

# # # exec('/Users/paul/Desktop/CellularAutomata/aux.py')
# # # exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'))



# # # exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'.encode('utf-8')).read())

# # # print(sys.path)


# # # diccionario -> buscar Key por value


# # # with open('/Users/paul/Desktop/CellularAutomata/QgsData/info.csv', newline='') as f:
# # #     reader = csv.reader(f)
# # #     data = list(reader)

# # # print(data)



# # project_path = '/Users/paul/Desktop/CellularAutomata'

# # import platform
# # import csv


# # if platform.system() == 'Windows':
# #     route_separator ='\\'
# # elif platform.system() == 'Darwin' or platform.system() == 'Linux':
# #     route_separator ='/'

# # var_dict = {}
# # for name_file_var, var_type in variables_dict.items():
# #     var_list = []
# #     file = project_path+route_separator+'QgsData'+route_separator+name_file_var+'.csv'

# #     with open(file, newline='') as f:
# #         reader = csv.reader(f)
# #         for row in reader:
# #             var_row = []
# #             for elem in row:
# #                 if var_type == 'int':
# #                     elem = int(elem)
# #                 elif var_type == 'float':
# #                     elem = float(elem)
# #                 elif var_type == 'str':
# #                     elem = str(elem)
# #                 elif var_type == 'bool':
# #                     elem = bool(elem)
        
# #                 var_row.append(elem)

# #             var_list.append(var_row)
    
# #     var_dict[name_file_var] = var_list






# # for name_file, var_type in variables_dict.items():
# #     print(name_file, var_type)

# # print(len(variables_dict))


# # print(var_dict)

# from tkinter import *

# root = Tk()
# root.title("Ventana principal")
# root.geometry("300x100")

# ventana_nueva1 = Toplevel()
# ventana_nueva1.geometry("300x200")
# ventana_nueva1.title("Ventana secundaria")

# mainloop()




import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()   # /Users/paul/Desktop/CellularAutomata/initialData

new_file = input("Name file\n")
print('+', file_path)
print('....')
#open_file = open(f"{file_path}\%s.py" % new_file, 'w')