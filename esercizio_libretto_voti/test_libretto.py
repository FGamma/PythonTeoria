from voto import Libretto, Voto

lib = Libretto()

v1 = Voto("Analisi I", 10, 28, False, "2022-01-30")
lib.append(v1)

lib.append(Voto("Fisica I", 10, 25, False, "2022-07-12"))
lib.append(Voto("Analisi II", 8, 30, True, "2023-02-15"))

voti25 = lib.findByPunteggio(25, False)
for v in voti25:
    print(v.esame)

# Gestire esame non trovato
# Metodo 1
voto_analisi2 = lib.findByEsame("Analisi IaI")
if voto_analisi2 is None:
    print("Nessun voto trovato")
else:
    print(f"Hai preso {voto_analisi2.str_punteggio()}")

# Eccezione non gestita dal mio programma chiamante e Python interrompe l'esecuzione.
# Usa try/except
# -> ValueError. Mi obbliga a controllare il return.
# voto_analisi2 = lib.findByEsame2("Analisi IaI")
# Metodo 2
try:
    voto_analisi2 = lib.findByEsame2("Analisi IaI")
    print(f"Hai preso {voto_analisi2.str_punteggio()}")
except ValueError:
    print("Nessun voto trovato")
# Metodo 1 e 2 si comportano allo stesso modo. Quale è meglio? Dipende dai casi.
# Due modi diversi di gestire il caso in cui non si trova: eccezione o valore
# speciale (None)

nuovo1 = Voto("Fisica I", 10, 25, False, "2022-07-13")
nuovo2 = Voto("Fisica II", 10, 25, False, "2022-07-13")

print("1)", lib.has_voto(nuovo1))
print("2)", lib.has_voto(nuovo2))

lib.append(Voto("Analisi 1", 10, 18,False, '2020-01-01'))
lib.append(Voto("Chimica", 8, 30,False, '2020-01-02'))
lib.append(Voto("Informatica", 8, 30,True, '2020-01-03'))
lib.append(Voto("Algebra Lineare", 10, 24,False, '2020-06-01'))
lib.append(Voto("Fisica 1", 10, 21,False, '2020-06-02'))

migliorato = lib.crea_migliorato()

print("Libretto originario")
lib.stampa()
print("Libretto migliorato")
migliorato.stampa()

print("Libretto ordinato")
ordinato = lib.crea_ordinato_per_esame()
ordinato.stampa()

ordinato.cancella_inferiori(24)
print("Libretto senza voti brutti")
ordinato.stampa()
