def is_same(x, y):
    return x == y


def check_password(key):
    x = 262010771
    y = key

    if is_same(x, y):
        return print("password match : {}".format(x))
    else:
        return False


check_password(262010771)
