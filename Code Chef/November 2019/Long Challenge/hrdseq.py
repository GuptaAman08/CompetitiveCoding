from sys import stdin
from collections import defaultdict

t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        a = [0, 0]

        count = defaultdict(int)
        count[0] += 1

        # track last occurence
        tlo = defaultdict(int)
        tlo[0] = 1

        for i in range(1, n):
            ele = a[i]
            
            if tlo[ele] == 0:
                a.append(0)
                tlo[ele] = i+1
                count[ele] += 1
            else:
                temp = i+1 - tlo[ele]
                a.append(temp)
                count[ele] += 1
                tlo[ele] = i+1
        
        print(count[a[n-1]])
    t -= 1