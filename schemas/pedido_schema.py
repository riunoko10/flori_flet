from sqlmodel import SQLModel


class NuevoPedido(SQLModel):
    cliente: str
    total: float = 0.0