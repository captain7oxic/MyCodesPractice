name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    word = line.split()
    if line.startswith('From '):
        count[word[1]] = count.get(word[1], 0) + 1
largest = 0
email = ''
for k in count:
    if count[k] > largest:
        largest = count[k]
        email = k
print (largest, email)
