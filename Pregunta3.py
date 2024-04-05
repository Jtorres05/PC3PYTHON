# Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
# “CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2) # Valor aproximado de π

# Uso de la clase
radio = float(input("Ingrese el valor del radio: "))
circulo = Circulo(radio)
print("Área del círculo:", circulo.calcular_area())