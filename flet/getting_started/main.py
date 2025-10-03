from time import sleep

import flet as ft


def main(page: ft.Page):
    """
    Due esempio di ft.Text:
     - txtIn: statico
     - txtOut: dinamico
    """
    txtIn = ft.Text(value="Buongiorno TdP 2024", color="red")
    # Aggiungo txtIn ai controlli
    page.controls.append(txtIn)
    # Aggiorno lo stato del mio controllo e visualizzo il controllo aggiunto
    page.update()

    txtOut = ft.Text(value="Counter:", color="red", size=24)
    page.controls.append(txtOut)
    page.update()
    # page.add(txtOut) equivale a:
    # 1. page.controls.append(txtOut)
    # 2. page.update()

    for i in range(1, 100):
        txtOut.value = "Counter: " + str(i)
        page.update()
        sleep(1)


ft.app(target=main, view=ft.AppView.FLET_APP)
