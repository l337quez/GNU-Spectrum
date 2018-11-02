# import math
# import pandas as pd

# with open('test.csv') as csvarchivo:
    # entrada = csv.reader(csvarchivo)
    # for reg in entrada:
        # print(reg)  # Cada línea se muestra como una lista de campos
        
        ###################
# with open(r'i.csv','r') as f:

	# data = f.read().splitlines()

	# data.pop(0)
	
	
# for u in data:

	# linea = u.split(';')
	# print(linea)


# df = pd.DataFrame(columns = ['i0','i'])
# df.to_csv('test.csv')
# print (df)

import pandas as pd
import math
from matplotlib import pyplot as plt
plt.rcParams['toolbar'] = 'toolmanager'
from matplotlib.backend_tools import ToolBase, ToolToggleBase


#importante para hacer media y mas en padas
#https://blog.adrianistan.eu/2017/11/04/estadistica-python-media-mediana-varianza-percentiles-parte-iii/

pieces = []
for num in [1, 2]:
    s = pd.read_csv('File%d.csv' % num) # your directory
    pieces.append(s)
newcsv = pd.concat(pieces, axis=1) # this will yield multiple columns
newcsv.to_csv('newcsv.csv')
#grabamos los cambios del data frame en el archivo
df = pd.read_csv('newcsv.csv') # your directory
#definimos cabeceras
df.columns = ['#', 'i0','i']
#eliminamos la primera columa de conteo
df.drop(df.columns[[0]], axis=1, inplace=True)
#grabamos los cambios del data frame en el archivo
df.to_csv('newcsv.csv')


#todoo
#T=df['i']+3*['i']
# T = df['i'] / df(['i0']).transform(prod)
# df=df.assign(transmitancia=T.values)
transmitancia=[]
for index, row in df.iterrows():
	transmitancia.append((row.i0 / row.i)*100)
df=df.assign(transmitancia=transmitancia)
print(transmitancia)
df.to_csv('newcsv.csv')


# Graficando
plt.title('Transmitancia')
plt.grid(True)
#plt.ylabel('LDR')
plt.plot(transmitancia, 'ro-', label='Degrees F')       #plot the temperature
plt.plot(transmitancia, label='Degrees F')       #plot the temperature
plt.legend(loc='upper left')                    #plot the legend
plt.show()









