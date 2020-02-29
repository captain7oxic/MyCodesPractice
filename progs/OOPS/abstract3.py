from collections import UserDict

# if you want your object to behave like a dict object


class A(UserDict):
    def __init__(self):
        super().__init__(self)
        self['Roll'] = 1
        self['Name'] = 'Vatsal'


obj = A()
print(obj)
print(type(obj))
