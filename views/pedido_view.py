import flet as ft
from logic import pedido_logic


def pedido_view(page: ft.Page):
    
    titulo = ft.Text("Registrar Pedido", size=24, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)

    
    


    def product_on_search():
        all_products = pedido_logic.get_all_products()
        list_products = []
        for product in all_products:
            print(product)
            list_products.append(ft.ListTile(
                title=ft.Text(product.nombre, color=ft.Colors.WHITE),
                subtitle=ft.Text(product.descripcion, color=ft.Colors.WHITE),
                on_click=close_anchor,
                data=product
            ))
        buscar_producto.controls = list_products



    def on_agregar_pedido(e):
        print("Agregar Pedido")
        next_id = pedido_logic.get_next_id_pedido()
        numero_pedido.value = f"ART-{next_id}"
        row_add_product.visible = True
        product_on_search()
        page.update()


    agregar_pedido = ft.ElevatedButton(
        "Nuevo Pedido",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.DEEP_ORANGE,
        col={"xs": 12, "sm": 4, "md": 3, "lg": 2},
        on_click=on_agregar_pedido
    )

  

    numero_pedido = ft.TextField(
        label="Numero de Pedido",
        bgcolor=ft.Colors.BLUE_GREY_700,
        col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
        disabled=True
    )

    row_botones = ft.Row(
        [numero_pedido,agregar_pedido],
        spacing=10,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    def close_anchor(e):
        text = f"{e.control.data.nombre}"
        print(f"closing view from {text}")
        buscar_producto.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")
        buscar_producto.open_view()


    # a1 = ft.ListTile(
    #     title=ft.Text("One-line list tile", color=ft.Colors.WHITE),
    #     on_click=close_anchor,
    #     data="red"
    # )
    # a2 = ft.ListTile(
    #     title=ft.Text("One-line list tile", color=ft.Colors.WHITE),
    #     on_click=close_anchor, 
    #     data="blue"
    # )

    agregar_producto = ft.ElevatedButton(
        "Agregar Producto",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.DEEP_ORANGE,
        col={"xs": 12, "sm": 3, "md": 3, "lg": 2},
    )
    

    buscar_producto = ft.SearchBar(
        view_elevation=4,
        bar_hint_text="Buscar Producto",
        col={"xs": 12, "sm": 5, "md": 5, "lg": 6},
        divider_color=ft.Colors.BLUE_GREY_700,
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        # controls=[a1,a2],
    )

    row_add_product = ft.ResponsiveRow(
        [buscar_producto, agregar_producto],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        visible=False
    )


    return ft.Column(
        [titulo, row_botones, row_add_product]
    )