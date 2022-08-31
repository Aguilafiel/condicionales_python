# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica




# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

from unicodedata import numeric


# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos


numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))


# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 < 0:
    print(numero_1 , 'es negativo ')
elif numero_1 > 0:
    print(numero_1 , 'es positivo')
else: 
    print('primer numero es igual a 0')

if numero_2 < 0:
    print(numero_2 , 'es negativo ')
elif numero_2 > 0:
    print(numero_2 , 'es positivo')
else: 
    print('primer numero es igual a 0')

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición 
if numero_1 > 0 and numero_1 < 100:
    print(numero_1 ,'Se encuentra en el rango entre 0 y 100' )
else:
    print(numero_1 , 'No se encuentra dentro del rango entre 0 y 100')

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print(numero_1 , 'es mayor que' , numero_2)
else:
    print(numero_2 , 'es mayor que' , numero_1)
