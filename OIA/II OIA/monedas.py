def main():
    monedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    n = int(input("Indique la cantidad de céntimos: "))
    def calculo(n, monedas):
        n = n/100.0
        l = []
        for moneda in monedas:
            while n >= moneda:
                n -= moneda
                l.append(moneda)
        
        print(f"Monedas usadas {l}")

    calculo(n, monedas)

if __name__ == "__main__":
    main()