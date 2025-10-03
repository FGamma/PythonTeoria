from time import sleep

import flet as ft


def main(page: ft.Page):
    """
    - Event handlers
    Alcuni controlli possono triggerare eventi (es. il bottone quando viene
    cliccato).
    - Row
    I controlli come Row, Column, Dropdown possono contenere controlli figli.
    """

    # Quando clicco un bottone genero un evento che è passato come ingresso
    # al mio metodo.
    def handleBottone(e):
        """
        Quando clicco il bottone mi compare il campo "Pulsante Cliccato"
        """
        txtOut.value = ""
        page.update()
        sleep(1)
        txtOut.value = "Pulsante Cliccato"
        page.update()

    txt1 = ft.Text(value="Colonna 1:", color="red")
    txt2 = ft.Text(value="Colonna 2:", color="blue")
    btn = ft.ElevatedButton(text="Premi qui", on_click=handleBottone)
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=24)
    page.add(row1, txtOut)
    page.update()


ft.app(target=main, view=ft.AppView.FLET_APP)
