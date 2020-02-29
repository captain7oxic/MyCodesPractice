def forgone():
    n = input()
    A, B = [], []
    for num in n:
        if num == '4':
            A.append('2')
            B.append('2')
        else:
            A.append(num)
            if B: B.append('0')
    return "{}{}".format("".join(A),"".join (B))


