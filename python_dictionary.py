''' Write a Python program to multiply all the items in a dictionary.'''
dict={1:10,2:20,3:30}
product = 1
for x in dict.values():
    product *= x
print(product)


''' Write a Python program to remove a key from a dictionary.'''
dict={0:10,1:20,2:30,3:40}
dict.pop(2)
print(dict)

''' Write a Python script to sort (ascending and descending) a dictionary by
value.'''
dict={10:"Dell",2:"HP",34:"ACER",4:"ASUS"}
for i in sorted(dict.keys()):
    print(i)

''' Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''
dict= {0:10,1:20,2:30}
dict[3]=40;
print(dict);

''' Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dictres={*dict1,dict2,*dict3}
print(dictres)

''' Write a Python script to check whether a given key already exists in a
dictionary.'''
dict1={0:10,1:20,2:30,3:40}
if(dict1.get(2,0)):
    print("2 is one of the keys")
else:
    print("2 is not one of the keys")


''' Write a Python program to iterate over dictionaries using for loops.'''
dict={1:10,2:20,3:30,4:40}
for x in dict:
    print(x,dict[x]);

''' Write a Python script to generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
dict={x:x*x for x in range(1,6)}
print(dict)

''' Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,
13: 169, 14: 196, 15: 225}'''
dict={x:x*x for x in range (1,16)}
print(dict)

''' Write a Python program to sum all the items in a dictionary.'''
dict={1:10,2:20,3:30}
print(sum(dict.values()))



''' Write a Python program to remove a key from a dictionary.'''
dict={0:10,1:20,2:30,3:40}
dict.pop(2)
print(dict)
