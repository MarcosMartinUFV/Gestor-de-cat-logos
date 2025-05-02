from funciones.crear import crear_producto       # Importa función para añadir producto
from funciones.leer import mostrar_productos     # Importa función para mostrar productos
from funciones.actualizar import actualizar_producto  # Importa función para actualizar productos
from funciones.eliminar import eliminar_producto     # Importa función para eliminar productos

def mostrar_menu():
    print("\n--- GESTOR DE CATÁLOGO ---")
    print("1. Añadir producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
def main():
    while True:
        mostrar_menu()               # Muestra opciones en pantalla
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            crear_producto()        # Añade nuevo producto
        elif opcion == "2":
            mostrar_productos()     # Muestra todos los productos
        elif opcion == "3":
            actualizar_producto()   # Permite actualizar uno
        elif opcion == "4":
            eliminar_producto()     # Permite eliminar uno
        elif opcion == "5":
            print("Saliendo del programa.")
            break                   # Sale del bucle y termina
        else:
            print("Opción no válida. Intenta de nuevo.")

if _name_ == "_main_":
    main()  # Ejecuta el programa cuando se ejecuta menu.py directamente