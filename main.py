import flet as ft
from datetime import datetime
from schemas.gastos_schemas import CategoriaEnum
from logger import get_logger
from logic import get_table_gastos, load_gastos_table, agregar_fila, eliminar_fila

logger = get_logger(__name__)

FECHA_ACTUAL = datetime.now().strftime("%Y-%m-%d")

def main(page: ft.Page):
    page.title = "Arte Floral"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Registrar Gastos", size=24, color=ft.Colors.WHITE)
    
    table_gastos = load_gastos_table(get_table_gastos, page)
    if table_gastos is None:
        table_gastos = get_table_gastos()  # Asegúrate de que table_gastos no sea None

    def on_agregar_fila(e):
        agregar_fila(descripcion, categoria_dd, importe, table_gastos, page)

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

    page.add(titulo, input_container, table_gastos)
    page.update()  # Asegúrate de actualizar la página

ft.app(main)