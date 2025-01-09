from datetime import datetime
import flet as ft
from crud import pedido_crud
from crud import producto_crud
from schemas.producto_pedido_schema import ProductoPedido


FECHA_ACTUAL = datetime.now().strftime("%Y-%m-%d")

def get_next_id_pedido():
    try:
        pedidos = pedido_crud.obtener_pedidos()
        print(pedidos)
        print(type(pedidos))
        if pedidos:
            last_pedido = pedidos[-1]
            return last_pedido.id + 1
        else:
            return 1
    except Exception as e:
        raise RuntimeError(f"Error al obtener el siguiente ID de pedido: {e}")


def get_all_products():
    try:
        productos = producto_crud.obtener_productos()
        return productos
    except Exception as e:
        raise RuntimeError(f"Error al obtener los productos: {e}")


