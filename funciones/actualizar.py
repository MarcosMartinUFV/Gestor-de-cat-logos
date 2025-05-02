# actualizar.py – Permite modificar productos existentes en la base de datos

from sqlalchemy.orm import Session  # Importa el objeto Session para manejar sesiones de base de datos
from basedatos import engine  # Importa el motor de la base de datos desde basedatos.py
from tablas.producto import Producto  # Importa la clase Producto definida en el modelo ORM

# Inicia una sesión para interactuar con la base de datos
session = Session(bind=engine)

# Solicita al usuario el ID del producto que desea modificar
id_producto = int(input("Introduce el ID del producto a modificar: "))

# Busca el producto por ID
producto = session.query(Producto).filter_by(id=id_producto).first()

# Si se encuentra el producto, permite modificarlo
if producto:
    print(f"Producto encontrado: {producto.nombre}")

    # Solicita nuevos valores (si se deja vacío, mantiene el actual)
    nuevo_nombre = input(f"Nuevo nombre (actual: {producto.nombre}): ") or producto.nombre
    nueva_descripcion = input(f"Nueva descripción (actual: {producto.descripcion}): ") or producto.descripcion
    nuevo_precio = input(f"Nuevo precio (actual: {producto.precio}): ")
    nuevo_stock = input(f"Nuevo stock (actual: {producto.stock}): ")

    # Actualiza solo si se ha introducido un nuevo valor, o mantiene el actual
    producto.nombre = nuevo_nombre
    producto.descripcion = nueva_descripcion
    if nuevo_precio != "":
        producto.precio = int(nuevo_precio)
    if nuevo_stock != "":
        producto.stock = int(nuevo_stock)

    # Guarda los cambios en la base de datos
    session.commit()
    print("Producto actualizado correctamente.")
else:
    print("❌ Producto no encontrado.")

# Cierra la sesión
session.close()


def actualizar_producto():
    return None