# def square_numbers(nums):
#   for i in nums:
#      yield (i * i)

my_nums = (x*x for x in [1, 2, 3, 4, 5])


for num in my_nums:
    print(num)

print(type(my_nums))
