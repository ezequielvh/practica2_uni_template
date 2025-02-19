import sys

def max_subarray_sum(A, n):
    max_global = float('-inf')  # Inicializamos con el menor valor posible
    max_actual = 0  # Inicializamos la suma parcial
    
    for num in A:
        max_actual += num
        if max_actual > max_global:
            max_global = max_actual
        if max_actual < 0:
            max_actual = 0  # Si la suma parcial es negativa, reiniciamos

    return max_global if max_global > 0 else 0  # Si no hay suma positiva, devolvemos 0

def main():
    # Lectura de entrada estándar
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    
    print(max_subarray_sum(A, n))
    
    
 # Caso 1
 
A = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(A)    

max_subarray_sum(A, n)

 # Caso 2
A = [-2, -3, -4, -1, -2, -1, -5, -3]
n = len(A)

max_subarray_sum(A, n)

if __name__ == '__main__':
    main()


