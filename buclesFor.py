# email= False
# for i in "SantoGmz@gmail.com":
#     if(i=="@"):
#         email=True
# if email:
#     print("Email es correcto")
# else:
#     print("Email es incorrecto")    


























































































contador=0
miEmail = input("Digita el email que quieres comprobar: ")

for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1    

if contador==2:
    print("Email correcto")
else:
    print("Email incorrecto")    


















