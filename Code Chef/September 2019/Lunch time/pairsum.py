t = int(input())

while t:
    n, Q = [int(x) for x in input().split()]
    
    b = [int(x) for x in input().split()]

    while Q:
        p, q = [int(x) for x in input().split()]
        if abs(p-q) % 2 == 0:
            print('UNKNOWN')
        else:
            min_ = min(p, q)
            max_ = max(p, q)
            c = 0
            ans = b[min_ - 1]
            for i in range(min_, max_ - 1):
                if c % 2 == 0:
                    ans -= b[i]
                else:
                    ans += b[i]
                c += 1
            print(ans)
        Q -= 1
    
    t -= 1