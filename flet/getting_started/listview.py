from time import sleep

import flet as ft


def main(page: ft.Page):
    """
    Esempio di ListView
    """
    # Quando clicco un bottone genero un evento che è passato come ingresso
    # al mio metodo.
    def handleBottone(e):
        """
        Aggiungo campi a ListView
        """
        lv.controls.append(ft.Text("Tasto cliccato"))
        lv.update()

    txt1 = ft.Text(value="Colonna 1:", color="red")
    txt2 = ft.Text(value="Colonna 2:", color="blue")
    btn = ft.ElevatedButton(text="Premi qui", on_click=handleBottone)
    row1 = ft.Row([txt1, txt2, btn])
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(row1, lv)
    page.update()


ft.app(target=main, view=ft.AppView.FLET_APP)
