from datetime import datetime
import flet as ft
from crud import gastos_crud
from schemas.gastos_schema import NuevoGasto

FECHA_ACTUAL = datetime.now().strftime("%Y-%m-%d")

def get_table_gastos():
    table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_700,
        border=ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3,ft.colors.BLUE_GREY_200),
        horizontal_lines=ft.border.BorderSide(1,ft.colors.BLUE_GREY_500),
        columns=[
            ft.DataColumn(ft.Text("Descripcion", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Categoria", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Importe", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Fecha", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("Acciones", color=ft.Colors.WHITE)),  # Nueva columna para acciones
        ],
        rows=[]
    )
    return table

def load_gastos_table(get_table, page):
    try:
        result = gastos_crud.obtener_gastos()
        table_gastos = get_table()
        if result:
            for gasto in result:
                nueva_fila = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(gasto.descripcion, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(gasto.categoria, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(gasto.importe, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.Text(gasto.fecha, color=ft.Colors.WHITE)),
                        ft.DataCell(ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.Colors.RED,
                            on_click=lambda e, gasto_id=gasto.id: eliminar_fila(gasto_id, table_gastos, page)
                        )),  # Botón de eliminar
                    ]
                )
                table_gastos.rows.append(nueva_fila)
        else:
            print("No se encontraron datos en la base de datos.")  # Mensaje de depuración
        return table_gastos
    except Exception as e:
        raise RuntimeError(f"Error al cargar los gastos: {e}")

def agregar_fila(descripcion, categoria_dd, importe, table_gastos, page):
    descripcion_data = descripcion.value
    categoria_data = categoria_dd.value  # Toma la información del dropdown
    importe_data = importe.value
    nuevo_gasto = NuevoGasto(
        descripcion=descripcion_data, 
        categoria=categoria_data, 
        importe=importe_data, 
    )
    gasto_creado = gastos_crud.crear_gasto(nuevo_gasto)
    nueva_fila = ft.DataRow(
        cells=[
            ft.DataCell(ft.Text(descripcion_data, color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(categoria_data, color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(importe_data, color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(FECHA_ACTUAL, color=ft.Colors.WHITE)),
            ft.DataCell(ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.Colors.RED,
                on_click=lambda e, gasto_id=gasto_creado.id: eliminar_fila(gasto_id, table_gastos, page)
            )),  # Botón de eliminar
        ])
    table_gastos.rows.append(nueva_fila)
    descripcion.value = ""
    categoria_dd.value = None  # Limpia el dropdown
    importe.value = ""
    page.update()

def eliminar_fila(gasto_id, table_gastos, page):
    gastos_crud.eliminar_gasto(gasto_id)
    # Refresh the table after deletion
    updated_table = load_gastos_table(get_table_gastos, page)
    table_gastos.rows.clear()
    table_gastos.rows.extend(updated_table.rows)
    page.update()
