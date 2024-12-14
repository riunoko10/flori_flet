from sqlmodel import SQLModel, Field
from datetime import datetime



class Gasto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    descripcion: str
    categoria: str
    importe: float
    fecha: datetime = Field(default=datetime.now())


