import keyword
import pyautogui as pa
import random
import time as tiempo
import webbrowser as navegador

#ciclo for para moverlo todo durante 10 veces
"""for i in range(10):
    #pa hace referencia a pyautogui, move al movimiento entonces equis y ye va ceparado entre comillas en parentecis para hacer movimientos
    pa.moveTo(x=random.randint(10,1910), y= random.randint(10,1070))
    #esto es para ver la posicion que actualmente se encuentra y asi poder saber donde se movera el mouse"""



navegador.open_new("https://www.youtube.com/")    

tiempo.sleep(5)
#seleccionar el buscador
pa.click(x=613,y=103)

#Lo que buscare
pa.typewrite("anuel aa Check", interval=0.1)

#click en el buscador

pa.click(x=1268, y=104)

tiempo.sleep(2)

#click en la cancion
pa.click(x=629, y=375)


print(pa.position())
