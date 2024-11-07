class Person:
    def __init__(self, name):
        self.name = name

    def movement(self):
        print(f"{self.name} va caminando")


class Marathoner(Person):
    def movement(self):
        print(f"{self.name} va trotando")


class Cyclist(Person):
    def movement(self):
        print(f"{self.name} va rodando")


person1 = Person("Diego")
person1.movement()
cyclist1 = Cyclist("Raúl")
cyclist1.movement()
marathoner1 = Marathoner("Ignacio")
marathoner1.movement()
