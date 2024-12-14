import flet as ft
from views.gastos_view import gastos_view
from logic import validate_and_create_tables

def main(page: ft.Page):
    validate_and_create_tables()  # Validate and create tables before starting the app

    page.title = "Arte Floral"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Gastos", content=gastos_view(page)),
            # Agrega más pestañas aquí para otras vistas
        ],
    )

    page.add(tabs)
    page.update()

ft.app(main)