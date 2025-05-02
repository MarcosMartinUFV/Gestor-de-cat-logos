from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()  # Clase base para modelos ORM

engine = create_engine("sqlite:///catalogo.db", echo=True)  # Conexión a SQLite con logging activado
Session = sessionmaker(bind=engine)  # Creador de sesiones
