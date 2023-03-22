import csv

def read_data(filename):
    data_dict = {}
    counter = 1
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if '' not in row:
                data_dict['dato' + str(counter)] = {
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
                
    return data_dict
