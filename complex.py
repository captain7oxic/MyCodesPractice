class Complex:

    def __init__(self, r, i):
        self.real = r
        self.img = i

    def __str__(self):
        return "{}+i{}".format(self.real, self.img)

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.img + c2.img)

    def __sub__(self, c2):
        return Complex(self.real - c2.real, self.img - c2.img)

    def __mul__(self, c2):
        return Complex(self.real * c2.real, self.img * c2.img)

    def __truediv__(self, c2):
        return Complex(self.real / c2.real, self.img / c2.img)


a = Complex(10, 20)
b = Complex(20, 40)
c = a + b
d = a / b
e = a * b

print(c, d, e)
