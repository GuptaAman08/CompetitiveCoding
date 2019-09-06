t = int(input())

while t:
    n, k, v = list(map(int, input().split()))
    a = sum(list(map(int, input().split())))

    ans = (v * (n+k) - a) / k

    if ans > 0 and ((ans % 1) == 0):
        print(int(ans))
    else:
        print(-1)
    
    t -= 1