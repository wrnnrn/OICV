import math

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Función para encontrar los primeros k primos mayores que n
def primos_consecutivos(n, k):
    primos = []
    num = n + 1
    while len(primos) < k:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

# Leer la cantidad de casos
t = int(input())

# Procesar cada caso
for _ in range(t):
    # Leer los valores n y k
    n, k = map(int, input().split())
    
    if k == 0:
        # Verificar si n es primo
        if es_primo(n):
            print("SI")
        else:
            print("NO")
    else:
        # Encontrar los k primos consecutivos mayores que n
        primos = primos_consecutivos(n, k)
        print(" ".join(map(str, primos)))
