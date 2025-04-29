from sqlalchemy import Column, Integer, String
from basedatos import Base  # Importa la clase Base desde basedatos.py

class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    precio = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
