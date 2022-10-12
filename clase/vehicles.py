from base import Vehicle

class Car(Vehicle):
    def turn_on(self):
        return "Se encendio el carro"

    def go_to_town(self):
        return "Salio rumbo al poblado"


class Truck(Vehicle):
    def turn_on(self):
        return "Se encendio el camion"

    def go_to_town(self):
        return "Salio rumbo al poblado"