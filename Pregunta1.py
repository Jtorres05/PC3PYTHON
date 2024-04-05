# Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno
# de X e Y es un número entero, y luego muestra, como un porcentaje redondeado al número
# entero más cercano, donde se indicará la cantidad de combustible en el tanque. 
# Se debe tener en cuenta los siguientes casos:
# Colocar E en caso X/Y sea menor a 1% del total Colocar F en caso X/Y sea mayor a 99%.
# En otro caso, devolver el valor en porcentaje % 
# También debe tomar en cuenta los siguientes casos:
# X y Y debenser números enteros
# X debe ser menor o igual a Y, y Y!= 0
# De no cumplirse estos casos, se debe volver a preguntar al usuario. 
# Asegúrese de detectar cualquier excepción como ValueError o ZeroDivisionError.

def obtener_porcentaje():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            partes = fraccion.split('/')
            numerador = int(partes[0])
            denominador = int(partes[1])

            if numerador < 0 or denominador <= 0:
                print("Error: Los números deben ser enteros positivos y Y diferente de 0")
                continue
            if numerador > denominador:
                print("Error: El numerador debe ser menor o igual al denominador")
                continue

            porcentaje = (numerador / denominador) * 100

            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{int(round(porcentaje))}%")
            break

        except ValueError:
            print("Error: Ingrese números enteros válidos para la fracción")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0")

if __name__ == "__main__":
    obtener_porcentaje()