import pandas as pd
import numpy as np
# Arevalo Rafael NC = 0031 Fecha:23/10/26
N_Filas=5
N_Columnas=5
Tag_Columnas=tuple('ABCDE') # etiquetas para las columnas de una tupla 
print(Tag_Columnas)
Matriz=np.random.randint(1, 6, size=(N_Filas, N_Columnas))
print("Genera Matriz de 5 Filas por 5 Columnas")
print("Con numeros aleatorios comprendidos entre 1 y 10")
print(Matriz)
# La variable df es DataFrame
df = pd.DataFrame(Matriz, columns= Tag_Columnas)
print(" ---- La variable o DataFrame ---- NC=0031")
print(df)
print("----Arevalo Rafael NC = 0031----")