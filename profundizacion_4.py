# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador "<")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador "<")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print("Ordenamiento de palabaras alfavetico o por longitud de carcatees")
print("Ingrese la primer palabra")
texto_1 = str(input())
print("Ingrese la segunda palabra")
texto_2 = str(input())
print("Ingrese la tercer palabra")
texto_3 = str(input())
print("Ingrese 1 si desea obtener el órden por órden alfabético o 2 so desea el órden por longiyud de carcateres" )
opciones = int(input())
if opciones != 2 and opciones != 1:
    print("El valor ingresado no se encuentra dentro de las opciones" )
    print("Ingrese 1 si desea obtener el órden por órden alfabético o 2 so desea el órden por longiyud de carcateres" )
    opciones = int(input())
if opciones == 1:
    #Órden alfabético
    if texto_1 < texto_2 and texto_1 < texto_3:
        if texto_2 < texto_3:
            print("Palabras por orden alfabético", texto_1, texto_2, texto_3)
        elif texto_3 < texto_2:
            print("Palabras por orden alfabético", texto_1, texto_3, texto_2)
        if texto_2 == texto_3:
            print("Palabras por orden alfabético", texto_1, "está primero", texto_2,"y", texto_3, "Son iguales")

    if texto_2 < texto_1 and texto_2 < texto_3:
        if texto_1 < texto_3:
            print("Palabras por orden alfabético", texto_2, texto_1, texto_3)
        elif texto_3 < texto_1:
            print("Palabras por orden alfabético", texto_2, texto_3, texto_1)
        if texto_1 == texto_3:
            print("Palabras por orden alfabético", texto_2, "está primero", texto_1,"y", texto_3, "Son iguales")

    if texto_3 < texto_1 and texto_3 < texto_2:
        if texto_2 < texto_1:
            print("Palabras por orden alfabético", texto_3, texto_2, texto_1)
        elif texto_1 < texto_2:
            print("Palabras por orden alfabético", texto_3, texto_1, texto_2)        
        if texto_1 == texto_2:
            print("Palabras por orden alfabético", texto_3, "está primero", texto_1,"y", texto_2, "Son iguales")

if opciones == 2:
    long_texto_1 = len(texto_1)
    long_texto_2 = len(texto_2)
    long_texto_3 = len(texto_3)
    
    print("longitudes", long_texto_1, long_texto_2, long_texto_3)
    
    
    if long_texto_1 == long_texto_2 and long_texto_1 == long_texto_3:
        print("Las tres palabras poseen la misma cantidad de carateres", long_texto_1)
   
    if long_texto_1 >= long_texto_2 and long_texto_1 >= long_texto_3:
        if long_texto_2 > long_texto_3:
            print("Palabras ordenadas por longitud de caracteres", long_texto_1, long_texto_2, long_texto_3)
        elif long_texto_3 > long_texto_2:
            print("Palabras ordenadas por longitud de caracteres", long_texto_1, long_texto_3, long_texto_2)
        if long_texto_2 == long_texto_3:
            print("Palabras ordenadas por longitud de caracteres", long_texto_1, "está primero", long_texto_2,"y", long_texto_3, "Son iguales")

    if long_texto_2 >= long_texto_1 and long_texto_2 >= long_texto_3:
        if long_texto_1 > long_texto_3:
            print("Palabras ordenadas por longitud de caracteres", long_texto_2, long_texto_1, long_texto_3)
        elif long_texto_3 > long_texto_1:
            print("Palabras ordenadas por longitud de caracteres", long_texto_2, long_texto_3, long_texto_1)
        if long_texto_1 == long_texto_3:
            print("Palabras ordenadas por longitud de caracteres", long_texto_2, "está primero", long_texto_1,"y", long_texto_3, "Son iguales")

    if long_texto_3 >= long_texto_1 and long_texto_3 >= long_texto_2:
        if long_texto_2 > long_texto_1:
            print("Palabras ordenadas por longitud de caracteres", long_texto_3, long_texto_2, long_texto_1)
        elif long_texto_1 > long_texto_2:
            print("Palabras ordenadas por longitud de caracteres", long_texto_3, long_texto_1, long_texto_2)        
        if long_texto_1 == long_texto_2:
            print("Palabras ordenadas por longitud de caracteres", long_texto_3, "está primero", long_texto_1,"y", long_texto_2, "Son iguales")