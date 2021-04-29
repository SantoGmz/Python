"""
def generaPares(limite):
    num=1

    miLista=[]

    while num<limite:
    
        miLista.append(num*2)

        num=num+1

    return miLista

print(generaPares(10))        

"""

#Creando el generador

def generaPares(limite):
    #Creando la variable de comienzo como 1
    num=1
    #Ciclo while donde digo que mientras numero sea menor que el limite que envie se siga ejecutando
    while num<limite:
        #para crear el objeto
        yield num*2
        #Aqui para que se siga aumentando el valor y tenga algun fin en una futura vuelta
        num=num+1
#Creando una lista con lo que me devuelva la funcion
devuelvePares=generaPares(10)

#con el ciclo for, doy recorrido para revisar toda la lista y verificar todo lo que se encuentre aqui dentro
"""for i in devuelvePares:
    print(i)"""

#con la palabra reservada llamada "next()", Devuelve el siguiente valor de una lista, por el ejemplo si la lista tiene 2,3,4,5 y escribo next 2 veces, devolverá el numero 2 y el numero 3
#next dice, "Se lo que estoy haciendo bro, Tranquis yo llevo la cuenta no te preocupes"
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))