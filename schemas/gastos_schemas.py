from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional
from enum import Enum



class CategoriaEnum(str, Enum):
    FLORES = "Flores"
    MATERIALES = "Materiales"
    TRANSPORTE = "Transporte"
    OTROS = "Otros"

class NuevoGasto(SQLModel):
    descripcion: str
    categoria: str
    importe: float
    fecha: Optional[datetime] = datetime.now()


    