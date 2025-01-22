def jugadores():
    x = 1
    j1_power = []
    while True:
        print(f"Jugador {x}")
        p = input("Introduce la poténcia de los samurais: ")
        if sum(p.split()) != 30:
            print("La Ptotal tiene que sumar 30")
            return
        else:
            x = 2
    



    # print("Equipo 1")
    # while True:
    #     j1 = input("Introduce potencia de los samurai: ")
    #     j1_list = j1.split()
    #     if sum(j1_list) != 30:
    #         print("Error, no suma 30")
    #     else:
    #         print()