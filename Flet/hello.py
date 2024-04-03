# Importing the library
import flet as ft

# ! Defining the main function
def main(page:ft.Page):
    
    # * Page Title
    page.title="Hello World!"

    # * Text
    text = ft.Text(value='My first flet app',color='purple',bgcolor="yellow")

    # * Appending & Updating to the page
    page.controls.append(text)
    page.update()


# ^ Starting the App
ft.app(target=main,view=ft.WEB_BROWSER)



