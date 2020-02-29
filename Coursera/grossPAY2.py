#we will make this new program with help of functions
#question-Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#  Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#  Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

def computepay(h,r,h1,r1):
    c=0
    if h<40:
    	grspay=h*r
    	print(grspay)
    elif h>40:
    	grspay=40*r
    	for i in range (40,h1):
        	c=c+1
    pay69=c*r1
    totalpay=grspay+pay69
    return totalpay
#eof
hrs = input("Enter Hours:")
h = float(hrs)
h1= int(hrs)
rate = input("enter rate:")
r = float(rate)
r1=r*1.5
p = computepay(h,r,h1,r1)
print("Amount Total Paid ",p)



