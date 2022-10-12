from ast import Num


class ClassName:
    pass

# Crea - Inicializa - Destruye

# Comportamientos (metodos), Datos (propiedades)
# Roberto

class Person():

    def __init__(self, name, age, telf=None) -> None:
        self.name = name
        self.age = age
        self.telf = telf
        print(self.saluda())

    def saluda(self): 
        return f"Hola {self.name}"
#------------------------------------------------------------   
roberto = Person("Roberto", 85, 8897779)

# Empresa 
# Empleado
# Trabajo


class Empresa:
    country = "Colombia"

    def __init__(self, name:str, addres:str) -> None:
        self.name = name
        self.addres = addres

    def do_contract(self, employe):
        print(f"Se contracto a {employe} en la empresa {self.name} con direccion {self.addres}")

academlo = Empresa("academlo", "calle muy lejos")
academlo.do_contract("Luis")

# Vehiculo
class Vehiculo:
    marca = "Honda"

    def __init__(self, motor:int, potencia:str, color:str) -> None:
        self.motor = motor
        self.potencia = potencia
        self.color = color

    def cliente(self, cliente):
        print(f"El señor {cliente} compro un auto {self.marca} con motor {self.motor} que tiene una potencia de {self.potencia} y es de color {self.color}")

honda = Vehiculo(1.6, "300hp", "blue")
honda.cliente("Ariel")            