


import numpy as np

def construir_polinomio(S):
    N = len(S)
    extraterrestres = []
    
    # Identificar las raíces (los números de los extraterrestres)
    for i in range(N):
        if S[i] == 'A':  # Los extraterrestres tienen raíces en 2(i+1)
            extraterrestres.append(2 * (i + 1))
    
    D = len(extraterrestres)  # El grado del polinomio es igual al número de extraterrestres
    if D == 0:
        return [0], [1]  # Polinomio constante P(x) = 1
    
    # Construir el polinomio con raíces en los extraterrestres
    polinomio = np.poly(extraterrestres).astype(int).tolist()
    
    return [D], polinomio  # Devuelve el grado y los coeficientes en orden decreciente

def main():
    S = input().strip()
    grado, coeficientes = construir_polinomio(S)
    
    # Imprimir la salida en el formato requerido
    print(grado[0])
    print(" ".join(map(str, coeficientes)))


# Caso 1
S = 'HHH'
construir_polinomio(S)

# Caso 2
S = 'AHHA'
construir_polinomio(S)

# Caso 3
S = "AHHHAH"
construir_polinomio(S)

