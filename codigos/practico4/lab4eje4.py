# laboratorio 4 - ejercicio 4

import matplotlib.pyplot as plt 
import numpy as np 

# cargar los datos desde la dirección web (url) del repositorio
# por el formato de los datos hay que considerar el argumento
# delimiter: hay que explicitar que las columnas estan separadas por comas
# usecols: solo leemos la columna 1 (segunda) que son los datos que necesitamos (y para evitar problemas con las fechas)
datos = np.loadtxt("https://raw.githubusercontent.com/gbrlm/anfamaf2024/main/datos/covid_italia.csv", delimiter=',', usecols=1)
x = np.arange(len(datos))

# ajuste y = a*exp(b*x) --> ln(y) = ln(a) + b*x
y = np.log(datos)
coef = np.polyfit(x,y,1)

plt.plot(x,datos,'.')
plt.plot(x,np.exp(coef[1])*np.exp(coef[0]*x))
plt.show()