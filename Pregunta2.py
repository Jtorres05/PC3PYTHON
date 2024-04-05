# Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
# la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
# calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
# cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
# formato. (Los métodos de cadena le serán de utilidad)

def obtener_calificaciones():
    calificaciones_str = input("Ingrese calificaciones separadas por comas: ")
    calificaciones = calificaciones_str.split(',')
    calificaciones_enteros = []
    for calificacion in calificaciones:
        try:
            calificacion_entero = int(calificacion.strip())
            calificaciones_enteros.append(calificacion_entero)
        except ValueError:
            print("Error: Las calificaciones tienen que ser números enteros.")
            return None
    return calificaciones_enteros

calificaciones = obtener_calificaciones()
if calificaciones:
    print("Calificaciones ingresadas:", calificaciones)