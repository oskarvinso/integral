import matplotlib.pyplot as graf #hay que intalar esta libreria para que grafique asi python3 -m pip install matplotlib
import numpy as np #hay que intalar esta libreria para la parte matematica asi python3 -m pip install numpy
import multiprocessing as mpi # se importa la libreria del multiproceso
areas = []
sumatoria = 0
def integrar(limi, limf, node):
	#declaro variables, dos listas para graficar los valores de X & Y, y la variable integral donde se depositara el resultado final
	gx = []
	gy = []
	integral = 0
	base = 0.1 # aqui se define la base de cada rectangulo, entre mas pequeña la base mayor resolucion de la integral
	for x in np.arange(limi, limf, base): # Limi y limf es el semgmento de la curva, la base del eje x para cada rectangulo
		y = (np.exp(np.sin(x)/(np.exp(x)/x)*x))	# la ecuacion que se esta graficando es (seno(x))^2/((x)^2/x)(x)
		gx.append (x)
		gy.append (y)
		area = (base * y)	# calcula area base por altura
		integral = area + integral  # hace la sumatoria
		print("segmento procesado por el nodo ", node "resultado hasta ahora ", integral)  # devuelve el resultado de la integral hasta el momento
		graf.stem(gx, gy) # Grafica
		graf.pause(0.0005) # pausa la grafica en 0.05 para ver el proceso
	return(integral)

# aqui se define que segmento de la integral va a procesar cada nodo definiendo el limite de inicio y de final
nodo1 = mpi.Process(target = areas.append(integrar(0,4,1)))
nodo2 = mpi.Process(target = areas.append(integrar(4,8,2)))
#nodo3 = mpi.Process(target=integrar)
#nodo4 = mpi.Process(target=integrar)

#se inicializan los nodos
nodo1.start()
nodo2.start()
#nodo3.start()
#nodo4.start()

#Finalmente hacemos la sumatoria total de las areas calculadas por cada nodo
for i in range (0,len(areas),1):
	sumatoria = areas[i] + sumatoria

print ("El total del area bajo la curva es de ", sumatoria)
graf.show()
