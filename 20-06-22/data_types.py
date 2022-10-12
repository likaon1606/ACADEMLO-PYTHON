# Data type -> Es un item, o elemento que define el tipo y el rango 
# de valores que puede tomar.

# numbers - strings - booleans

# Variables - Un nombre que tiene un valor asignado

import quopri
from random import random


income = 480
Income = 470
income = 470 # reasignamos el valor de 480 a 470

income2 = 789
_name = 'Nico'
name_ = 'Nico2'

print(income)
print(Income)
print(income2)
print(_name)
print(name_)

EDAD = 78 # las constantes se escriben en mayusculas por convencion, pero pueden ser modificadas a diferencia de JS
print(EDAD)
EDAD = 45
print(EDAD)

print(name_, EDAD) # se pueden imprimir 2 variables de una sola vez

# Numeros - Enteros
numero = 844
numero2 = -844
print(numero)
print(numero2)

print(
    type(numero) # para saber el tipo de dato con type
)

# Numeros - flotantes - float
numero = 77.90
print(numero)
print(type(numero))

# Numeros - complejos - complex
numero = complex(10,20) # 10 + 20j
print(type(numero))

# Booleans
print(True)# en python los boleanos empiezan con mayuscula
print(False)

print(True + 0)
print(False + 0)

name = 'Nico'
print(type(name))

quote = """
This is a great
quote"""
print(type(quote))

random_string = "i am Ariel"
print(len(random_string)) # len cuenta los caracteres

batman = "Bruce Wayne"
first = batman[0] # para buscar el primer elemento de la lista
print(first)

print(batman[len(batman) -1]) #imprime el ultimo caracter del string
print(batman[0:11]) # imprime el rango de 0 a 11

