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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print("Ingrese el primer número")
numero_1 = int(input())
print("Ingrese el segundo número")
numero_2 = int(input())
print("Ingrese el tercer número")
numero_3 = int(input())
todos_impares = 0
todos_pares = 0
resto_1 = numero_1 % 2 
resto_2 = numero_2 % 2
resto_3 = numero_3 % 2

if resto_1 == 0 and resto_2 == 0 and resto_3 == 0:
    print("Los tres números son pares", numero_1, numero_2, numero_3)
    todos_pares = 1
if resto_1 != 0 and resto_2 != 0 and resto_3 != 0:
    print("Los tres números son impares", numero_1, numero_2, numero_3)
    todos_impares = 1
if todos_pares == 0 and todos_impares == 0:
    if resto_1 == 0:
        print("el primer número es par", numero_1)
    else:  print("el primer número es impar", numero_1)
    if resto_2 == 0:
        print("el segundo número es par", numero_2)
    else:  print("el segundo número es impar", numero_2)
    if resto_3 == 0:
        print("el tercer número es par", numero_2)
    else:  print("el tercer número es impar", numero_2)
    
