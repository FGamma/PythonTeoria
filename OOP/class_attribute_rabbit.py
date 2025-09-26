class Rabbit:
    # Attributo di classe definito fuori __init__
    tag = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.rid = Rabbit.tag
        Rabbit.tag +=1

    def __str__(self):
        return (f"Il coniglio di nome {self.name} ha il tag univoco"
                f" {self.rid}")

# Ogni volta che creo una nuova instanza, il tag aumenta il suo valore
con_1 = Rabbit("Rabbit1",2)
con_2 = Rabbit("Rabbit2",1)
con_3 = Rabbit("Rabbit3",3)

print(con_1)
print(con_2)
print(con_3)