# 5 operadores
#ARITMETICOS
# (), **, %, *, /, //, +, -
adicion = 13 + 87
print(adicion)

float = 14.8 + 9.1
print(float)

print(10-5) # tambien se puede

num = 20
flt = 10.5
print(int(num - flt))

import math
from unittest import result
print(math.floor(4.5))

num = 10/4
num = 10//4 # division a entero
print(num)

num = 3**2 # potencia elevado a 2
print(num)

num = 10%2 # residuo
print(num)

print(10-3*2)
print(3*20 /5)
print(3/20*5)

print((10-3)*2)

#COMPARACION siempre retornan un booleano
# el triple === no existe en python
a = 8>2
b = 5<3
print(a,b)

c = 5 <= 5
d = 7 >= 9
print(c,d)

f = 8 == 8
print(f)

h = 2 != 3 # diferente
print(h)

print("3"==3)

num2 = 10
num3 = 10

list1 = [6,7,8]
list2 = [6,7,8]
print(list1 is list2) # is es un comparador
print(num2 is not num3)
print(id(num2)) # para saber la direcciond e memoria que se le asigna
print(id(num3))


#ASIGNACION
nombre = "ariel"
year = 2022
year += 1
print(year)
year -=1
print(year)
year *= 2
print(year)
year /= 2
print(year)
year //= 1
print(year)

num = 2
num **= 3 # potencia
print(num)


#LOGICOS
# and or not
my_bool = True or False
print(my_bool)
my_bool = True and False
print(my_bool)
my_bool = False
print(not my_bool) # esta negando el false
print(15*True)

house = "dasdas"
house_copy = "dsadasdasda"
print(house < house_copy) # true, house tiene menos caracteres

x = 20
y = 5
result = (x + True) / (4 - y * False)
print(result)


name = input("ingresa tu nombre")

print(f"Hola {name}")
edad = int(input("Ingresa tu edad"))
edad = edad + 1
print(edad)
#BITWISE