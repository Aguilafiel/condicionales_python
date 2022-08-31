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

from cgi import print_environ


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print( 'ingrese un numero')
num_1 = int(input()) 
print('ingrese segundo numero')
num_2 = int( input()) 

resta = num_1 - num_2
if resta > 0:
    print( resta , 'es positivo')
elif resta < 0:
    print(resta, ' es negativo')
else :
    print( 'el resultado es igual a 0')
