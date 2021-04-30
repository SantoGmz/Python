#https://www.youtube.com/watch?v=dLH-oay4Bts&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=23

def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edad negativas")
        
        #raise ZeroDivisionError("No se permiten edad negativas") - Estos sirven para crear mensajes de errores, Tambien puedo declararlos
        #raise miPropioError("No se permiten edad negativas")


    if edad <20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<56:
        return "eres maduro"        
    elif edad<100:
        return "Cuidate.."        

print(evaluaEdad(21))        


#https://youtu.be/dLH-oay4Bts?t=243