class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i 

    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(3, 2)
c2 = Complex(1, 7)

result = c1 * c2
print(result)  
