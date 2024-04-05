def area_rectangulo (b:float, h:float)-> float:
    '''Calcula el area del rectangulo a partir de la base y altura'''
    try:
        b = int(input('Ingrese la base: '))
        h = int(input('Ingrese la altura: '))
        return b * h
    except ValueError as e:
        print("Error:", e)
        return None

    