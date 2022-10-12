# jon_snow = [
#     "Jon snow",
#     "Winterfell",
#     30
# ]
# print(jon_snow)
# print(type(jon_snow))

# print(jon_snow[-1])
 
# jon_snow[2] += 3
# print(jon_snow)

world_cup_winners = [
    [2006, "Italy"], 
    [20210,"Spain"],
    [2014, "Germany"],
    [2018, "France"]
]
# print(world_cup_winners)
print(world_cup_winners[0][-1]) # muestra el nombre y no el año

# part_a = [1,2,3,4,5]
# part_b = [6,7,8,9,10]

# merged_list = part_a + part_b
# print(merged_list)

# part_a = [1,2,3,4,5]
# part_b = [6,7,8,9,10]

# print(part_a)
# part_a.extend(part_b)
# print(part_a)

# num_list = []
# num_list.append(1)
# num_list.append(2)
# num_list.append(3)
# num_list.append([4,5,8])
# print(num_list)

# num_list = [1, 2, 3, 5, 6]
# num_list.insert(3,4) # el 3 es la posicion a insertar y el segundo es el caracter a insertar
# print(num_list)

# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# last_house =  houses.pop(2) # estrae el elemento en la posicion 2 y lo quita del array
# print(last_house)
# print(houses)
# name = "Hufflepuff"
# houses.remove( name)
# print(name) # remueve un elemento especifipo por su nombre
# print(houses)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(num_list[2:5]) # extrae los elementos de la poisicion 2 a la 5


# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print(cities.index("London")) # arroja el indice del elemento a buscar
# print("Paris" in cities) # "in" muestra si el elemento "Paris se encuentra en cities"
# print("Bucaramanga" in cities)

# num_list = [20, 40, 10, 50.4, 30, 100, 5,7,40]
# num_list.sort(reverse=True) # ordena la lista en reversa con "reverse" y con sort lo ordena ascendente
# print(num_list)

# num_list = list(set(num_list)) # "set" no permite valores repetidos
# print(num_list)

# z = ["a", "l", "b", "q", "p"]
# z.sort(reverse=True)
# print(z)

# lista = []
# for i in [4,2,8,10]:
#     lista.append(2*i) # se recorre el array y se multiplica i por 2 y se guarda el resultado en un array vacio
# print(lista)

# lista = ["Hola", "Como", "Estas"]
# txt = " ".join(lista) # "join" une los elementos separados, en las "" se especifica como unirlos, espacio u cualquier caracter
# print(txt)

# lista = [0,1,2,3]
# lista[1] = "Hola" # otra forma de insertar un valor es con [] y el indice de la posición donde se insertará
# print(lista)

# a  = "Hola Como Estas"
# z = a.split("a") # elimina un caracter en las "" puede ser cualquier caracter presente en la lista
# print(z)

car = ("Ford", "Raptor", 2019, "Red", (8,8)) # muestra elemento por elemento hasta recorrer car
for i in car:
    print(i)

print("Ford" in car)

a = (8,)
print(type(a)) # muestra el tipo de elemento, "string, int, etc."