# Ejercicio 1
# Crea un string hecho del primer caracter, del 
# caracter del medio y el caracter final

#str1 = "James" -> Jms

from hashlib import sha3_384


str1 = "James"

str2 = str1[0]
str3 = str1[2]
str4 = str1[-1]

res = str2 + str3 + str4
print(res)

#Ejercicio 02
#Crea un caracter hecho de los tres 
# caracteres del medio

#str1 = "JhonDipPeta" -> Dip

str1 = "JhonDipPeta"
print(str1[4:7])


# Ejercicio 03
# Dados dos string, s1 y s2. Escribe un 
# programa para crear un nuevo string s3 
# agregando s2 en el medio de s1
s1 = "Ault"
s2 = "Kelly"
#-> AuKellylt
x = s1[0:2]
y = s1[2:4]
s3 = x + s2 + y
print(s3)

#Ejercicio 4
#Crea un nuevo string hecho del primer, 
# el del medio y el final caracter de cada 
# string existente.

s1 = "America"

s2 = "Japan"

x = s1[0], s2[0]
y = s1[3], s2[2]
z = s1[-1], s2[-1]

res = x + y + z
s3 = "".join(res)
print(s3)

#Ejercicio 5
#Despues de haber visto todos los métodos que tenemos disponible para los strings es 
#momento de poner todo ese conocimiento en practica

#Dado el siguiente texto
x = "IT was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and charcoal ruins of history. - FAHRENHEIT 451"

#Aplicaremos los metodos que acabamos de ver para obtener el siguiente resultado
#It was a special pleasure to see things eaten, to see things blackened and changed. with the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and charcoal ruins of history. - Fahrenheit 451

x1 = x[0:385].capitalize()
x2 = x[385:-1].capitalize()
res = x1 + x2
print(res)