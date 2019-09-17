import math
t = int(input())

while t:
    n, m = list(map(int, input().split())) 

    if (m < (n-1)) or (m > ((n*(n-1))//2 + n)):
        print(-1)
    else:
        if n == 1:
            if m == 0:
                print(0)
            else:
                print(1)
        elif n == 2:
            if m == 2 or m == 3:
                print(2)
            else:
                print(1)
        else:
            if m <= n+1:
                print(2)
            elif (m > n+1) and (m <= (2*n)):
                print(3)
            else:
                ans = 3
                temp = m - 2*n
                if temp % n == 0:
                    ans += 2*(temp//n)
                else:
                    roundtofloor = temp // n
                    remainder = temp % n
                    ans += roundtofloor * 2
                    if remainder <= (n // 2):
                        ans += 1
                    else:
                        ans += 2
                print(ans)
    t -= 1