import flet as ft

def main(page: ft.Page):
    page.title = "Minhas coisas favoritas!"

    # Da o output em uma linha
    page.add(
        ft.Row(controls=[ft.Text("Minhas frutas favoritas: \n")]),
        ft.Row(
            controls=[ 
                ft.Text("Abacate"),
                ft.Text("Goiaba"),
                ft.Text("Manga")
            ]
        ),
    # Da o output em uma coluna
    ft.Column(controls=[ft.Text("Meus pilotos favoritoss: \n")]),
    ft.Column(
        controls=[ 
            ft.Text("Ayrton Senna"),
            ft.Text("Max Verstappen"),
            ft.Text("Vitor Genz")
        ]
    )
)


ft.app(target=main)