def main():
    n = input(" ")
    medicamentos, maleta = n.split()
    print(f"{medicamentos} {maleta}")

    if medicamentos == 5:
        m1 = input()
        volumen1, precio1, minimo1 = m1.split()

        m2 = input()
        volumen2, precio2, minimo2 = m2.split()

        m3 = input()
        volumen3, precio3, minimo3 = m3.split()

        m4 = input()
        volumen4, precio4, minimo4 = m4.split()

        m5 = input()
        volumen5, precio5, minimo5 = m5.split()

    if medicamentos == 4:
        m1 = input()
        volumen1, precio1, minimo1 = m1.split()

        m2 = input()
        volumen2, precio2, minimo2 = m2.split()

        m3 = input()
        volumen3, precio3, minimo3 = m3.split()

        m4 = input()
        volumen4, precio4, minimo4 = m4.split()

    if medicamentos == 3:
        m1 = input()
        volumen1, precio1, minimo1 = m1.split()

        m2 = input()
        volumen2, precio2, minimo2 = m2.split()

        m3 = input()
        volumen3, precio3, minimo3 = m3.split()

    if medicamentos == 2:
        m1 = input()
        volumen1, precio1, minimo1 = m1.split()

        m2 = input()
        volumen2, precio2, minimo2 = m2.split()

    if medicamentos == 1:
        m1 = input()
        volumen1, precio1, minimo1 = m1.split()       


    def calculo():
    # Formula = n
    #           ∑ Vi * Xi
    #           i=1     


    # def info_medicamentos():
    #     for i in range(0, medicamentos):
    #         info = input()
    #         volumen, precio, minimo = info.split()
    #         medicamento+i = [volumen, precio, minimo]
            

        

if __name__ == "__main__":
    main()