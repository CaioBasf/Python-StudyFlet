import flet as ft
from time import sleep

# Definindo a função principal
def main(page: ft.Page):
    page.title = "App de cronometrô" # Colocando o texto do app

    text = ft.Text() # Variavel de input
    page.add(text) # Adicionar a página

    for i in range(1,11):
        text.value = "Cronometrô: " + str(i)
        page.update()
        sleep(1) # Vai fazer o programa parar por 1 segundo

ft.app(target=main)


"""
page.controls.append()
page.update()
-->
page.add(text)
"""