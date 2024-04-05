# Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
# para:
# 1. Display- Debe mostrar toda la información del estudiante (nombre y número de registro).
# 2. setAge- Debe asignar la edad al estudiante
# 3. setNota- Debe asignar las notas al estudiante.

class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)

# Creo Objetos a partir de mi clase
alumno1 = Alumno("Jhon", 147852)
alumno1.setAge(25)
alumno1.setNota(18)
alumno1.setNota(20)
alumno1.display()