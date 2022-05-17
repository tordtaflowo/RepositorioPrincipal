#Florencia Korn

with open("lista.txt","r") as lista, open("lista_nueva.txt","w") as lista_nueva:

    for linea in lista:
        linea = linea.split()
        lista_nueva.write(linea[1])
        lista_nueva.write("\n")


#El archivo "lista.txt" muestra un ejemplo de lista de alumnos
