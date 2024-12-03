def saludo():
    i = input()
    ii = i.split()
    n = ii[0]
    k = ii[1]

    if k == '1':
        names = []
        for _ in range(int(n)):
            name = input()
            names.append(name)            
        for name in names:
            print(f"Hola {name}")

    else:
        for i in range(int(n)):
            print("Hola OICV")
saludo()