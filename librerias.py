import random

def numAleatorio(num1,num2)
    resultado = random.randint(num1,num2)
    return resultado

respuesta = input("¿Quieres saber tu numero de la suerte? S o N")


while respuesta =! "S" and respuesta != "N" and respuesta =! "s" and respuesta != "n":
    respuesta = input("ERROR: debes digitar S o N:")

if respuesta== "S":
    numAleatorio(1,100)    


