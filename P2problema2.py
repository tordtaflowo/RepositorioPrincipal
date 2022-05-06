import numpy as np

imagen = np.array([[[58,23,125],[150,0,255,],[0,0,0],[14,0,99]],
[[0,0,200],[34,25,0],[0,65,0],[8,0,45]],
[[58,0,1],[70,25,0],[0,80,165],[255,255,255]]])

print("la imagen inicial es: \n",imagen)

def invertir_imagen(imagen):
        imagen = 255 - imagen
        return imagen

inversa = invertir_imagen(imagen)

print("\n \n la imagen inversa es: \n",inversa)

def rotar_derecha(imagen):
        imagen = np.rot90(imagen)
        imagen = np.rot90(imagen)
        imagen = np.rot90(imagen)
        return imagen

rotada = rotar_derecha(imagen)

print("\n \n la imagen rotada es: \n",rotada)
