# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 < texto_2:
    print(texto_1, "se encuentra primero en ordel alfabético que", texto_2)
elif texto_1 > texto_2:
    print(texto_2, "se encuentra primero en ordel alfabético que", texto_1)
else:
     print(texto_2, "Las palabras son iguales", texto_1)
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
cuantas_texto_1 = len(texto_1)
cuantas_texto_2 = len(texto_2)
if cuantas_texto_1 < cuantas_texto_2:
    print(texto_1, "tiene menos caracteres que", texto_2)
elif cuantas_texto_1 > cuantas_texto_2:
    print(texto_2, "tiene menos caracteres que", texto_1)
else:
    print(texto_1, "posee la misma cantidad de carcateres que", texto_2)

# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
#primera_letra_1= texto_1[0]:
#primera_letra_2= texto_1[0]:
if texto_1[0] < texto_2[0]:
    print(texto_1[0], "está alfabeticamente antes que", texto_2[0] )
elif texto_1[0] > texto_2[0]:
    print(texto_2[0], "está alfabeticamente antes que", texto_1[0] )
else:
    print("Las primeras letras son iguales")
# Copia de la variable texto_1
copia_texto_1 = texto_1
# Verifique que copia_texto_1 es igual a texto_1
if copia_texto_1 == texto_1:
# Imprima en pantalla según corresponda
    print(copia_texto_1, "es igual a", texto_1)
# Verifique que copia_texto_1 es distinta a texto_2
if copia_texto_1 != texto_2:    
# Imprima en pantalla según corresponda
    print(copia_texto_1, "es distinto a", texto_2)
