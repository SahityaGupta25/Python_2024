import flet as ft
def main(page = ft.Page):
    page.title = "Fruits & Cricketers"
    page.add(
        ft.Row(controls=[ft.Text("My favorite fruits :\n")]),
             ft.Row(
                 controls=[
                     ft.Text("Apple"),
                     ft.Text("Papaya"),
                     ft.Text("Mango")
                 ]
             ),
        ft.Column(controls=[ft.Text("My favorite Cricketer:\n")]),
             ft.Column(
                 controls=[
                     ft.Text("Sachin"),
                     ft.Text("Virat"),
                     ft.Text("Dhoni")
                 ]
             )
    )
    #! page.update()

ft.app(target=main)