"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame
superato, e una classe Libretto, che contiene l'elenco dei voti di uno
studente.
"""


class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio != 30:
            raise ValueError("Lode non applicabile")

    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return (f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, "
                f"{self.lode}, '{self.data}')")


class Libretto:
    def __init__(self):
        # Per convenzione un attributo privato inizia con _
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi) / len(punteggi)


voto_1 = Voto("Analisi Matematica 1", 10, 28,
              False, "2022-02-10")
voto_2 = Voto("Basi di Dati", 8, 30,
              True,"2023-06-15")

mio_libretto = Libretto()
mio_libretto.append(voto_1)
mio_libretto.append(voto_2)

print(f"Media libretto: {mio_libretto.media()}")

print(
    f"""
    mio_libretto._voti: {mio_libretto._voti}
    Python la fa eseguire, non da errori ma per convenzione NON si puo fare.
"""
)
