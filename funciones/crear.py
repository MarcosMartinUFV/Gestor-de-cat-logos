from tablas.producto import Producto  # Importamos la clase Producto del modelo
from basedatos import Session  # Importamos la sesión de la base de datos


def crear_producto():
    session = Session()  # Iniciamos una sesión para conectarnos a la BBDD
    print("Introduce los datos del nuevo producto")

    nombre = input("Nombre del producto: ")  # Pedimos nombre
    descripcion = input("Descripción: ")  # Pedimos descripción
    precio = float(input("Precio (€): "))  # Pedimos precio
    stock = int(input("Stock: "))  # Pedimos stock (FALTABA)

    nuevo_producto = Producto(  # Creamos un nuevo producto con los datos
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        stock=stock
    )

    session.add(nuevo_producto)  # Añadimos el producto a la sesión
    session.commit()  # Guardamos los cambios en la base de datos
    print("Producto añadido correctamente.")
    session.close()  # Cerramos la sesión


"""
Esta función crear_producto() permite al usuario añadir un nuevo producto al catálogo directamente desde la consola.
Solicita al usuario que introduzca el nombre, descripción y precio del producto, crea una instancia de la clase Producto, y la guarda en la base de datos usando SQLAlchemy.
Usa un bloque with para asegurar que la sesión se cierre correctamente, y confirma con un mensaje que la operación se ha realizado con éxito.
Es el primer paso para construir un CRUD completo.
"""
