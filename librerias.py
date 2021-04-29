import random



def numAleatorio(num1,num2):
    resultado = random.randint(num1,num2)
    return resultado

respuesta = input("¿Quieres un numero de la suerte? S/N --> ")


while respuesta != "S" and respuesta != "N" and respuesta != "s" and respuesta != "n":
    respuesta = input("ERROR: debes digitar 'S' o 'N':")


#el or, es como si respuesta es igual a "S" o igual a "s"
if respuesta == "S" or respuesta == "s":
    print("tu numero de la suerte es:", str(numAleatorio(1,100)))    
else:
    print("Vuelve cuando quieras un numero aleatorio")

