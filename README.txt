deben instalar estas dos librerias
numpy y matplotlib
asi:

python3 -m pip install matplotlib
python3 -m pip install numpy


para cambiar la resolucion de la integral se puede modificar el tamaño de la base de 0 a 1 . entre mas pequeño el numero mas pequeña la base de cada rectangulo y por lo tanto mayor resolucion en el calculo de la integral

Programacion paralela:
cada nodo se encarga de procesar un segmento de la integral para esto se define una variable limite inicio y otra limite final.