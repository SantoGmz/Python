import cv2


imagen=cv2.imread('/Users/S A N T O S/Documents/Python/leer-img/logo.png',0)
cv2.imshow('prueba de imagen', imagen)
cv2.imwrite('grises.png', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()