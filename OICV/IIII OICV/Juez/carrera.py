def solitario():
   posicion = 0
   for indice, elemento in enumerate(tablero)

def carrera():
   while True:
       # Input
       input_principal = input("")
       ip_list = input_principal.split()
       n = ip_list[0]
       c = ip_list[1]
       b = ip_list[2]
       t = input()
       tablero = t.split()
       mazo = []
       for i in range(b):
           m = input()
           mazo.append(m)
    
       # Hay que sacar cartas_finales
       if n <=0:
           exit()

       if n == 1:
           solitario()
       if n >= 2:
           multijugador()

    
carrera()
