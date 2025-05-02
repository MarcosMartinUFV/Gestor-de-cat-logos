from sqlalchemy.orm import Session                     # Importamos la clase Session para manejar sesiones con la base de datos
from tablas.producto import Producto                   # Importamos el modelo Producto definido en tablas/producto.py
from basedatos import engine                           # Importamos el engine para vincular la base de datos

def crear_producto():
    """Función para añadir un nuevo producto al catálogo"""

    # Crear una nueva sesión de base de datos
    with Session(engine) as session:                   # Usamos un contexto para que la sesión se cierre sola al terminar
        print("Introduce los datos del nuevo producto")

        nombre = input("Nombre del producto: ")        # Pedimos al usuario el nombre del producto
        descripcion = input("Descripción: ")           # Pedimos una descripción
        precio = float(input("Precio (€): "))          # Pedimos el precio y lo convertimos a float

        # Creamos una instancia de Producto con los datos introducidos
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio
        )
        session.add(nuevo_producto)                    # Añadimos el nuevo producto a la sesión
        session.commit()                               # Guardamos los cambios en la base de datos

        print(f"\n✅ Producto '{nombre}' añadido correctamente.")







