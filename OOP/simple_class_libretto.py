"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame
superato, e una classe Libretto, che contiene l'elenco dei voti di uno
studente.
"""


class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        # Posso definire gli attributi (parametri costruttore) anche al di
        # fuori del costruttore, nei metodi successivi.
        # Ma per pulizia è consigliabile inserirli nel costruttore.
        # Il costruttore deve fare controlli di validità sul dato perchè Python
        # non fa controlli sui tipi dei valori passati.
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio != 30:
            raise ValueError("Lode non applicabile")

    # Definisco un metodo stringa
    def stringa(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    # Metodi DUNDER (speciali): DUNDER init, DUNDER str, DUNDER repr
    # (DUNDER si usa nel parlato dei metodi con __metodo__)
    # __str__: usato quando voglio mostrare le cose all'esterno
    # (print, GUI, ecc).
    # --repr__: fammi vedere la tua rappresentazione interna (utile al
    # programmatore (in debug)). Restituisce una stringa, ma questa
    # è pensata per il programmatore.
    # La stinga che costruisco è la chiamata che farei per costruire
    # quell'oggetto. Il metodo __repr__ stampa le info sotto forma di chiamata
    # al costruttore.
    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return (
            f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, "
            f"{self.lode}, '{self.data}')"
        )


class Libretto:
    def __init__(self):
        # Definisco una proprietà voti, con zero voti dentro
        self.voti = []

    def append(self, voto):
        self.voti.append(voto)

    def media(self):
        if len(self.voti) == 0:
            raise ValueError("Elenco voti vuoto")
        # In Java NON va bene perchè sto leggendo nella classe Libretto,
        # l'attributo punteggio della classe Voto. Le proprietà della classe
        # sono private e nessun oggetto può leggere le mie proprietà se non ho
        # un metodo get. Qui non serve perchè in Python tutti gli
        # attributi di una classe sono pubblici.
        # Il concetto di visibilità degli attributi non c'è in Python,
        # sono tutti pubblici anche se ci sono convenzioni basate su _
        # (preferirei che questa variabili non la toccassi)
        punteggi = [v.punteggio for v in self.voti]
        return sum(punteggi) / len(punteggi)


# Creo voto_1, voto_2 che sono 2 istanze della classe Voto
# Creare un nuovo oggetto di una classe è equivalente a chiamare il metodo init
# di quella classe
voto_1 = Voto("Analisi Matematica 1", 10, 28, False, "2022-02-10")
voto_2 = Voto("Basi di Dati", 8, 30, True, "2023-06-15")

# Stampa il riferimento a quell'oggetto se non definisco __str__
# print(f"Stampa il riferimento a quell'oggetto: {voto_1}")

# Stringa è un metodo della classe Voto.
# Metodo 1
print(f"Metodo 1: print(voto_1.stringa()): {voto_1.stringa()}")

# Metodo 2
print(f"Metodo 2: print(voto_1.__str__()): {voto_1.__str__()}")

# Metodo 3
print(f"Metodo 3: print(voto_1): {voto_1}")

# Chiama __str__
print(f"Chiama __str__ print(voto_1, voto_2): {voto_1, voto_2}")

# Metto 2 oggetti in una lista
miei_voti = [voto_1, voto_2]
# Qui Python usa __repr__ e non __str__. Se non avessi definito __repr__
# ma solo __str__ la stampa mi mostra i riferimenti in una lista.
print(f"Chiama __repr__ print(miei_voti): {miei_voti}")
