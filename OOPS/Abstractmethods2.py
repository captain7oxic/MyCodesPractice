from abc import ABC, abstractclassmethod


class A:
    @abstractclassmethod
    def __init__(self):
        print('Init of class a')


class B(A):
    def __init__(self):
        super().__init__()
        print('Init of class B')


B()
