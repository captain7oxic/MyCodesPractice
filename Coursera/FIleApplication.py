#7.1 Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#and print the contents of the file in upper case. 
#---------------------------------------------------------#

hand=input("Enter the file name :  ")
try:
    fhand=open(hand)
except:
    print('file not found' , hand) 
    exit()   
inp=fhand.read()
#inpu=inp.strip()
#print(inpu.upper())








