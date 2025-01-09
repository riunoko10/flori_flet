from sqlmodel import Session, select
from db.db_connection import engine
from models.models import Producto
from schemas.producto_schema import NuevoProducto


def crear_producto(nuevo_producto: NuevoProducto):
    try:
        producto = Producto(
            nombre=nuevo_producto.nombre,
            descripcion=nuevo_producto.descripcion,
            precio=nuevo_producto.precio,
            stock=nuevo_producto.stock
        )
        with Session(engine) as session:
            session.add(producto)
            session.commit()
            session.refresh(producto)
        return producto
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al crear el producto: {e}")


def obtener_productos():
    try:
        with Session(engine) as session:
            productos = session.exec(select(Producto), execution_options={"prebuffer_rows": True}).all()
            return productos
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al obtener los productos: {e}")

def eliminar_producto(producto_id: int):
    try:
        with Session(engine) as session:
            producto = session.get(Producto, producto_id)
            if producto is None:
                raise RuntimeError(f"No se encontro el producto con ID {producto_id}.")
            session.delete(producto)
            session.commit()
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error al eliminar el producto: {e}")