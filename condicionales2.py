# nombre = input("Cual es tu nombre:")
# edad = int(input("edad:"))

# def entrada(edad,nombre):
    
#     if edad<18:
#         return(print("Lo sentimos, Quizas deberias volver despues ", nombre))        
#     elif edad>100:
#         return(print("Lo sentimos,", nombre, "Pero la edad",edad,", es invalida"))    
#     else:
#         return(print("Bienvenido al club ", nombre))

# entrada(edad,nombre)        

nota= int(input("Nota del alumno: "))

if nota<5:
    print("insuficiente")
elif nota<6:
    print("Suficiente")
elif nota<7:
    print("Bien")
elif nota<9:
    print("Notable")   
else:    
    print("Sobresaliente")
