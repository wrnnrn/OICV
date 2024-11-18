# Input
l1_input = input()
l1 = l1_input.split()
v = int(l1[1])
k = int(l1[2])

l2 = input()
n = list(map(int, l2.split()))
# Media aritmética
p_vector = 1
vector_final = []

def media_aritmetica():
    for i in range(int(v)):
        global p_vector
        resultado = ((n[p_vector-1]) + p_vector + (n[p_vector-1]))/k
        p_vector += 1
        vector_final.append(round(resultado))

media_aritmetica()

print(vector_final)