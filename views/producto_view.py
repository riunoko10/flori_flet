import flet as ft
from schemas.producto_schema import NuevoProducto
from logic import producto_logic


def producto_view(page: ft.Page):
    titulo = ft.Text("Registrar Producto", size=24, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
    
    table_productos = producto_logic.load_productos_table(producto_logic.get_table_productos, page)
    if table_productos is None:
        table_productos = producto_logic.get_table_productos()


    def on_agregar_producto(e):
        producto_logic.agregar_producto(nombre, descripcion, precio, stock, table_productos, page)
        table_container.content = producto_logic.load_productos_table(producto_logic.get_table_productos, page)
        nombre.value = ""
        descripcion.value = ""
        precio.value = ""
        stock.value = ""
        page.update()
    
    def on_eliminar_fila(gasto_id):
        producto_logic.eliminar_producto(gasto_id, table_productos, page)
        table_container.content = producto_logic.load_productos_table(producto_logic.get_table_productos, page)
        page.update()
    
    agregar_boton = ft.ElevatedButton(
    "Agregar", 
    on_click=on_agregar_producto,
    color=ft.colors.WHITE, 
    bgcolor=ft.colors.DEEP_ORANGE,
    col={ "xs": 12, "sm": 6, "md": 4, "lg": 2 }
    )

    nombre = ft.TextField(label="Nombre", bgcolor=ft.Colors.BLUE_GREY_700, col={ "xs": 12, "sm": 6, "md": 4, "lg": 3 })
    descripcion = ft.TextField(label="Descripcion", bgcolor=ft.Colors.BLUE_GREY_700, col={ "xs": 12, "sm": 6, "md": 4, "lg": 3 })
    precio = ft.TextField(label="Precio", bgcolor=ft.Colors.BLUE_GREY_700, col={ "xs": 12, "sm": 6, "md": 4, "lg": 3 })
    stock = ft.TextField(label="Cantidad en inventario", bgcolor=ft.Colors.BLUE_GREY_700, col={ "xs": 12, "sm": 6, "md": 4, "lg": 3 })


    input_container_responsive = ft.ResponsiveRow(
        [nombre, descripcion, precio, stock, agregar_boton],
        spacing=10, 
        alignment=ft.MainAxisAlignment.CENTER,
    )



    table_container = ft.Container(
        content=table_productos,
        alignment=ft.alignment.center
    )


    return ft.Column([titulo, input_container_responsive, table_container])

