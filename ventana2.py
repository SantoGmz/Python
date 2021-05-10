#https://www.youtube.com/watch?v=jqRHhWjKDD8
import tkinter

ventana2 = tkinter.Tk()

ventana2.geometry("400x300")
cajaTexto = tkinter.Entry(ventana2)
cajaTexto.pack()

etiqueta = tkinter.Label(ventana2)
etiqueta.pack()

def textoDeLaCaja():
    text20 = cajaTexto.get()
    etiqueta["text"] = text20 

boton1 = tkinter.Button(ventana2, text = "click", command = textoDeLaCaja)
boton1.pack()

ventana2.mainloop()