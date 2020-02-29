a = int(input())
reverse = 0
temp = a
while (a != 0):
    remainder = a % 10
    reverse = reverse * 10 + remainder
    a = a // 10

print(reverse)

if (temp == reverse):
    print('palindrome')
    print(reverse)
    print('-'*60)
else:
    print('not Palindrome')
    print(reverse)
