import pandas as pd

def isNaN(num):
    return num != num

#------------------------------------------------
#------------------------------------------------

df = pd.read_csv("data/param.csv", sep=";", skip_blank_lines=False)

#print(df)

parametros = []

for fila, columna in df.iterrows():

    #if fila==1:

    fila = []

    for i in range(len(columna)):

        fila.append(columna[i])


    parametros.append(fila)


#print(parametros)

#------------------------------------------------
#------------------------------------------------

df2 = pd.read_csv("data/data.csv", sep=";", skip_blank_lines=False)

print(df2)

data = []

for fila, columna in df2.iterrows():

    #if fila==1:

    fila = []

    for i in range(len(columna)):

        fila.append(columna[i])


    data.append(fila)


#print(data)

#------------------------------------------------
#------------------------------------------------

import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    for i in data:

        edad = i[0]
        peso = i[1]
        estado = '';

        #P3;P10;P25;P50;P75;P90

        for ii in parametros:
            if ii[0]==edad:

                if (peso < ii[1]):
                    estado = '< P3'

                if (peso == ii[1]):
                    estado = 'P3'

                if (peso > ii[1]) and (peso < ii[2]):
                    estado = 'P3 - P10'

                if (peso == ii[2]):
                    estado = 'P10'

                if (peso > ii[2]) and (peso < ii[3]):
                    estado = 'P10 - P25'

                if (peso==ii[3]):
                    estado = 'P25'

                if (peso > ii[3]) and (peso < ii[4]):
                    estado = 'P25 - P50'

                if (peso==ii[4]):
                    estado = 'P50'

                if (peso > ii[4]) and (peso < ii[5]):
                    estado = 'P50 - P75'

                if (peso==ii[5]):
                    estado = 'P75'

                if (peso > ii[5]) and (peso < ii[6]):
                    estado = 'P75 - P90'

                if (peso==ii[6]):
                    estado = 'P90'

                if (peso>ii[6]):
                    estado = '> P90'


        i.append(estado)
        writer.writerow(i)



#end 
