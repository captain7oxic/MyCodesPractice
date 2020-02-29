class Positive(Exception):
    pass


class Negative(Exception):
    pass


class Zero(Exception):
    pass


def whatsign(x):
    if x > 0:
        raise Positive('Number is positive ')
    elif x < 0:
        raise Negative('Number is negative')
    else:
        raise Zero('Number is zero')


n = print(input("Enter a number :"))

try:
    whatsign(n)
except Positive as e:
    print(e)
except Negative as e:
    print(e)
except Zero as e:
    prnt(e)
