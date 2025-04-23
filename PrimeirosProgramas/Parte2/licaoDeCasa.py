# Fazer um app que peça os três tipo de nome e escreva

import flet as ft

def main(page: ft.Page):
    page.title = "Licão de Casa"
    page.theme_mode = "Dark"

    nome = ft.TextField(label="Coloque seu primeiro nome", width=500, autofocus=True)
    sobrenome = ft.TextField(label="Coloque seu sobrenome", width=500)
    ultimoNome = ft.TextField(label="Coloque seu ultimo nome", width=500)

# Função de Boas vindas
    def BoasVindas(e):
        page.add(ft.Text(f"Olá {nome} {sobrenome} {ultimoNome}"))
        nome.value = sobrenome.value = ultimoNome.value = " "
        nome.focus()
        page.update()

    botao = ft.ElevatedButton(text="Click", on_click=BoasVindas)


    page.add(
            nome,
            sobrenome,
            ultimoNome,
            botao
    )

ft.app(target=main)