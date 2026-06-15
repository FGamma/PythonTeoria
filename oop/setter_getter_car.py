class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12

    # Getter
    @property
    def voltage(self):
        return self._voltage

    # Setter
    # Se non definisco il Setter, l'attributo voltage è read-only
    @voltage.setter
    def voltage(self, volt):
        print("Warning!")
        self._voltage = volt

my_car = Car("red", "Ford", 2010)
print(my_car.voltage)
my_car.voltage = 24
print(my_car.voltage)









