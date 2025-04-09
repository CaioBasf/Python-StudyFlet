import flet as ft

def main(page: ft.Page):
    page.title = "App de boas vindas!"
    page.theme_mode = "Dark"
    
    # Input do nome do usuario
    inputNome = ft.TextField(label="Coloque seu primeiro nome", autofocus=True)
    # Input do sobrenome do usuario
    inputSobrenome = ft.TextField(label="Coloque seu sobrenome")

    controleDeColuna = ft.Column()
    # Função de quando o botão é clicado
    def BoasVindas(e):
        page.add(ft.Text(f"Bem vindo(a) {inputNome.value} {inputSobrenome.value}"))
        inputNome.value = ""
        inputSobrenome.value = ""
        inputNome.focus()
        inputSobrenome.focus()
        

    # Botão clicavel
    botao = ft.ElevatedButton(text="Botão de boas vindas!", on_click=BoasVindas)

    page.add(
        ft.Column(
            [
            inputNome,
            inputSobrenome,
            botao
            ]
    )
)
ft.app(target=main)