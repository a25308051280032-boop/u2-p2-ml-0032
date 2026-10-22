import numpy as np
# Iris Chavez NC 0032
# Ejemplos de numpy   Numerical Python
print("-- Espaciado Linealmente en array -- 0032")
arre = np.linspace(start=0,stop=5,num=5)
print(arre)
print("--  Matriz identidad en 2D array -- 0032")
matrix=np.eye(4)
print(matrix)
print("--  Genera numeros al azar (Aleatorios) en 2D array -- 0032")
print("generar 12 numeros aleatorios")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios 
print(numale)
print("generar 9 numeros aleatorios centre 0 y 1")
numale=np.random.random((3,3)) # genera 9 numeros aleatorios 
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios centre 0 y 20")
arre = np.random.randint(1, 21, size=(3, 3))
print(arre)
print("Iris Chavez NC 0032")