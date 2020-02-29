from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def f(self):
        print('jsn')

    @abstractclassmethod
    def g(self):
        print('dncenc')

    def h(self):
        print('kjnejfnwnvwjl')


class B(A):
    def f(self):
        print('Hello cBf')


class C(B):
    def g(self):
        print('dvkjnv')


obj = C()
obj.f()
obj.g()
obj.h()
