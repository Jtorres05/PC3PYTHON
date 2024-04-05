# Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
# Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
# método para agregar productos y otra para mostrar toda la lista de productos.
# Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
# agregar más atributos a los productos para que se puedan hacer otras funcionalidades

class Producto:
    def __init__(self, nombre, marca, año):
        self.nombre = nombre
        self.marca = marca
        self.año = año

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.marca, self.año)


class Catalogo:
    def __init__(self):
        self.productos = [] # Esta lista contendrá objetos de la clase Producto

    def agregar_producto(self, p):
        self.productos.append(p)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


# Crear un catálogo
catalogo = Catalogo()

# Agregar productos al catálogo
p1 = Producto("Filtro de aceite", "Bosch", 2021)
p2 = Producto("Pastillas de freno", "Ferodo", 2020)
p3 = Producto("Bujías", "NGK", 2021)

catalogo.agregar_producto(p1)
catalogo.agregar_producto(p2)
catalogo.agregar_producto(p3)

# Mostrar la lista de productos
catalogo.mostrar_productos()

# Filtrar productos por año
catalogo.filtrar_por_año(2021)