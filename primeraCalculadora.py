operacion=int(input("¿Que operacion realizaras? \n 1-Suma \n 2-Resta \n 3-Division \n 4-Multipliacaion: \n Operacion --> "))

# Creando una funcion
def aritmetica(num1, num2, operacion):
    
    if operacion ==1:
        resultado = num1+num2
        return resultado
    elif operacion==2:
        resultado = num1-num2
        return resultado        
    elif operacion==3:
        resultado = num1/num2
        return resultado   
    elif operacion==4:
        resultado = num1*num2
        return resultado   


# Creando una condicional que comprueba que la variable operacion funciona correctamente
if operacion>0 and operacion<5:
    print("Digite 2 numeros:")
    
    # creando las variables para almacenar ambos valores
    num1= int(input("Valor 1:--> "))
    num2= int(input("Valor 2:--> "))
    
    # enviando los parametros a la funcion despues de ver sido comprobado
    print("el resultado es:",aritmetica(num1,num2, operacion))
    
    # si da algun error se ejecutaran las siguentes 2 lienas de codigo
else:
    print("Lo sentimos, No has seleccionado una operacion aritmetica")    


print(input("preciona cualquier tecla"))