import sys
from random import*
u='a'
while u=='a':
    print('guess a number between 20')
    secret=randint(1,20)
    for num in range(1,7):
        number=input()
        if int(number)>secret:
            print("guess too high")
        elif int(number)<secret:
            print('guess too low')
        else:
            break
    if(int(number)==secret):
        print('correct guess!! you took '+str(num)+'guesses .')
        print("do you want to continue: [y/n]")
        y=input()
        if y=='n':
            sys.exit()
        
    else:
        print('WASTED!! the number i guessed was '+str(secret))
        print("do you want to continue: [y/n]")
        y=input()
        if y=='n':
            sys.exit()
    


