import flet as ft

def main(page: ft.Page):
    page.title = "App to-do!"
    page.theme_mode = "Dark"

    # Pegando o input do usuario
    inputTexto = ft.TextField(hint_text="Oque você quer fazer... ", width=350)
    
    # Função para gerar uma CheckBox com o texto inputado quando é clickado
    def ClickBotao(e):
        page.add(ft.Checkbox(label=inputTexto.value))

    # Alinhando o texto de input e o botâo em uma linha
    page.add(
        ft.Row(
            # Ao inves de controls pode-se usar apenas []
            [
                inputTexto,
                # Criação do botão para clickar
                ft.ElevatedButton(text="Adicionar", on_click=ClickBotao)
            ]

        )
    )

ft.app(target=main)