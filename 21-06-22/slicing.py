my_string="This is my string!"
print(my_string[0:4])#toma hasta la posicion 3, simepre llega a una posicion antes
print(my_string[1:7])
print(my_string[8:len(my_string)])#imprime desde la posicion 8 hasta el final por el "len"
a = "hola"
print(len(a))

# obtener la ultima posicion de un iterable (string)
print(my_string[-1])
print(my_string[len(my_string) -1])

print(my_string[:4]) # obtiene la primer posicion de los 3 caracteres
print(my_string[2:])# obtine la posicion 2 hasta el final

print(my_string[::2]) # salta de 2 en 2 posiciones, puede saltar lo que le digamos por ejemplo de 5 en 5 etc

# CONCATENACION

name = "Carla"
last_name = "Jimenez"

full_name = name + " " + last_name
print(full_name)
full_name = f"My full name is {name} {last_name}"
print(full_name)














