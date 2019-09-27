# till subtask two
t = int(input())

while t:
    a, b, c = [int(x) for x in input().split()]
    
    c -= 1
    mod = 1000000007
    res = 0
    temp = 0
    for i in range(1, b+1):
        temp = i*i
        for j in range(1, i+1):
            res = (res%mod + max(0, c - (temp//j))%mod)%mod

    print(res)
    t -= 1