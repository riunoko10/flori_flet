from sqlmodel import Session, select
from db.db_connection import engine
from models.models import Pedido



def crear_pedido(cliente: str):
    try:
        with Session(engine) as session:
            # Crear el pedido
            pedido = Pedido(cliente=cliente, total=0.0)
            session.add(pedido)
            session.commit()
            session.refresh(pedido)
        return pedido
    except Exception as e:
        raise RuntimeError(f"Error al crear el pedido: {e}")


def eliminar_pedido(pedido_id: int):
    """
    Eliminar un pedido y restaurar el stock de los productos asociados.
    :param pedido_id: ID del pedido a eliminar.
    """
    try:
        with Session(engine) as session:
            pedido = session.get(Pedido, pedido_id)
            if not pedido:
                raise RuntimeError(f"No se encontró el pedido con ID {pedido_id}.")
            session.delete(pedido)
            session.commit()
    except Exception as e:
        raise RuntimeError(f"Error al eliminar el pedido: {e}")


def obtener_pedido(pedido_id: int) -> Pedido:
    """
    Obtener detalles de un pedido, incluyendo productos y subtotales.
    :param pedido_id: ID del pedido.
    :return: Diccionario con los detalles del pedido.
    """
    try:
        with Session(engine) as session:
            pedido = session.get(Pedido, pedido_id)
            if not pedido:
                raise RuntimeError(f"No se encontró el pedido con ID {pedido_id}.")
        return pedido
    except Exception as e:
        raise RuntimeError(f"Error al obtener el pedido: {e}")

def obtener_pedidos():
    try:
        with Session(engine) as session:
            pedidos = session.exec(select(Pedido)).all()
            return pedidos
    except Exception as e:
        raise RuntimeError(f"Error al obtener los pedidos: {e}")
