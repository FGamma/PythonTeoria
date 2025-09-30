import operator
from dataclasses import dataclass


@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile punteggio,
        tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio (senza lode), sotto forma
        di stringa (quindi non restituire self.punteggio ma una stringa,
        ovvero f"{self.punteggio}")
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"

    def copy(self):
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

    def __str__(self):
        return f"{self.esame} ({self.cfu}): voto {self.str_punteggio()} il {self.data}"




class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            # Uso self per il metodo perchè è mio
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi) / len(punteggi)

    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona tutti e soli i soli voti che hanno un punteggio definito.
        :param punteggio: Numero intero che rappresenta il punteggio
        :param lode: Booleano che indica la presenza di lode
        :return: Lista di oggetti di tipo Voto che hanno il punteggio
         specificato (può anche essere vuota).
        """
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)

        return corsi

    def findByEsame(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: Nome dell'esame da cercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure None se non viene trovato.
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: Nome dell'esame da cercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure un'eccezione
         ValueError se l'elemento non viene trovato.
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")

    def has_voto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome e lo stesso punteggio
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if (
                v.esame == voto.esame
                and v.punteggio == voto.punteggio
                and v.lode == voto.lode
            ):
                # Stessa condizione ma scritta in modo diverso
                # if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                return True
        return False

    def has_conflitto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome ma punteggio diverso
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and not (
                v.punteggio == voto.punteggio and v.lode == voto.lode
            ):
                # Stessa condizione ma scritta in modo diverso
                # if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                return True
        return False

    def copy(self):
        nuovo = Libretto()
        # Con .copy() faccio una copia dell'oggetto Libretto ma non ho fatto
        # copie dell'oggetto Voto. Quindi quando nel main chiamo questo metodo,
        # cambiano anche i voti di Libretto, che dovrebbero rimanere invariati.

        # # # nuovo._voti = self._voti.copy()  # or nuovo._voti = self._voti[:]

        # nuovo._voti[0] e self._voti[0] a seguito della copia, sono lo stesso
        # oggetto. Sono due riferimenti, due nomi diversi dello stesso oggetto.
        # Ho creato una nuova lista, che contiene come elementi il contenuto
        # della lista precedente, ovvero i riferimenti.
        # Una lista contiene riferimenti a oggetti Voto. Quando copio la lista
        # copio i riferimenti. nuovo._voti[0] NON è una copia di self._voti[0],
        # ma è lo stesso oggetto. Quindi quando cambio un campo di quell'oggetto,
        # la modifica si vedere nei 2 oggetti. Quindi non devo solo creare
        # un nuovo Libretto, ma devo creare una copia dei voti in modo che
        # questi voti nascano uguali ma siano oggetti indipendenti e quindi
        # possono essere modificati indipendentemente l'uno dall'altro.

        # Le operazioni che posso fare sulla copia che non influenzano la
        # lista originale sono le operazioni che modificano la lista e non
        # le operazioni che modificano gli elementi contenuti nella lista.
        # Le operazioni che modificano la lista sono: aggiungere/cancellare
        # un elemento, sostituire un elemento con un altro...Le operazioni
        # che modificano la lista sono le operazioni che cambiano l'insieme
        # dei valori, ovvero dei riferimenti contenuti nella lista (append,
        # remove, sort, ...).
        # Per rendere indipendenti questi 2 libretti devo creare un Libretto
        # nuovo e nella lista voti non devo fare solo una copia dei riferimenti
        # nuovo._voti = self._voti.copy() ma creare nuovi oggetti voto da
        # mettere dentro. Quindi creo una nuova lista che contiene una copia dei
        # voti.

        # Allora invece di avere solo

        # nuovo._voti = self._voti.copy()

        # e il resto del codice scrivo:

        ### Nuovo codice al posto di nuovo._voti = self._voti.copy()

        # Soluzione 1
        # for v in self._voti:
        #     nuovo._voti.append(Voto(v.esame, v.cfu, v.punteggio, v.lode, v.data))

        # Creo un nuovo Libretto dove il contenuto sono nuovi oggetti il cui
        # contenuto uguale a quello degli oggetti precedenti. Non ho quasi
        # più legame con Libretto di partenza perchè anche
        # Voto(v.esame, ...) copia riferimenti. Creo un nuovo oggetto Voto,
        # nel cui attributo esame copio il riferimento che c'era
        # nell'attributo esame del Voto precedente. La stringa dell'
        # attributo esame è una sola, non la sto copiando ma la condivido.
        # L'operazione copy() è una shallow copy. Qui invece voglio una deep
        # copy.
        # Svantaggio: se ho una nuova proprietà di Voto(), questo costruttore
        # fallisce. Devo passare un parametro in più.
        ### Fine nuovo codice ###

        ### Nuovo codice
        # Soluzione 1
        for v in self._voti:
            nuovo._voti.append(v.copy())
        return nuovo
        # Aggiungo dento Voto() il metodo copy
        ### Fine nuovo codice ###


    def crea_migliorato(self):
        """
        Crea una copia del libretto e migliora i voti in esso presenti.
        :return:
        """
        nuovo = self.copy()

        for v in nuovo._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30

        return nuovo
    def crea_ordinato_per_esame(self):
        # Crea una copia profonda dell'oggetto e ordina quella.
        nuovo = self.copy()

        # ordina nuovo._voti
        nuovo.ordina_per_esame()

        return nuovo




    def ordina_per_esame(self):
        # Modifica l'oggetto.
        # ordina self._voti per nome esame

        # Per poter essere ordinata la lista deve contenere oggetti che implementano
        # il metodo __lt__. Se non voglio ordinare usando lt, usa key (invece di chiamare lt,
        # uso key). L'argomento di key è una funzione che prende l'oggetto Voto che restituisce
        # una stringa (campo esame)

        # # Metodo 1 che non si usa
        # self._voti.sort(key=estrai_campo_esame)
        # # dove estrai_campo_esame metodo da mettere in Voto
        # def estrai_campo_esame(v):
        #     return v.esame

        # Metodo 2 che si usa
        self._voti.sort(key=operator.attrgetter('esame'))

        # Metodo 3: funziona inline. Si usa quando il valore da ordinare, non è l'attributo dell'
        # oggetto: metodo 2
        #self._voti.sort(key=lambda v: v.esame)

        # sort si applica a qualunque lista ma non a tuple perchè sono immutabili.
    def crea_ordinato_per_punteggio(self):
        nuovo = self.copy()
        self._voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True)
        return nuovo

    def stampa(self):
        print(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            print(v)
        print(f"La media vale {self.media()}")

    def cancella_inferiori(self, punteggio):
        # Metodo 1 e 2: sconsigliato perchè non efficiente computazionalmente e modifichi
        # una lista sulla quale iteri.
        # for v in self._voti:
        #     if v.punteggio < punteggio:
        #         self._voti.remove(v)
        #
        # for i in range(len(self._voti)):
        #     if self._voti[i] < punteggio:
        #         self._voti.pop(i)

        # Metodo3
        # voti_nuovi = []
        # for v in self._voti:
        #     if v.punteggio >= punteggio:
        #         voti_nuovi.append(v)
        # self._voti = voti_nuovi

        # oppure
        self._voti = [v for v in self._voti if v.punteggio >= punteggio]





    """
    Opzione 1:
    metodo stampa_per_nome e metodo stampa_per_punteggio, che semplicemente stampano
    e non modificano nulla. Sconsigliato.
    
    Opzione 2:
    metodo crea_libretto_ordinato_per_nome, ed un metodo crea_libretto_ordinato_per_punteggio,
    che creano delle copie separate, sulle quali potrò chiamare il metodo stampa().
    Qui non tocco il Libretto() originale e ordino la copia. Creo oggetti che occupano spazio.
    
    Opzione 3:
    metodo ordina_per_nome, che modifica il libretto stesso riordinando i Voti,
    e ordina_per_punteggio, poi userò stampa(). Modifico il libretto attuale.
    Allora aggiungo metodo copy. E' piu versatile.
    
    Opzione 2bis:
    creo una copia shallow del libretto
    """


def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, "2024-03-11")
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())


if __name__ == "__main__":
    _test_voto()
