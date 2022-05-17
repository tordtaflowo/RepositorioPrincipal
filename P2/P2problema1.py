import random

class personaje:
    def __init__(self,nombre,ataque,resistencia,velocidad,vida,precision):
        self.nombre = nombre
        self.ataque = ataque
        self.resistencia = resistencia
        self.velocidad = velocidad
        self.vida = vida
        self.precision = precision
        
    def daño(self,per):
        if(random.random() <= (self.precision - per.velocidad) / 100):
            atacar = abs(self.ataque // per.resistencia)
            per.vida -= atacar
            print(self.nombre,"ataca!\n")
        else:
            print(per.nombre,"ha esquivado el golpe!\n")

j1 = int(input("eliga el primer personaje: \n 1)Gurdy \n 2)Greed \n 3)Ultra Pestilence \n 4)Hush \n 5)Delirium \n"))
j2 = int(input("eliga el segundo personaje: \n 1)Gurdy \n 2)Greed \n 3)Ultra Pestilence \n 4)Hush \n 5)Delirium \n"))

gurdy = personaje('Gurdy',1000,70,20,100,200)
greed = personaje('Greed',1000,55,40,100,150)
pestilence = personaje('Ultra Pestilence',1400,50,25,100,100)
hush = personaje('Hush',1100,60,30,100,250)
delirium = personaje('Delirium',1200,50,45,100,150)

if j1 == 1:
    j1 = gurdy
elif j1 == 2:
    j1 = greed
elif j1 == 3:
    j1 = pestilence
elif j1 == 4:
    j1 = hush
elif j1 == 5:
    j1 = delirium

if j2 == 1:
    j2 = gurdy
elif j2 == 2:
    j2 = greed
elif j2 == 3:
    j2 = pestilence
elif j2 == 4:
    j2 = hush
elif j2 == 5:
    j2 = delirium


def pelea(j1,j2):
    if(j1.velocidad > j2.velocidad):
        print(j1.nombre,"es mas rapido y comienza la batalla!\n")
        golpea = j1
        recibe = j2
    elif(j1.velocidad < j2.velocidad):
        golpea = j2
        recibe = j1
        print(j1.nombre,"es mas rapido y comienza la batalla!\n")
    while(j1.vida > 0 and j2.vida > 0):
        print(j1.nombre,"tiene",j1.vida,"de vida!",j2.nombre,"tiene",j2.vida,"de vida!")
        golpea.daño(recibe)
        golpea,recibe = recibe,golpea
    print("Ganador:",recibe.nombre)

print("Comienza la batalla!\n")
pelea(j1,j2)

## algunas lineas de codigo fueron extraidas del pdf subido por el profesor en classroom
