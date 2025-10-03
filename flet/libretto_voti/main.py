import flet as ft

from controller import Controller
from view import View


def main(page: ft.Page):
    # View è l'unico che conosce e che può modificare la pagina. L'unico con
    # il parametro page.
    v = View(page)
    # Il controllore è l'unico che può parlare sia con il View che con il Model.
    # Il controllore prende come ingresso il View
    c = Controller(v)
    # Dico al View che il suo controllore è c
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
