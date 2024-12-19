from sqlmodel import SQLModel
from typing import Optional



class ProductoPedido(SQLModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    subtotal: float