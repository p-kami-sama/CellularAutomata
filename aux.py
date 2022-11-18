#from celula.States import States
import sys

print('1 gato')
print('2 gato')
print('3 gato')
print('4 gato')

#print(States.Ardiendo)

print('5 gato')


# exec('/Users/paul/Desktop/CellularAutomata/aux.py', $output);
# print_r($output);

# exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'.encode('utf-8')).read())

# exec('/Users/paul/Desktop/CellularAutomata/aux.py')
# exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'))



# exec(open('/Users/paul/Desktop/CellularAutomata/aux.py'.encode('utf-8')).read())

# print(sys.path)


# diccionario -> buscar Key por value












import csv

with open('/Users/paul/Desktop/CellularAutomata/QgsData/info.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
