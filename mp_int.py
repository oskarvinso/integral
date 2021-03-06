import matplotlib.pyplot as graf #hay que intalar esta libreria para que grafique asi python3 -m pip install matplotlib
import numpy as np #hay que intalar esta libreria para la parte matematica asi python3 -m pip install numpy
import multiprocessing as mpi # se importa la libreria del multiproceso
areas = []
def integrar(limi, limf, node):
	#declaro variables, dos listas para graficar los valores de X & Y, y la variable integral donde se depositara el resultado final
	gx = []
	gy = []
	integral = 0
	base = 0.1 # aqui se define la base de cada rectangulo, entre mas pequeña la base mayor resolucion de la integral
	for x in np.arange(limi, limf, base): # Limi y limf es el semgmento de la curva, la base del eje x para cada rectangulo
		y = (np.exp(np.sin(x)/(np.exp(x)/x)*x))	# la ecuacion que se esta graficando
		gx.append (x)
		gy.append (y)
		area = (base * y)	# calcula area base por altura
		integral = area + integral  # hace la sumatoria
		print("Segmento procesado por el nodo {}, area para este segmento {}".format(node, integral))  # devuelve el resultado de la integral hasta el momento
		graf.stem(gx, gy) # Grafica
		graf.pause(0.0005) # pausa la grafica en 0.05 para ver el proceso
	return(integral)

# aqui se define que segmento de la integral va a procesar cada nodo definiendo el limite de inicio y de final
if __name__ == '__main__':
	nodo1 = mpi.Process(target = areas.append(integrar(0.01,4,1)))
	nodo1.start()
	nodo2 = mpi.Process(target = areas.append(integrar(4.01,8,2)))
	nodo2.start()
	nodo1.join()
	nodo2.join()
	#Finalmente hacemos la sumatoria total de las areas calculadas por cada nodo
	print ("El total del area bajo la curva es de ", sum(areas))
	graf.show()
