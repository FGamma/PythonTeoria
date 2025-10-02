from dataclasses import dataclass

@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

# _test_voto: convenzione per dire che non bisogna importarlo.
def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, '2024-03-11')
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

# STAND-ALONE: testo il modulo separatamente, lanciando il modulo.
# Nel modulo scrivo classi e istruzioni per testarle. Quando le classi sono
# pronte invece di buttare via le istruzioni di test, le tengo qui con questo
# codice che mi evita di eseguire questo codice quando faccio il run del main.
# Ogni volta che devo migliorare qualcosa, lo posso fare qui facendo il run
# del modulo stesso.
# Se faccio il run del main: __name__ qui vale voto (prova in debug)
# Se faccio il run qui     : __name__ vale __main__ (prova in debug)
if __name__=="__main__":
    _test_voto()
