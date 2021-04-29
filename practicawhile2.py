# Importa el metodo math y todas sus funciones
import math 


print("Programa de calculo de raiz cuadrada")

# Alamcenar el numero para sacar la raiz cuadrada
numero= int(input("Introduce un numero por favor"))

# Crear un contador de vueltas que pasa el contador
intentos=0 


# Las veces que se ejecutara el programa si el numero es menor que 0 que se pidio al principio
while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

# Si los intentos son erroneos 2 veces entonces se ejecuta este if que
# quiere decir con breack que el programa se cerrará
    if intentos ==2:
        print("Has consumido demasiados intentos, el programa ha finalizado")
        break;

# Aqui vuelve a ejecutar la linea para que ponga un numero mayor que 0
    numero= int(input("Introduce un numero por favor"))
    if numero<0:
        # Aqui van aumentanto los intentos de 1 en 1, a = a+a como que aumenta lo que tiene mas lo que se le agrege
        intentos=intentos+1

# Si todo es correcto pasara aqui y no por el breack
if intentos <2:
    solucion=math.sqrt(numero)        
    print("La raiz cuadrada de " + str(numero) + " es "+ str(solucion))