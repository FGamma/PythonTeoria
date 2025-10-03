# Libretto Universitario

**Obiettivo:** utilizzare il pattern **MVC** per organizzare un'applicazione in Flet.

Il programma permette la gestione semplificata dei voti della carriera universitaria.  
Si basa su due classi principali:  

- **Voto**: rappresenta un singolo esame, contenente nome del corso, punteggio ottenuto e data dell’esame.  
- **Libretto**: gestisce un elenco di `Voto` e fornisce un metodo `append()` per l’inserimento degli esami.  

---

## Struttura MVC

### 1. VIEW
Presentazione dell’interfaccia utente:
- Classe `View`, che istanzia i controller definiti da Flet.  
- Interagisce direttamente con il **Controller** per mostrare i dati e ricevere input.  

### 2. CONTROLLER
Reazione alle azioni dell’utente:
- Insieme di **gestori di eventi**.  
- Variabili locali per la gestione dello **stato dell’interfaccia**.  

### 3. MODEL
Gestione dei dati:
- Classe/i che rappresentano i dati.  
- I dati possono essere persistenti su **database**.  
- Nel progetto, il **Model** è la classe `Voto`.  

---
