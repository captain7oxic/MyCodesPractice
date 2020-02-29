ddd=dict()
lines=input("enter words:")
words=lines.split()
print('Words:',words)
for word in words:
    ddd[word]=ddd.get(word,0)+1 #countingtrick

print(ddd.items()) #item,keys,values are the contents that can be printed from dictionary