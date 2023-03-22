import csv

def read_data(filename):
    
    data_dict = {}
    counter = 1

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if all(row): 
                data_dict[f'dato{counter}'] = {
                    'fixed acidity': float(row[0]),
                    'volatile acidity': float(row[1]),
                    'citric acid': float(row[2]),
                    'residual sugar': float(row[3]),
                    'chlorides': float(row[4]),
                    'free sulfur dioxide': float(row[5]),
                    'total sulfur dioxide': float(row[6]),
                    'density': float(row[7]),
                    'PH': float(row[8]),
                    'sulphates': float(row[9]),
                    'alcohol': float(row[10]),
                    'quality': int(row[11])
                }
                counter += 1

        if counter <= 10:
            raise ValueError("El archivo tiene menos de 10 líneas con valores en todos los atributos. Revise su contenido.")
            
    return data_dict


def read_data(filename):





def split(data):
    white_data_dict = {}
    red_data_dict = {}
    
    for key, value in data.items():
        if value (type) == 'white'
            white_data_dict = value
        elif value (type) == 'red'
    
     return white_data_dict, red_data_dict

#Manera tradicional
#resultado = []
#for i in valores:
 # resultado.append(i * 2)
#print(resultado) 

def reduce(data, attribute):
    if attribute not in list(data['dato1']):
        raise ValueError(f"No existe en el diccionario")


        result = []
        for data in data.values():
            result.append(attribute)
            
        return result


def silhouette(lista1, lista2):

    total = sum(lista1)
    return total/len(lista1)



