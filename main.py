import flet as ft
from views.gastos_view import gastos_view
from views.producto_view import producto_view
from logic.db_logic import validate_and_create_tables



def main(page: ft.Page):
    validate_and_create_tables()  # Validate and create tables before starting the app

    page.title = "Arte Floral"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Gastos", content=gastos_view(page)),
            ft.Tab(text="Productos", content=producto_view(page)),
            # Agrega más pestañas aquí para otras vistas
        ],
        expand=1,
    )

    page.add(tabs)
    page.update()

ft.app(main)