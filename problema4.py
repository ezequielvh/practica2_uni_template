

import sys
from collections import defaultdict

def contar_pares(A, n, C):
    frecuencia = defaultdict(int)  # Diccionario para almacenar frecuencias
    count = 0

    for precio in A:
        complemento = C - precio  # Buscamos cuánto falta para llegar a C
        if complemento in frecuencia:  
            count += frecuencia[complemento]  # Se suma cuántas veces ha aparecido el complemento
        frecuencia[precio] += 1  # Se almacena la ocurrencia del precio actual

    return count

def main():
    # Lectura de entrada estándar
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    C = int(input().strip())

    print(contar_pares(A, n, C))

# Caso 1
A = [40, 40, 40]
n = len(A)
C = 80

contar_pares(A, n, C)

# Caso 2
A = [10, 2, 6, 8, 4]
n = len(A)
C = 10

contar_pares(A, n, C)

