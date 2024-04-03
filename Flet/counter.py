import flet as ft
from time import sleep

def main(page:ft.Page):
    page.title="Counter App - build with 'FLET'"
    text = ft.Text()
    page.add(text)
    for i in range(1,999999999+1):
        text.value = "Count"+" "+str(i)
        page.update()
        sleep(1) # * It will make the program sleep for 1 second

ft.app(target=main)