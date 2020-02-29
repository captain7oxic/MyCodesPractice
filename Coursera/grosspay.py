c=0
hrs = input("Enter Hours:")
h = float(hrs)
h1=int(hrs)
rate = input("enter rate")
r = float(rate)
rate1=r*1.5
r1=float(rate1)
if hrs<40:
    grspay=hrs*r
    print(grspay)
elif hrs>40:
    grspay=40*r
    for i in range (40,h1):
        c=c+1
    pay=c*r1
    totalpay=grspay+pay
    
print(totalpay)
    