from sqlmodel import Session, select
from db.db_connection import engine
from schemas.producto_schema import Producto
from schemas.pedido_schema import NuevoPedido
from schemas.producto_pedido_schema import ProductoPedido


def set_producto_pedido(producto:Producto, pedido:NuevoPedido, cantidad:int):
    try:
        nuevo_poducto_pedido = ProductoPedido(
            producto_id=producto.id,
            pedido_id=pedido.id,
            cantidad=cantidad,
            subtotal=producto.precio * cantidad
        )
        with Session(engine) as session:
            session.add(nuevo_poducto_pedido)
            session.commit()
            session.refresh(nuevo_poducto_pedido)
        return nuevo_poducto_pedido
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al crear el producto y pedido: {e}")


def eliminar_producto_pedido(producto_pedido_id: int):
    try:
        with Session(engine) as session:
            producto_pedido = session.get(ProductoPedido, producto_pedido_id)
            if producto_pedido is None:
                raise RuntimeError(f"No se encontro el producto_pedido con ID {producto_pedido_id}.")
            session.delete(producto_pedido)
            session.commit()
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al eliminar el producto_pedido: {e}")


def obtener_productos_pedido(pedido_id: int):
    try:
        with Session(engine) as session:
            statement = select(ProductoPedido).where(ProductoPedido.pedido_id == pedido_id)
            productos_pedido = session.exec(statement)
            return productos_pedido
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al obtener los productos_pedido: {e}")