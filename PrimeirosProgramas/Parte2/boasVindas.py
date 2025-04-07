import flet as ft

def main(page: ft.Page):
    page.title = "App de boas vindas!"
    page.theme_mode = "Dark"
    
    inputNome = ft.TextField(hint_text="Coloque seu primeiro nome: ", width="350")
    inputSobrenome = ft.TextField(hint_text="Coloque seu sobrenome: ", width="350")

    def BotaoOla(e):
        page.add(ft.Text(f"Bem vindo(a) {inputNome.value} {inputSobrenome.value}"))

    page.add(
        ft.Column(
            [
            inputNome,
            inputSobrenome,
            ft.ElevatedButton(text="Botâo de boas vindas!", on_click=BotaoOla)
            ]
    )
)
ft.app(target=main)