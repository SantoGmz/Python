#importando desde forma no oriendata a objeto todo de la libreria "turtle"
from turtle import *
#importandon libreria del tiempo
import time
#redimencionando la ventana
screensize(10, 10)
#Titulo de la ventana que se habrira
title("SantosTesting")
#Creando el grafico de la tortuga
shape('turtle')

#tiempo de espera al cargar la ventana para comenzar a dibujar
#time.sleep(4)

#Ciclo for, con este creo una variable, esta aumentara de 1 en 1 hasta llegar a 80
for i in range(80):
 #velocidad a la que se movera, Mientra mas alto menos lento,
    speed(i)

    #esto es para mover la tortuga y poder dibujar
    forward(300)
    right(200)
    forward(300)
    left(300)
    #esto lo utilizo para aumentar el tamaño del pencil
    pensize(i)
    #con esto aumento 1 pixel mas en cada vuelta del bucle para asi poder dibujar mas grande
    i = i + 1
# aqui para que no cierre de forma automatica.
time.sleep(10)

 
