print("Programa de becas año 2021")

distancia= int(input("¿Aque distancia vive?: "))
hermanos = int(input("¿Cuantos hermanos tiene?: "))
salario = int(input("¿Cual es su salario?: "))

if distancia>40 and hermanos>2 and salario<=20000:
    print("Beca aceptada por ser pobre")
else:
    print("Beca rechazada, Otras personas la nesecitan mas que tu, Kbron")    