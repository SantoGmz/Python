import turtle

#Agregando a una variable para que se a mas corto a la hora de llamarlo
f =turtle.Turtle()

#configurando el fondo de bg/fondo
turtle.bgcolor("black")
#tamaño del lapiz/pencil
turtle.pensize(2)
#velocidad
turtle.speed(0)

#cilo que siempre se ejecutara
while (True):
    #ciclo for, donde creo 1 circulo
    for i in range(6):
        #creando un array, en este lenguaje se llaman listas, y array dimencionales son tuplas
        for colors in["red", "blue","yellow", "white", "gray", "green", "orange"]:
            #para darle el color desde el ciclo de arriba
            turtle.color(colors)
            #tamaño del circulo
            turtle.circle(100)
            #para mover el circulo uno al lado del otro
            turtle.left(10)
#para ocultar la tortuga            
turtle.hideturtle()
#para que se mantenga habierto siempre funciona hasta que el usuario finalice el programa
turtle.mainloop()        




