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