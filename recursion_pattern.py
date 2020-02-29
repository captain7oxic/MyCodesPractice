def row(n, i):
    if n == 0:
        return

    def column1(n):
        if n == 0:
            return
        column1(n - 1)
        print(n, end=" ")

    def column2(n):
        if n == 0:
            return
        print(n, end=" ")
        column2(n - 1)

    row(n - 1, i + 1)
    print(" " * i, end=" ")
    column1(n)
    column2(n - 1)
    print()


a = int(input())
row(a, 0)
