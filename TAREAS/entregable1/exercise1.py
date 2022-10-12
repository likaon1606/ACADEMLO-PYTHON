import csv
import encodings
import pandas as pd
import glob

todos = []

for f in glob.glob("*.csv"):
    df = pd.read_csv(f)
    todos.append(pd.read_csv(f))

df = pd.concat(todos, ignore_index="True")
print(df)    

list_join = []

with open(df) as csv_file:
  file_to_process = csv.DictReader(csv_file)
for i in file_to_process:
    first_name = i["First Name"].lower()
    last_name = i["Last Name"].lower()
    score = int(i["Score"])
    list_join.append({"name":first_name, "last_name":last_name, "score":score})
    print(list_join)

# with open("quiz_2.csv", encoding="utf-8") as csv_file2:
#   file_to_process2 = csv.DictReader(csv_file2)
#   for i in file_to_process2:
#     first_name = i["First Name"].lower()
#     last_name = i["Last Name"].lower()
#     score = int(i["Score"])
#     list_join.append({"name":first_name, "last_name":last_name, "score":score})

# with open("quiz_3.csv", encoding="utf-8") as csv_file2:
#   file_to_process2 = csv.DictReader(csv_file2)
#   for i in file_to_process2:
#     first_name = i["First Name"].lower()
#     last_name = i["Last Name"].lower()
#     score = int(i["Score"])
#     list_join.append({"name":first_name, "last_name":last_name, "score":score})

# with open("quiz_4.csv", encoding="utf-8") as csv_file2:
#   file_to_process2 = csv.DictReader(csv_file2)
#   for i in file_to_process2:
#     first_name = i["First Name"].lower()
#     last_name = i["Last Name"].lower()
#     score = int(i["Score"])
#     list_join.append({"name":first_name, "last_name":last_name, "score":score})
     




  



  

# Deberas crear una clase para las siguientes funcionalidades: 
# Abrir Archivos Procesar Archivos Encontrar Ganadores (Los dos primeros: 
# Puntos extra si permiten que la cantidad de ganadores sea dinamica) 
# ganador con su puntaje. ( SE CONSIDERA GANADORE A LAS PERSONA QUE TENGAN 
# EL MAYOR PUNTAJE AL SUMAR EL PUNTAJE DE TODOS LOS QUIZES Y PUNTOS EXTRAS ) 
# Encontrar Usuarios que tengan un porcentaje de acierto mayor a 70 % 
# (Puntos extra si el porcentaje es dinamico) por cada quiz Cualquier 
# clase extra que consideres necesaria para resolver el ejercicio. 
# El objetivo final es encontrar las dos personas que hasta el día de hoy van a la delantera


