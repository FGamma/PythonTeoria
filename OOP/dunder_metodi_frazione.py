class Fraction:
    def __init__(self, num, denom):
        assert isinstance(num, int) and isinstance(denom, int) and denom != 0, (
            "Il numeratore e il denominatore devono essere numeri interi. "
            "Il denominatore deve essere diverso da 0."
        )
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(num={self.num},"
            f" " f"denom={self.denom})"
        )

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)


a = Fraction(1, 4)
print(a)
print(a.__repr__())
b = Fraction(3, 4)
c = a + b
print(c)
