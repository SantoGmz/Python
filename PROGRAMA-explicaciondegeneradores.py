
print("Hablemos de los generadores que tenemos en Python")
print("1-¿Que son generadores? \n 2-Funcionamiento \n 3¿Cual es su utilidad? \n 4-¿Cual es su sintaxis?")

intentos=0

pregunta= int(input("Seleccione: 1/4: -->"))

while pregunta<0 or pregunta>4:
    pregunta= int(input("ERROR: SELECCIONA UN NUMERO DEL 1(UNO) HASTA EL 4(CUATRO), ANIMAL SALVAJE: -->"))
    intentos+=1
    if intentos>2:
        print("Intentalo mas tarde, No estoy en perder el tiempo enseñandole a animales salvajes.")
        break;

if pregunta== 1:
    print("\n*Los generadores son estructuras que extraen valores de una funcion y \n se almacenan en objetos iterables (Que se pueden recorrer). \n")
    print("*Estos valores se almacenan de uno en uno. \n")
    print("*Cada vez que un generador almacena un valor, esta permanece en un estado \n pausado hasta que se solocita el siguiente. Esta caracteristica es conocida como 'suspencion de estado'. \n")
elif pregunta== 2:
    print("Su funcionamiento es...")
    echo
elif pregunta== 3:
    print("Su funcionamiento es...")
elif pregunta== 4:
    print("Su funcionamiento es...")                