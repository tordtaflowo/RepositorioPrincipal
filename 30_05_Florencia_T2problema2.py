#Florencia Korn

nombre1 = "Francisco"
adn1 = "AJDFNRGEYCDGFRTMQXJR"

nombre2 = "Ignacio"
adn2 = "CHTAJDFNRG"

nombre3 = "Francia"
adn3 = "DFFJHCCDMRTIAHDCRLGH"


class Extraterrestre:
    def __init__(self,adn,nombre):
        self.adn = adn
        self.nombre = nombre


def Mutacion (Extraterrestre,adn):
    if len(Extraterrestre.adn) < 20:
        return ("True (El ADN tiene menos de 20 letras)")
    elif any([Extraterrestre.adn[i] == Extraterrestre.adn[i + 1] for i in range(len(Extraterrestre.adn)-1)]):
        return ("True (El ADN contiene 2 letras iguales seguidas)")
    elif len(Extraterrestre.adn) >= 20:
        return ("False")
    else:
        return("False")

Extraterrestre.adn = adn1
print("Ejemplo 1: \n")
print("Nombre:" ,nombre1)
print("ADN:" ,adn1)
print("¿El ADN tiene mutacion?: " ,Mutacion(Extraterrestre,adn1))

Extraterrestre.adn = adn2
print("\nEjemplo 2: \n")
print("Nombre:" ,nombre2)
print("ADN:" ,adn2)
print("¿El ADN tiene mutacion?: " ,Mutacion(Extraterrestre,adn2))

Extraterrestre.adn = adn3
print("\nEjemplo 3: \n")
print("Nombre:" ,nombre3)
print("ADN:" ,adn3)
print("¿El ADN tiene mutacion?: " ,Mutacion(Extraterrestre,adn3))


#Parte del codigo para saber si hay 2 letras iguales seguidas fue extraido de: https://es.acervolima.com/python-multiplica-los-elementos-consecutivos-en-la-lista/
