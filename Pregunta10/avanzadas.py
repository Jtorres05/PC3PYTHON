def area_cuadrado(lado):

    try:
        lado = float(input("Ingrese el valor del lado del cuadrado: "))
        if lado < 0:
            raise ValueError("El lado debe ser un número positivo.")
        
        area = lado ** 2
        return area
    except ValueError:
        print("Error: El valor ingresado no es válido.")
        return None