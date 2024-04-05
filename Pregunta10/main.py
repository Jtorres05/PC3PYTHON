# 1. Librerias
import ingreso_datos
import recta_1
import avanzadas

# 2. Constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? Escribe una opción
    1) Calcular el área de un circulo
    2) Calcular el área de un rectangulo
    3) Calcular el área de un cuadrado
    4) Salir
"""
# 3. Funciones y/o métodos

def opcion1():
    area = ingreso_datos.area_circulo('radio') 
    print(f'El área del circulo es {area}')

def opcion2():
    a = recta_1.area_rectangulo('b:float','h:float')
    print(f'El área del rectangulo es {a}')

def opcion3():
    a1 = avanzadas.area_cuadrado('lado')
    print(f'El área del rectangulo es {a1}')

def main():
    print("MENSAJE_BIENVENIDA")
    while True:
        opcion = input(OPCIONES_MENU) # me devuelve un string ''
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")

# 4. Función nain
if __name__=='__main__':
    main()