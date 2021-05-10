import tkinter

#agrega tkinter.Tk() a una variable
ventana = tkinter.Tk()
#la propiedad title del objeto tkinter o en este caso variable, le cambia el titulo de la ventana, osea la cabecera que trae por defecto
ventana.title("Testing")

#con "geometry" puedo dimencionar mi ventana, el tamaño de ella
ventana.geometry("300x300")
"""
etiqueta = tkinter.Label(ventana, text ="Hola Santos", bg = "green")
etiqueta.pack(fill = tkinter.BOTH, expand = True)
"""

def mensaje(nombre):
    print("hola " + nombre)
#tkinter.button, para crear un boton
"""
tkinter.button, para crear un boton
dentro de los parentesis van los parametros, por ejemplo, "ventana" para decir en que lugar hira lo que agrege en este caso el boton.
text, esta propiedad es para decir el texto que lleva dentro,
propiedad padx y pady, son para dimencionar el objeto boton, con esto dimenciono a mi gusto el tamaño que quiera,
command, es para decir que hara si se llega a clickear.
si quiero agregar una funcion con parametros tengo que agregar LAMBDA: porque sin la palabra reservada la funcion se activara automaticamente
sin necesidad de llamarla.
"""
#boton =tkinter.Button(ventana, text = "preciona", padx = 20,pady = 7, command = lambda: mensaje("Santos"))




#la palabra pack() es como para mostrar cualquier cosa que halla hecho, ya sea un boton o un label

#boton.pack()
 
ventana.mainloop()