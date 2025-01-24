import numpy as np

# Crear un array
array = np.array([1, 2, 3, 4])
print(array * 2)  # [2, 4, 6, 8]



a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)  # [11, 22, 33, 44]

matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])
print(np.dot(matriz_a, matriz_b))  # Producto matricial

datos = np.array([10, 20, 30, 40, 50])
print(np.mean(datos))  # Media: 30.0
print(np.std(datos))   # Desviación estándar

numeros_aleatorios = np.random.rand(5)  # Genera 5 números entre 0 y 1
print(numeros_aleatorios)

