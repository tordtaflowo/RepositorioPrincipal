#Florencia Korn

with open("empleados.txt","r") as empleados, open("correos.txt","w") as correos:

    for linea in empleados:
        correos.write(linea)
        linea = linea.lower()
        linea = linea.split()
        correos.write(linea[1][0])
        correos.write(linea[2][0])
        correos.write(linea[0])
        if len(linea) == 4:
            correos.write("@gerenciaempresa.cl")
        else:
            correos.write("@empresa.cl")
        correos.write("\n")
        correos.write("\n")
    
