from sqlalchemy.orm import Session                   # Importamos la clase Session para manejar sesiones de base de datos
from tablas.producto import Producto                 # Importamos el modelo Producto
from basedatos import engine                         # Importamos el motor de conexión a la base de datos

def mostrar_productos():
    """Función para listar todos los productos registrados"""

    with Session(engine) as session:                 # Iniciamos una sesión con la base de datos
        productos = session.query(Producto).all()    # Consultamos todos los productos existentes

        if productos:                                # Si hay productos en la lista
            print("\nLista de productos:")
            for p in productos:                      # Recorremos cada producto
                print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: {p.precio} € | Descripción: {p.descripcion}")
        else:
            print("\n⚠No hay productos registrados.")
