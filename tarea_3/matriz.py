import numpy as np

matriz = np.random.randint(100, size=(5,10))

print("Matriz:")
print(matriz)

max = np.max(matriz)
pos_max = np.where(matriz == max)
min = np.min(matriz)
pos_min = np.where(matriz == min)

print("El número máximo es", max, "y se encuentra en la posición", pos_max)
print("El número mínimo es", min, "y se encuentra en la posición", pos_min)

matriz_ordenada = np.sort(matriz, axis=None)[::-1].reshape((5,10))

print("Matriz ordenada :")
print(matriz_ordenada)
