# i=1

# while i<=10:
#     print("ejecucion " + str(i))
#     i=i+1
    

# print("Termino la ejecucion")


edad= int(input("Cual es tu edad: "))

while edad<0:
    print("ERROR: REPITA SU EDAD: ")
edad= int(input("Cual es tu edad: "))
    
print("Puedes pasar")
print(f"Edad es {edad}")    

edad=int(input("Introduce tu edad por favor: "))

while edad<=0 or edad>130:
    print("has introducido una edad erronea. Vuelve a intentarlo")
    edad=int(input("Intruce tu edadad: "))



print("Gracias por colaborar. Puedes pasar")
print("edad del aspirante " + str(edad)) 

