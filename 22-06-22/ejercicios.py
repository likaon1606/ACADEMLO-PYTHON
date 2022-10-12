price = int(input("ingresa el precio"))

if price >= 300:
    price *= 0.7 # descuento del 30% y asi sucesivamente
elif price >= 200:
    price *= 0.8
elif price >= 100:
    price *= 0.9
elif price < 100:
    price *= 0.95

print(f"El precio final es: {price}")
