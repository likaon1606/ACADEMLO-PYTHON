frase = "Esta es una gran frase"

name = 0
for i in frase[::2]: # recorrer una frase de 2 en 2 caracteres
    print(i)
    
    a = range(1,11,3)
    print(a)
    for i in a:
        print(i)

for i in range(1,45):
    if i % 10 == 0:
        print(i)

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

num_odd = [x for x in num_list if x%2 != 0]
print(num_odd)

for n1  in num_list:
    for n2 in num_list:
        if n1 + n2 == n:
            print(n1,n2)
            break

nueva_lista = []
for x in num_list:
    if x%2 !=0:
        nueva_lista.append(x)

print(nueva_lista)        