# Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
# ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
# atributos de la clase.

class Rectangulo:
    def __init__(self):
        self.largo = float(input("Ingrese el valor del largo: "))
        self.ancho = float(input("Ingrese el valor del ancho: "))

    def calcular_area(self):
        return self.largo * self.ancho

# Uso de la clase
rectangulo = Rectangulo()
print("Área del rectángulo:", rectangulo.calcular_area())