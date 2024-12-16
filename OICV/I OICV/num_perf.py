def inicio():
    t = int(input) # Primer numero = tamaño de la secuencia de nº (t) mayor a 0; 
    if t <= 0:
        exit()
    
    numeros = []
    for i in range(t):
        aux = input()
        if aux < 1000:
            numeros.append(aux)
