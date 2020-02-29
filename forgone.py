for TestCase in range(int(input())):
    num = input()
    A = num
    B = "".join('2' if d == '4' else '0' for d in num).lstrip('0')
    A = A.replace('4', '2')
    print("Test CASE #{}: {}  {}".format(TestCase+1,A,B))