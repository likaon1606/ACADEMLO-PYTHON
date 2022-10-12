# NUMEROS COMPLEJOS

from ast import Import


z = complex(1, -7) # con la funcion complex asigna el numero real e imaginario 7j
print(type(z))
print(z.real) #muestra el numero real 1.0
print(z.imag) #muestra el numero imaginario -7.0

z1 = 2 - 6j
z2 = 5 + 4j
print(z1 + z2) # suma la parte real con real y la imaginaria con imaginaria, asi con todas las operaciones

z = -2 + 1j # siempre debe tener un numero antes de la j, aunque este sea 1
print(z.conjugate()) # devuelve el conjugado -2-1j


z = -2j
print(abs(z)) # devulve el valor absoluto

#-----------------CALCULAR EL ARGUMENTO---------------------------

import cmath
print(cmath.phase(z)) # es la fase del argumento del numero complejo -2j

# pasar la forma binomica a forma polar
print(cmath.polar(z))

# recuperar la forma binomica de la polar
print(cmath.rect(abs(z), cmath.phase(z)))

# METODO .format cambia varios valores a strings
print("My name is {name} and have {age} years".format(name = "Ariel", age = 42))

# obtener los 10 ultimos elementos
s = "soy fan de los videojuegos"
print(s[-10:])

# obtener desde el final hasta las diez ultimas posiciones
print(s[:-10])