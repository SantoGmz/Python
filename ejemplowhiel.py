email = input("Introduce tu email.")

for arroba in email:
    if arroba == "@":
        arroba=True
        break;

else:
    arroba = False

print(arroba)        