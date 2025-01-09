from sqlmodel import Session, select
from db.db_connection import get_session
from schemas.gastos_schema import NuevoGasto
from models.models import Gasto



def crear_gasto(nuevo_gasto: NuevoGasto):
    try:
        nuevo_gasto = Gasto(
            descripcion=nuevo_gasto.descripcion, 
            categoria=nuevo_gasto.categoria, 
            importe=nuevo_gasto.importe, 
            fecha=nuevo_gasto.fecha
        )
        response = None
        with get_session() as session:
            session.add(nuevo_gasto)
            session.commit()
            session.refresh(nuevo_gasto)
            response =  nuevo_gasto
        return response
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al crear el gasto: {e}")


def obtener_gastos():
    try:
        with get_session() as session:
            statement = select(Gasto)
            gastos = session.exec(statement, execution_options={"prebuffer_rows": True})
        return gastos
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al obtener los gastos: {e}")


def eliminar_gasto(gasto_id: int):
    try:
        with get_session() as session:
            gasto = session.get(Gasto, gasto_id)
            if gasto is None:
                raise RuntimeError(f"No se encontro el gasto con ID {gasto_id}.")
            session.delete(gasto)
            session.commit()
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al eliminar el gasto: {e}")