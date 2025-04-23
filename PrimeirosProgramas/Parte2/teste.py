import flet as ft

def main(page: ft.Page):
    page.title = "Greetings"
    def hello(e):
        text = (f"Hello {first.value} {middle.value} {last.value}")
        row.controls.append(ft.Text(text)) 
        first.value = ""
        middle.value = ""
        last.value = ""
        page.update()
        

    first = ft.TextField(label="first name", width=300)
    middle = ft.TextField(label="middle name", width=300)
    last = ft.TextField(label="last name", width=300)
    button = ft.ElevatedButton(text="push me", on_click=hello)
    text = ""
    row =  ft.Row([ft.Text(text)])
    page.add(first, middle, last, button, row)

ft.app(target=main)