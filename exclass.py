l = [(3, 5), (4, 6), (7, 2), (5, 9), (8, -1)]

l = l.sort()
print(l)

b = l.sort(key=lambda x: x[1])
print(b)
