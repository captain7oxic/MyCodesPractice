"""Inthischallenge, theuserentersastring
and asubstring.Youhavetoprintthenumber
of times that the substring occurs in thegivenstring.
String traversal will take place from left to right,
not from right to left."""


def count_substring(string, sub_string):
    count = sum([1 for i in range(len(string))
                 if string[i:i+len(sub_string)] == sub_string])

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
