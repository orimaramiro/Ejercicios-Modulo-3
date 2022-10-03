# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 < texto_2:
    print(texto_1, "se encuentra primero en ordel alfabético que", texto_2)
elif texto_1 > texto_2:
    print(texto_2, "se encuentra primero en ordel alfabético que", texto_1)
else:
     print(texto_2, "Las palabras son iguales", texto_1)

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
numero_1 = int(texto_1)
numero_2 = int(texto_2)
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
if texto_1 < texto_2:
    print(texto_1, "es menor que", texto_2)
elif texto_1 > texto_2:
    print(texto_2, "es menor que", texto_1)
else:
     print(texto_2, "Las numeros son iguales", texto_1)


# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
"""Porque Phyton interpreta con comillas que son carcateres, pero a su vez dentro de esos caracteres están incorporados los numeros
y su valor numerico es igual a su valor tipo string""" 
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
