import queue


class Coda_prioritaria:
    def __init__(self):
        self._lista = []

    def put(self, valore):
        self._lista.append(valore)

    def pop(self):
        """
        Restituisce il valore minimo presente nella lista e lo cancella
        dalla lista stessa.
        :return:
        """
        # remove(): non il metodo migliore perchè già cerco l'elemento minimo
        # nella lista e poi cerco di nuovo lo stesso elemento per poterlo
        # cancellare --> quando trovo il minimo trovo già la posizione del
        # minimo così faccio un pop() della posizione del minimo (più efficace
        # di remove())

        # val_min = min(self._lista)
        # self._lista.remove(val_min)

        # Allora trovo il minimo e la sua posizione-> trasformo la lista
        # in una lista di tuple indice valore --> enumerate
        # [2, 5, 1, 9] enumerate return una lista con lo stesso numero di elementi,
        # dove questi elementi sono tuple fatte dal 1 elemento che è l'indice
        # e il 2 elemento è il valore
        # enumerate restituisce [(0,2),(1,5),(2,1),(3,9)]
        # key=lambda t: t[1] questo invece trova il minimo del 2 elemento delle
        # tuple. Il 1 elemento è l'indice, quindi sarebbe sempre il primo.
        pos_min, val_min = min(enumerate(self._lista), key=lambda t: t[1])
        self._lista.pop(pos_min)
        # min(enumerate(self._lista), key=lambda t: t[1]) e self._lista.pop(pos_min)
        # su strutture dati grandi possono essere faticose.
        return val_min

c = Coda_prioritaria()
c.put(2)
c.put(5)
c.put(1)
print(c.pop())
c.put(3)
print(c.pop())
print(c.pop())
print(c.pop())

# Gestire coda di nomi in modo che le donne passino prima degli uomini:
# uomini: priorità 2
# donne: priorità 1
# Poi a parità del primo elemento vedo il secondo: ordine alfabetico
c = Coda_prioritaria()
c.put((2, "Paolo"))
c.put((1, "Giulia"))
c.put((2, "Antonio"))
print(c.pop())
c.put((1, "Anna"))
print(c.pop())
print(c.pop())
print(c.pop())

# Usa la classe PriorityQueue ma il concetto è simile alla classe implementata
# da noi
c = queue.PriorityQueue()
c.put((2, "Paolo"))
c.put((1, "Giulia"))
c.put((2, "Antonio"))
print(c.get())
c.put((1, "Anna"))
print(c.get())
print(c.get())
print(c.get())