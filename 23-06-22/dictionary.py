phone_bok = {
    "name": "Batman",
    "city": "Ghotham",
    "cel": 545465,
    "enemy": "Himself",
    "meta": {
        "record": 1
    }
}

name = phone_bok["name"]
cel = phone_bok["cel"]
print(name, cel)
print(phone_bok["meta"]["record"]) # para acceder al nombre de una propiedad en el objeto

empty_dict = dict()
empty_dict_2 = {}


# empty_dict.update(
#     {"color":"red"} # "update" actualiza la información de un dictionary en pyton, insertando el nuevo elemento pero no toma en cuenta el vlaor que esta dentro 
# )

# empty_dict_2.update(
#     {"color":"blue"}
# )
# empty_dict_2.update(
#     {"size":"m"}
# )

# print(empty_dict)
# print(empty_dict_2)


empty_dict["adress"] = "Muy lejos" # asigna un valor a la propiedad adress
print(empty_dict)

empty_dict["adress"] = "cerquita"
print(empty_dict)

del empty_dict["adress"] # "del" borra la propiedad del objeto "adress"
print(empty_dict)

z = {'color': 'red', 'adress': 'Muy lejos', "verde": (8,)}
print(list(z.keys())) # imprime las propiedades del objeto
print(list(z.values())) # imprime los valores de las propiedades
print(list(z.items())) # imprime las propiedades con sus elementos 

a = z.get("color") # accede a la propiedad color
b = z["color"] # accede a la propiedad color, pero es más facil que con "get"
print(a)
print(b)

a = z.get("pepito", "NAN") # el segundo valor se muestra al no encontrar "pepito" pero en lugar de "none" muestra "NAN"
print(a)