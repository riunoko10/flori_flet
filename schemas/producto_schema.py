from sqlmodel import SQLModel
from typing import Optional


class NuevoProducto(SQLModel):
    nombre: str
    descripcion: Optional[str]  # Descripción del producto
    precio: Optional[float]  # Precio del producto
    stock: Optional[int]  # Cantidad disponible en inventario