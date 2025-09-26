class Coniglio:
    # Attributo di classe definito fuori __init__
    tag = 1
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        self.rid = Coniglio.tag
        Coniglio.tag +=1

    def __str__(self):
        return (f"Il coniglio di nome {self.nome} ha il tag univoco"
                f" {self.rid}")

# Ogni volta che creo una nuova instanza, il tag aumenta il suo valore
con_1 = Coniglio("Tim",2)
con_2 = Coniglio("Tom",1)
con_3 = Coniglio("Tam",3)

print(con_1)
print(con_2)
print(con_3)