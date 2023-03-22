from pprint import pprint
from functions import functions


data_dict = read_data('winequality.csv')


#split main

data_dict = read_data('winequality.csv')
white_data_dict, red_data_dict = split(data_dict)

print(f"{len(white_data_dict)} blanco {len(red_data_dict)} rojo")

print(white_data_dict['dato1'])

#read_data main
data2_dict = read_data('winequality.csv')
alcohol_lista = reduce(data_dict, 'alcohol')
print(alcohol_lista)