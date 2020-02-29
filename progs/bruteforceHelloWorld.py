import random
import sys
import time


target_array=["H",'e',"l",'l','o'," ","W","o","r","l","d" ]
string_array=["","","","","","","","","","",""]

i=0
count=0
while i<len(target_array):
    if string_array[i]!=target_array[i]:
        string_array[i] = chr(random.randint(0,256))


    if string_array[i] == target_array[i]:
        i=i+1



        x=0
        print("\n")
        while x<len(string_array):
            print(string_array[x] , end = "" , flush = True)
            x+=1
            count +=1
        time.sleep(0.01)


print(" Total guesses is : ", count)
    
