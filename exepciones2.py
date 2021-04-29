#https://www.youtube.com/watch?v=HH3c6ZBvSx8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=22
#Creo un ciclo infinito
while True:
    #try: es para intentar hacer una cosa
    try:
        #Creando las variable y convirtiendolas en numeros enteras a la vez pidiendole que me digite 2 numeros
        val1 = int(input("valor 1: "))
        val2 = int(input("valor 2 :"))
        #para saltar desde aqui si todo los numeros son correctos
        break
    #Esto es la exepceion, en este caso es error de valores
    except ValueError:
        #esto es lo que dire si los valores agregados no son correctos
        print("Los valores introducidos no son correctos.")    
        #puedo hacer varias excepciones
    except ZeroDivisionError:

        print("No se puede dividir entre zero")         
        #finally es para hacer las ordenes que envie a pesar de que halla algun error
    #puedo cerrar bases de datos con finally porque hace lo que sea aunque halla un error en el programa
    finally:
        print("")        

print("Siguio hasta aca")
#https://youtu.be/HH3c6ZBvSx8?t=558