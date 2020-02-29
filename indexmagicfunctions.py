class xyz:

    def __init__(self, x):
        self.x = x

    def __index__(self):
        return self.x

    def __add__(self, c2):
        return self.x + c2.x


obj, obj2 = xyz(274380), xyz(38737)
obj = obj+obj2
print(oct(obj))
print(hex(obj))
print(bin(obj))
print(obj)
