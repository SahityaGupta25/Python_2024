import flet as ft
def main(page = ft.Page):
    page.title = "Fruits & Cricketers"
    page.add(ft.Row(controls=[ft.Text("My favorite fruits :\n")]))
    #! page.update()

ft.app(target=main)