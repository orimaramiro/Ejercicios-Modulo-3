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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print ("Ingrese el primer número:") 
numero_1= int (input())
print ("Ingrese el segundo número:") 
numero_2= int (input())
print("Diferencia entre primer y segundo número")
diferencia= numero_1 - numero_2
if diferencia > 0:
    print("El resultado es positivo", diferencia)
elif diferencia < 0:
     print("El resultado es negativo", diferencia)
else:
    print ("El resultado es = a 0", diferencia )

print("Diferencia entre segundo y primer número")
diferencia= numero_2 - numero_1
if diferencia > 0:
    print("El resultado es positivo", diferencia)
elif diferencia < 0:
     print("El resultado es negativo", diferencia)
else:
    print ("El resultado es = a 0", diferencia )