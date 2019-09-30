import math

t = int(input())

while t:
    l, r, g = [int(x) for x in input().split()]

    if g > r:
        print(0)
    else:
        ans = ((r//g) - (l//g))

        if (l%g == 0):
            ans += 1
        
        if ans != 1:
            print(ans)
        else:
            if l <= g and g <= r:
                print(1)
            else:
                print(0)

    t -= 1