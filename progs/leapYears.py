#%%
print(*range(1, 10, 2))
#%%
for var in range(0, 10):
    if var % 2 == 0:
        continue
    print(var)

# %%
c = 1
while c <= 10:
    print(f" hello world times {c}")
    c = c + 1
    


# %%
import math
start = int(input())
end = int(input())
if start == 1:
    start += 1
elif i < 1:
    print("invalid output")
else:
    for number in range(start, end):
        for check in range(2, math.ceil(math.sqrt(number) + 1)):
            if number == 2:
                print(number, end=', ')
                Counter = Counter +1
            elif number % check == 0:
                break
            else:
                print(f"prime number {number}")
                Count = Count + 1

 


# %%
