def tickets(people):
    cashier = {100: 0, 50: 0, 25: 0}
    for cash in people:
        if cash == 25:
            cashier[25] += 1

        elif cash == 50:
            if cashier[25] == 0:
                return "NO"
            else:
                cashier[50] += 1
                cashier[25] -= 1

        else:
            if cashier[50] >= 1 and cashier[25] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            elif cashier[25] >= 3:
                cashier[25] -= 3
            else:
                return "NO"

    return "YES"
