#Florencia Korn

x = open("lista.txt")

lineas = x.readlines()
for linea in lineas:
    linea = linea.replace(" " ,"\n")
    print(linea)

x.close()

#El archivo "lista.txt" muestra un ejemplo de lista de alumnos
