from sqlalchemy.orm import Session  # Importamos la clase Session para trabajar con la BBDD
from tablas.producto import Producto  # Importamos el modelo Producto
from basedatos import engine  # Importamos el engine para conectar a la base de datos

def eliminar_producto():
    """Elimina un producto del catálogo usando su ID"""
    with Session(engine) as session:  # Creamos una sesión de conexión a la base de datos
        try:
            id_producto = int(input("Introduce el ID del producto que quieres eliminar: "))  # Pedimos el ID al usuario
        except ValueError:
            print("⚠  El ID debe ser un número entero.")
            return

        producto = session.get(Producto, id_producto)  # Buscamos el producto con ese ID

        if producto:  # Si se encuentra el producto
            session.delete(producto)  # Lo marcamos para eliminar
            session.commit()  # Confirmamos la eliminación
            print(f"✅ Producto con ID {id_producto} eliminado correctamente.")
        else:
            print("❌ No se encontró ningún producto con ese ID.")




"""
Este módulo implementa la función eliminar_producto(), que elimina un producto de la base de datos a partir del ID proporcionado por el usuario.
Usa SQLAlchemy para conectar con la base de datos y operar sobre el modelo Producto.
Gestiona errores si el ID no existe o no es válido, y confirma la operación al usuario.
"""