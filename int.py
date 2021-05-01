import matplotlib.pyplot as graf #hay que intalar esta libreria para que grafique asi python3 -m pip install matplotlib
import numpy as np #hay que intalar esta libreria para la parte matematica asi python3 -m pip install numpy

# declaro variables, dos listas para graficar los valores de X & Y, y la variable integral donde se depositara el resultado final
gx = []
gy = []
integral = 0
base = 0.08 # aqui se define la base de cada rectangulo, entre mas pequeña la base mayor resolucion de la integral

for x in np.arange(0,8, base): # la base le da la resolucion de eje x para cada rectangulo
	y = (np.exp(np.sin(x)/(np.exp(x)/x)*x))	# la ecuacion que se esta graficando es (seno(x))^2
	gx.append (x)
	gy.append (y)
	area = (base * y)	# calcula area base por altura
	integral = area + integral  # hace la sumatoria
	print(integral)  # devuelve el resultado de la integral
	graf.stem(gx, gy) # Grafica
	graf.pause(0.0005) # pausa la grafica en 0.05 para ver el proceso

graf.show()
# el area aproximada bajo la curva es de 11.446360991014123 u^2
