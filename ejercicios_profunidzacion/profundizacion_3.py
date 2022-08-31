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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

from ctypes.wintypes import PINT


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('ingrese temperatura 1')
temp_1 = int(input())
print('ingrese temperatura N.2')
temp_2 = int(input()) 
print('ingrese temperatura N.3')
temp_3 = int(input())

if temp_1 > temp_2 and temp_1 > temp_3:
    print(temp_1 , ' es la maxima temperatura ')
elif temp_2 > temp_1 and temp_2 > temp_3:
    print( temp_2 , 'es la maxima temperatura')
else:
    print(temp_3 , 'es la temperatura maxima')

if temp_1 < temp_2 and  temp_1 < temp_3:
    print( temp_1, 'es la temperatura minima')
elif temp_2 < temp_1 and temp_2 < temp_3:
    print(temp_2 , 'es la temperatura minima')
else:
     print(temp_3, 'es la temperatura minima')


suma = temp_1 + temp_2 + temp_3
promedio = suma / 3
print( 'el promedio de temperatura es:', promedio) 
