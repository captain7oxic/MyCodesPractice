def snail(snail_map):
    lis = []
    col_beg = 0
    col_end = len(snail_map[0])-1
    row_beg = 0
    row_end = len(snail_map)-1

    while row_beg <= row_end and col_beg <= col_end:

        for i in range(col_beg, col_end+1):
            lis.append(snail_map[row_beg][i])
        row_beg += 1

        for i in range(row_beg, row_end+1):
            lis.append(snail_map[i][col_end])
        col_end -= 1

        if row_beg < row_end:
            for i in range(col_end, col_beg-1, -1):
                lis.append(snail_map[row_end][i])
            row_end -= 1

        if col_beg < col_end:
            for i in range(row_end, row_beg-1, -1):
                lis.append(snail_map[i][col_beg])
            col_beg += 1

    return lis


def snail2(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(snail(array))
print(snail2(array))
