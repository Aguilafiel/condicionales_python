# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

from ast import keyword
from itertools import count
import numbers


texto_1 = '5'
texto_2 = '7'

if texto_1 > texto_2:
    print('la palabra 1 es mas larga que la palabra 2')
else:
    print('la palabra 2 es mayor que la palabra 1')
    # 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

num_1 = int(texto_1)
num_2 = int(texto_2)
if num_1 > num_2:
    print('el numero 1 es mayor que el numero 2')
else:
    print('el numero 2 es mayor que el numero 1')

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?

# respuesta : esto es por el valor de cada caracter en la tabla ASCII 

# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
