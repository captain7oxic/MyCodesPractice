def a():
    a = 15000

    def f():

        print(a)

        def g():
            nonlocal a
            print(a)
        return g
    return f


a = 100
h = a()
g = f()
g()
