# OOP in Python

Questo progetto mostra diversi concetti di **Programmazione Orientata agli Oggetti (OOP)** in Python attraverso esempi pratici. Ogni cartella/file illustra un caso specifico di utilizzo delle classi, degli attributi e dei metodi.

---

## Casi implementati

### 1. simple_class_libretto
Implementa due classi principali:
- **Voto**: rappresenta un singolo voto con attributi e metodi.
- **Libretto**: rappresenta un insieme di voti.
  
Include:
- Costruttore `__init__`
- Metodi di rappresentazione `__str__` e `__repr__`

---

### 2. private_attribute_libretto
Mostra come definire **attributi privati** in Python usando la convenzione `_nome_attributo`.
- Non sono presenti setter e getter espliciti.
- L’obiettivo è illustrare come gli attributi “privati” siano solo una convenzione.

---

### 3. dataclass_libretto
Dimostra l’uso del decoratore **`@dataclass`** per semplificare la definizione di classi.
- I metodi `__init__`, `__repr__`, `__eq__` vengono generati automaticamente.
- Ideale per classi il cui scopo principale è contenere dati.

---

### 4. class_attribute_coniglio
Confronto tra:
- **Attributi di classe**: condivisi tra tutte le istanze della classe.
- **Attributi di istanza**: specifici di ogni singola istanza.
  
Esempio pratico con una classe `Coniglio`.

---

### 5. setter_getter_car
Implementa l'equivalente di getter e setter in Python usando il costrutto
@property.

---

### 6. dunder_metodi_frazione
Implementa i seguenti metodi dunder:
- **Dunder init**
- **Dunder str**
- **Dunder repr**
- **Dunder add**


---