#7.2 Write a program that prompts for a file name,
#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and 
#compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
#when you are testing below enter mbox-short.txt as the file name.
#______________________________________________________________________#

hand=input('Enter the file name : ')
fhand=open(hand)
count=0
num=0
tot=0
for lines in fhand:
    if lines.startswith("X-DSPAM-Confidence:"): continue
    count=count+1
    num=float(lines[21:])
    tot=tot+num
avg=tot/count
print("Average spam confidence:",avg)



