import flet as ft
from schemas.producto_schema import NuevoProducto
from crud import producto_crud

def get_table_productos():
    table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_700,
        border=ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3,ft.colors.BLUE_GREY_200),
        horizontal_lines=ft.border.BorderSide(1,ft.colors.BLUE_GREY_500),
        columns=[
            ft.DataColumn(ft.Text("Nombre", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Descripcion", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Precio", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Stock", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Acciones", color=ft.Colors.WHITE)),  # Nueva columna para acciones
        ],
        rows=[]
    )
    return table

def load_productos_table(get_table_productos, page):
    try:
        result = producto_crud.obtener_productos()
        print("Productos:")
        print(result)
        table_productos = get_table_productos()
        if result:
            for producto in result:
                nueva_fila = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(producto.nombre, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(producto.descripcion, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(producto.precio, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(producto.stock, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.Colors.RED,
                            on_click=lambda e, producto_id=producto.id: eliminar_producto(producto_id, table_productos, page)
                        )),  # Botón de eliminar
                    ]
                )
                table_productos.rows.append(nueva_fila)
        else:
            print("No se encontraron datos en la base de datos.")  # Mensaje de depuración
        return table_productos
    except Exception as e:
        raise RuntimeError(f"Error al cargar los productos: {e}")


def agregar_producto(nombre, descripcion, precio, stock, table_productos, page):
    nombre_data = nombre.value
    descripcion_data = descripcion.value
    precio_data = precio.value
    stock_data = stock.value
    nuevo_producto = NuevoProducto(
        nombre=nombre_data,
        descripcion=descripcion_data,
        precio=precio_data,
        stock=stock_data,
    )
    try:
        result = producto_crud.crear_producto(nuevo_producto)
        if result:
            print("Producto agregado correctamente.")
            table_productos.content = load_productos_table(get_table_productos, page)
            page.update()
        else:
            print("No se pudo agregar el producto.")
    except Exception as e:
        raise RuntimeError(f"Error al agregar el producto: {e}")


def eliminar_producto(producto_id, table_productos, page):
    try:
        producto_crud.eliminar_producto(producto_id)
        update_table_productos = load_productos_table(get_table_productos, page)
        table_productos.rows.clear()
        table_productos.rows.extend(update_table_productos.rows)
        page.update()
    except Exception as e:
        raise RuntimeError(f"Error al eliminar el producto: {e}")