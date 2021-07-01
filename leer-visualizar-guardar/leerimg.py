import cv2

#para agregar en una variable la img que voy a leer
imagen=cv2.imread('logo.png')

#el logo de la imagen y la ubicacion de la img
cv2.imshow('Prueba de imagen', imagen)
#donde waitKey es el tiempo de espera, si lo dejo en 0 durara hasta que lo cierre, si lo pongo en 1000 durara 1 segundo
cv2.waitKey(0)

#esto es para cerrar todas las ventanas de windows
cv2.destroyAllWindows()