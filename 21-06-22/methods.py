# CAPITALIZE -> convertir el primer caracter a mayuscula
from itertools import count


title = "esto es una gran clase"
new = title.capitalize()

print(new)

# CASEFOLD -> convierte el texto en minuscula
# Es mas agresivo
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#lower
#hace lo mismo de casefold pero  menos agresivo
txt = "Hello, And Welcome To My World!"
x = txt.lower()
print(x)

# upper convierte a mayusculas toda la frase
txt = "Hello, And Welcome To My World!"
x = txt.upper()
print(x)

# title convierte el primer caracter de cada palabra en mayuscula
new = "En Peru las empanadas son horneadas"
new = new.title()
print(new)

# count contar cuantas veces aparece una palabra, recordando escribirla en mayuscula o minuscula segun corresponda
count = new.count("Son")
print(count)

# find encontrar la posicion de una palabra
txt = "Hello, And Welcome To My World!"
x = txt.find("Welcome")
print(x)

# endwith
txt = "Hello, And Welcome To My World!"
x = txt.endswith("!")
print(x)

# startswith
txt = "Hello, And Welcome To My World!"
x = txt.startswith("H")
print(x)

# center
txt = "banana"
x = txt.center(20, " ")
print(x)

#zfill para decimales a la izquierda
factura = "15"
x = factura.zfill(10)
print(x)

# split para separar palabras en ''
txt = "welcome to the jungle"
x = txt.split()
print(x)

# join para unir palabras puede ser espacio, comas, etc
x = " ".join(x)
print(x)

# x, y, z = "Ariel", 42, "Fuentes" # declarar multipoles variables
# print(x,y,z)



