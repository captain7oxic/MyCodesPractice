class student:
    def __new__(cls, r, n):
        print(type(cls))  # class type arguement passed to __new__ method cls
        return object.__new__(cls)

    def __init__(self, r, n):
        print(type(self))
        self.name = n
        self.roll = r

    def __str__(self):
        return "{} {}".format(self.roll, self.name)


s1 = student(1, "Abhilasha")
print(type(s1))

del s1
