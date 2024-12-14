import flet as ft
from logic import get_table_gastos, load_gastos_table, agregar_fila, eliminar_fila
from schemas.gastos_schemas import CategoriaEnum

def gastos_view(page: ft.Page):
    titulo = ft.Text("Registrar Gastos", size=24, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
    
    table_gastos = load_gastos_table(get_table_gastos, page)
    if table_gastos is None:
        table_gastos = get_table_gastos()  # Asegúrate de que table_gastos no sea None

    def on_agregar_fila(e):
        agregar_fila(descripcion, categoria_dd, importe, table_gastos, page)
        table_container.content = load_gastos_table(get_table_gastos, page)
        page.update()

    def on_eliminar_fila(gasto_id):
        eliminar_fila(gasto_id, table_gastos, page)
        table_container.content = load_gastos_table(get_table_gastos, page)
        page.update()

    agregar_boton = ft.ElevatedButton(
        "Agregar", 
        on_click=on_agregar_fila, 
        color=ft.colors.WHITE, 
        bgcolor=ft.colors.DEEP_ORANGE
    )

    descripcion = ft.TextField("Descripcion", bgcolor=ft.Colors.BLUE_GREY_700)
    importe = ft.TextField("Importe", bgcolor=ft.Colors.BLUE_GREY_700)

    categoria_dd = ft.Dropdown(
        options=[ft.dropdown.Option(categoria.value, text=categoria.value) for categoria in CategoriaEnum],
        width=200,
    )

    input_container = ft.Row([descripcion, categoria_dd, importe, agregar_boton], spacing=10, alignment=ft.MainAxisAlignment.CENTER)

    table_container = ft.Container(
        content=table_gastos,
        alignment=ft.alignment.center
    )

    return ft.Column([titulo, input_container, table_container])
