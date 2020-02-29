import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary - self.imaginary*other.real)

    def __truediv__(self, other):
        # return Complex(self.real // other.real, self.imaginary // other.imaginary)
        pass
    # def mod(self):
        # return Complex(math.mod(self.real), math.mod(self.imaginary))
        # pass

    def __str__(self):
        if self.imaginary == 0:
            result = "{0:.2f}+{0.00}i".format((self.real))
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "{0.00}+{.2fi}".format((self.imaginary))
            else:
                result = "{0.00}-{0:.2fi}".format((abs(self.imaginary)))

        elif self.imaginary > 0:
            result = "{0:.2f}+{0:.2f}i".format((self.real, self.imaginary))
        else:
            result = "{0:.2f}-{0:.2f}i".format(
                (self.real, abs(self.imaginary)))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y]), sep='\n')
