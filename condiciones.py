# https://www.youtube.com/watch?v=iV-4F0jGWak&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=10

print("Programa de evaluacion de notas de alumnos")


nota_Alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5 :
        valoracion="Suspendido"
    return valoracion

print(evaluacion(int(nota_Alumno)))          


f=input()