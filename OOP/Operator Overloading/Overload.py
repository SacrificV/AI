class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(1.5, 2.0)
c2 = ComplexNumber(3.0, 4.5)

c3 = c1 + c2
print(c3)
