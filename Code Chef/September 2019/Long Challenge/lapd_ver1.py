# This will give you partially solved anwser

t = int(input())

while t:
    a, b, c = [int(x) for x in input().split()]

    mod = 1000000007
    res = 0
    temp = 0
    for i in range(1, b+1):
        temp = pow(i, 2)
        for j in range(1, a+1):
            res = (res%mod + max(0, c - (temp//j))%mod)%mod

    print(res)
    t -= 1