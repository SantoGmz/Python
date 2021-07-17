import cv2
import numpy as np

#para importar imagenes
img= cv2.imread('test.png')

# cv2.cvtColor(imagen_Que_introduje,cv2.COLOR.... esto es para efectos de colores ya sea rgb o bgr o hsv)
gris= cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
#imshow() es para en el primer parametro poner nombre a la ventana y el segundo la imagen a imprimir
cv2.imshow('test', gris)

#waitkey en 0 es para que espere a que tecla le dare para que se cierre
cv2.waitKey(0)

#esto destruye otras ventanas para evitar errores al cerrar y inicar nuevamente
cv2.destroyAllWindows