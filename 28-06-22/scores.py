lista_estudiantes = [
  {
    "name": "Andres",
    "score": "45894"
  },
  {
    "name": "AndreS",
    "score": "45894"
  },
  {
    "name": "Jimena",
    "score": 789995
  },
  {
    "name": "Jimena",
    "score": 789995
  },
    {
    "score": 4899,
    "name": "Angela Burt"
  },
  {
    "score": 6044,
    "name": "Emma Mcclain"
  },
  {
    "score": 6283,
    "name": "Carey Blevins"
  },
  {
    "score": 2093,
    "name": "Guerrero Collier"
  },
  {
    "score": 5434,
    "name": "Dickson Mercado"
  },
  {
    "score": 2549,
    "name": "Knox Robinson"
  },
  {
    "score": 5950,
    "name": "Wilder Conley"
  },
  {
    "score": "6155",
    "name": "Agnes Stanley"
  },
  {
    "score": 1177,
    "name": "Jones Koch"
  },
  {
    "score": 1207,
    "name": "Rosario Mays"
  },
  {
    "score": 2100,
    "name": "Trina Miles"
  },
  {
    "score": 3524,
    "name": "Murphy Hayden"
  },
  {
    "score": 1679,
    "name": "Sharlene Roach"
  },
  {
    "score": 6943,
    "name": "Rutledge Castaneda"
  },
  {
    "score": "1019",
    "name": "Evelyn Serrano"
  }
]

from typing import List

from typing import List

def procces_data(lista: str) -> List: 
  for element in lista:
    element["name"] = element.get("name").lower()
    element["score"] = int(element.get("score"))

  return lista

def obtener_puntajes(lista_a_sumar):

  new_dict = {}

  for student in lista_a_sumar:
    if student["name"] not in new_dict.keys():
      new_dict[student["name"]] = student["score"]
    else:
      new_dict[student["name"]] = new_dict[student["name"]] + student["score"]
  
  return new_dict



