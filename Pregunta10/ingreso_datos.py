def area_circulo(radio):

    try:
        radio = float(input("Ingrese el valor del radio del círculo: "))
        if radio < 0:
            raise ValueError("El radio debe ser un número positivo.")
        
        area = 3.14 * radio ** 2
        return area
    except ValueError:
        print("Error: El valor ingresado no es válido.")
        return None
    
