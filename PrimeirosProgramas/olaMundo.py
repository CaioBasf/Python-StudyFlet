import flet as ft

def main(page : ft.Page):

    # o titulo principal da página
    page.title = "Olá, Mundo"

    # Variavel de texto
    text = ft.Text(value="Meu primeiro Olá Mundo em flet!", color="black")

    # Colocando e atualizando o text na página
    page.controls.append(text)
    page.update()

# inicializando o app na função Main
ft.app(target=main)

#Com esse comando eu tranformo meu app em Site
#ft.app(target=main, view=ft.WEB_BROWSER)

# Se iniciar apenas rodando com o VS precisará ficar saindo e colocando na aplicação
# Se iniciar com flet <Código> ele atualizara automaticamente.