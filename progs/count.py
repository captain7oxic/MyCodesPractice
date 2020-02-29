import pprint
message='jsbdvibvsdncuocnkecnilejcoijcnkl/sencievnrnuebciybvjkec ueniodsdnconeuniu;bi;kjsduvbounvJKnkuvuns'
count={ }
for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1


pprint.pprint(count)
Text=pprint.pformat(count)
print(Text)
