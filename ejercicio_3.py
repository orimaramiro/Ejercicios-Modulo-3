# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 3
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
if numero_1 > 5:
#   --> En caso afirmativo, verifique si el numero_2 es positivo
    if numero_2 > 0:
     #       --> En caso afirmativo imprima en pantalla "Resp=1"
        print("Resp=1")
#       --> En caso negativo imprima en pantalla   "Resp=2"
    else:
        print("Resp=2")
#  --> En caso negativo (numero_1 no es mayor a 5)
else: 
    numero_1 < 5
#      verifique si el numero_2 es mayor a 5
    if numero_2 > 5:
#       --> En caso afirmativo imprima en pantalla "Resp=3"
        print("Resp = 3")
#       --> En caso negativo imprima en pantalla "Resp=4"
    else:
         print("Resp = 4")
# Verifique la calificación de un estudiante según su
# puntaje en un examen, cambie los parametros
puntaje = 93
calificacion = "S/C"
# Si el puntaje es mayor igual a 50 --> imprimir D
if puntaje >= 50:
    calificacion = "D"
# Si el puntaje es mayor igual a 60 --> imprimir F
    if puntaje >= 60:
        calificacion = "F"
# Si el puntaje es mayor igual a 70 --> imprimir C
        if puntaje >= 70:
            calificacion = "C"
# Si el puntaje es mayor igual a 80 --> imprimir B
            if puntaje >= 80:
                calificacion = "B"
# Si el puntaje es menor a  90      --> imprimir A
                if puntaje >= 90:
                    calificacion = "A"
print("la calificacion del alumno es", calificacion)
# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados
