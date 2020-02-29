class xyz:

    def __init__(self):
        self.l = [1, 2, 3, 4, 5, 5, 6, 67, "kmcek"]

    def __getitem__(self, i):
        print("List : ", i)
        if isinstance(i, int):
            return self.l[i]
        else:
            print(i.start, i.stop, i.step)
            return self.l[i]


obj = xyz()
print(obj[0])
print(obj[-2:])
print(obj[1:4:6])

print("kmcek" in obj)
print("jncj" in obj)

#


def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
#

#


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    list3 = []
    for element in list1:
        list3 = [element] + list3
    return list2+list3


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#


def squares(start, end):
    return [x*x for x in range(start, end+1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#


def car_listing(car_prices):
    result = ""
    for keys, value in car_prices.items():
        result += "{} costs {} dollars".format(keys, value) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
                   "Ford Fiesta": 13000, "Toyota Prius": 24000}))
#
