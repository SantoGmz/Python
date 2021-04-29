"""Las excepciones son los errores que ocurren durante la ejecucion del programa. La sintaxis
del codigo es correcta pero durante la ejecucion ha ocurrido "algo inesperado""" 

"""Este tipo de errores de ejecucion dse pueden controlasr para que la ejecuciondel programa continue. 
es lo que se conoce como manejo o  control de excepciones."""

#intentar hacerlo.

def result(op1,op2):
    #con esto puedo trabajar como el if y elif, try para intentar hacer algo y except para si no puede hacerlo
    #que se habia mandado hacer no se cierre el programa sino que captura el error y el programa funcionaria correctamente
    try:
        resulFinal= op1/op2
        return print(resulFinal)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion erronea"
    
op1 = int(input("Valor 1"))
op2 = int(input("Valor 2"))    

result(op1,op2)    