import flet as ft

def main(page: ft.Page):
    page.title = "App de contador"
    page.theme_mode = "Dark"
    page.vertical_alignment = "center"

    # Label principal "onde vai aparecer os números"
    numero = ft.TextField(value="0", text_align="center" ,width=100)

    # funções dos botões
    def menos_click(e):
        numero.value = int(numero.value) - 1
        page.update()

    def mais_click(e):
        numero.value = int(numero.value) + 1
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=menos_click),
                numero,
                ft.IconButton(ft.icons.ADD, on_click=mais_click)
            ],
            alignment="center"
        )
    )
ft.app(target=main)

# https://gallery.flet.dev/icons-browser/
# nesse site tem icones que o propio flet possui