from sqlmodel import Session, select
from db.db_connection import engine
from schemas.gastos_schemas import NuevoGasto
from models.models import Gasto



def crear_gasto(nuevo_gasto: NuevoGasto):
    try:
        nuevo_gasto = Gasto(
            descripcion=nuevo_gasto.descripcion, 
            categoria=nuevo_gasto.categoria, 
            importe=nuevo_gasto.importe, 
            fecha=nuevo_gasto.fecha
        )
        with Session(engine) as session:
            session.add(nuevo_gasto)
            session.commit()
            session.refresh(nuevo_gasto)
        return nuevo_gasto
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al crear el gasto: {e}")


def obtener_gastos():
    try:
        with Session(engine) as session:
            gastos = session.query(Gasto).all()
            return gastos
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al obtener los gastos: {e}")

def eliminar_gasto(gasto_id: int):
    with Session(engine) as session:
        gasto = session.get(Gasto, gasto_id)
        if gasto:
            session.delete(gasto)
            session.commit()