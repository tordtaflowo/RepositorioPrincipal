print("EJEMPLO:")
print("La suma de los multiplos de 3 y 5 menores a 10 es 23 \n")

numero_e = 1
L_e = []

while numero_e < 10:
    if numero_e % 3 == 0:
        L_e.append(numero_e)
    if numero_e % 5 == 0:
        L_e.append(numero_e)
    numero_e += 1

L_e = list(set(L_e))

suma_e = sum(L_e)

L_e.sort()

print("Los multiplos de 3 y 5 menores a 10 son:" ,L_e)
print("La suma de estos multiplos es:" ,suma_e)



print("\n\n\nSe busca la suma de todos los multiplos de 3 y 5 menores a 1000 \n")

numero = 1
L = []

while numero < 1000:
    if numero % 3 == 0:
        L.append(numero)
    if numero % 5 == 0:
        L.append(numero)
    numero += 1

L = list(set(L))

suma = sum(L)

print("La suma de los multiplos de 3 y 5 menores a 1000 es:" ,suma)
