# Gestor-de-cat-logos

Este proyecto permite gestionar un catálogo de productos mediante una aplicación en Python con interfaz de texto. Está construido con SQLite como base de datos y SQLAlchemy como ORM, y sigue una estructura modular clara para facilitar el trabajo en equipo.

## 🎯 Objetivo

El objetivo principal es implementar un sistema que permita:
- Añadir nuevos productos
- Consultar productos registrados
- Modificar sus datos
- Eliminar productos del catálogo

Todo esto a través de un menú interactivo en consola, con persistencia en base de datos y buenas prácticas de programación.

---

## 📂 Estructura del Proyecto

Gestor_de_catalogos/
├── README.md               # Explicación general del proyecto
├── .gitignore              # Archivos ignorados por Git
├── basedatos.py            # Configuración de conexión a SQLite con SQLAlchemy
├── menu.py                 # Menú interactivo de consola
├── requirements.txt        # Lista de dependencias
├── catalogo.db             # Base de datos SQLite
├── funciones/              # Funciones CRUD
│   ├── crear.py            # Añadir productos
│   ├── leer.py             # Ver productos
│   ├── actualizar.py       # Editar productos
│   ├── eliminar.py         # Eliminar productos
├── tablas/                 # Modelos ORM
│   └── producto.py         # Clase Producto generada desde SQLite



## FUNCIONES ÚTILES
🔹 Uso programa
-- python3 menu.py → Iniciar el programa

🔹 Gestión de Git
-- git branch                       # Ver ramas locales
-- git checkout nombre-rama         # Cambiar de rama
-- git add .                        # Añadir todos los cambios
-- git commit -m "Mensaje claro"    # Hacer commit con mensaje humano
-- git push -u origin nombre-rama   # Subir nueva rama a GitHub
-- git pull                         # Traer últimos cambios del repositorio
-- git log --oneline --graph --all  # Ver historial de commits con ramas

🔹 Gestión de SQLite
-- sqlite3 catalogo.db              # Abrir la base de datos desde terminal
-- .tables                          # Ver todas las tablas
-- .schema producto                 # Ver la estructura de la tabla producto
-- .quit                            # Salir del modo SQLite

## Dependencias y requisitos con `requirementes.txt`

Es muy importante mantener actualizado el archivo `requirements.txt`. Puesto que es fundamental para cualquier proyecto en Python que vaya a utilizar librerías externas.

Si se instalan nuevas librerías y no se añaden a este archivo, pueden encontrarse con errores al intentar instalar las dependencias usando: pip install -r requirements.txt.





