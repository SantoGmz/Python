# for letra in "python":
#     if letra=="h":
#         # continue siver para pasar por encima cualquier letra marcada con el if
#         continue

#     print("Viendo la vuelta: " + letra)


nombre = "Pildoras Informaticas"



contador = 0

for i in nombre:
    if i == " ":
        continue

    contador+=1

print(contador)