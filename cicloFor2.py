# a=0
# b=10

# for i in range(a,b,3):
#     print(f"Valor de la variable {i}")

valido=False

email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
        
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")            