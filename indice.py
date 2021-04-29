print("Bienvenido a la calculadora v1.0")

i= int(1)
 while i <= 5:
    signo = input("+ = Sumar \n - = Resta \n / = Division \n * = Multiplicacion")
    print(f"Has seleccionado {signo}")

    if signo != "+" and signo != "-" and signo != "/" and signo != "*":
        print(f"lo siento, pero {signo} no es un signo de aritmetica, piensalo bien animal antes de \n escribir un simbolo aritmetico.")
    else:
        print("Excelente!.")
        i+=1



# print("Debes ingresar 2 valores a continuacion:")

# valor1 = int(input("Valor 1: "))
# valor2=int(input("Valor 2: "))

