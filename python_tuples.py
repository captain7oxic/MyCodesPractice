
# --------------------------------------------------------------------------------

#Program 1
tup1=('Eleven','Twelve','Thirteen')
print('Before adding',tup1)
list1=list(tup1)
list1.append('Fourteen')
tup1=tuple(list1)
print('After append',tup1)

# --------------------------------------------------------------------------------


#Program 2
tup1 = ('Y','u','v','r','a','j')
lst = list(tup1)
string=''.join(lst)
print(string)


# --------------------------------------------------------------------------------


#Program 3
tup = ('H','i')
tup1 = tup
print(tup1)


# --------------------------------------------------------------------------------

#Program 4
tup1 = (2,3,4,5,6,7)
lst = list(tup1)
ele = int(input("Enter the value you want to remove : "))
if ele in lst:
    lst.remove(ele)
tup1 = tuple(lst)
print(tup1)


# --------------------------------------------------------------------------------



#Program 5
tup1=('Yuvraj',19567,'CS')
(name,roll,stream)=tuple1
print(name,'\n',roll,'\n',stream)

# --------------------------------------------------------------------------------

#Program 6
tuple1=('H','i',' ','I','m',' ','Y','u','v','r','a','j')
x1 = tuple1[3]
print(x1)
x2 = tuple1[-4]
print(x2)
