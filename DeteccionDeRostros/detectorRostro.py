import cv2 
import numpy as np

faceClassif = cv2.CascadeClassifier('/Users/S A N T O S/Documents/Python/DeteccionDeRostros/haarcascade_frontalface_alt.xml')

image =cv2.imread('/Users/S A N T O S/Documents/Python/DeteccionDeRostros/gente.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(image,
scaleFactor=1.1,
minNeighbors=5,
minSize=(30,30),
maxSize=(200,200))

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()     