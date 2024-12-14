from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional



class Gasto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    descripcion: str
    categoria: str
    importe: float
    fecha: datetime = Field(default=datetime.now())

class Producto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    descripcion: Optional[str]  # Descripción del producto
    precio: Optional[float]  # Precio del producto
    stock: Optional[int]  # Cantidad disponible en inventario
    pedidos: List["PedidoProducto"] = Relationship(back_populates="producto")


class Pedido(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    cliente: str  # Nombre del cliente
    total: float = Field(default=0.0)  # Total del pedido
    fecha: datetime = Field(default=datetime.now())
    productos: List["PedidoProducto"] = Relationship(back_populates="pedido")


class PedidoProducto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedido.id")
    producto_id: int = Field(foreign_key="producto.id")
    cantidad: int  # Cantidad comprada de este producto
    subtotal: float  # Precio total para este producto en el pedido

    pedido: Pedido = Relationship(back_populates="productos")
    producto: Producto = Relationship(back_populates="pedidos")