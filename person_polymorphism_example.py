class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        print(f"{self.nombre} va caminando")


class Maratonista(Persona):
    def movimiento(self):
        print(f"{self.nombre} va trotando")


class Ciclista(Persona):
    def movimiento(self):
        print(f"{self.nombre} va rodando")


persona1 = Persona("Diego")
persona1.movimiento()
ciclista1 = Ciclista("Raúl")
ciclista1.movimiento()
maratonista1 = Maratonista("Ignacio")
maratonista1.movimiento()
