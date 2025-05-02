from basedatos import Session
from tablas.producto import Producto

def actualizar_producto():
    session = Session()
    try:
        id_producto = int(input("Introduce el ID del producto a modificar: "))
        producto = session.query(Producto).get(id_producto)

        if producto:
            nuevo_nombre = input(f"Nombre actual ({producto.nombre}): ") or producto.nombre
            nueva_descripcion = input(f"Descripción actual ({producto.descripcion}): ") or producto.descripcion
            nuevo_precio = input(f"Precio actual ({producto.precio}): ") or producto.precio
            nuevo_stock = input(f"Stock actual ({producto.stock}): ") or producto.stock

            producto.nombre = nuevo_nombre
            producto.descripcion = nueva_descripcion
            producto.precio = int(nuevo_precio)
            producto.stock = int(nuevo_stock)

            session.commit()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("❌ ID, precio o stock no válidos.")
    finally:
        session.close()
