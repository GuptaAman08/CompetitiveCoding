import numpy as np
t = int(input())

while t != 0:
    n = int(input())
    m = []

    for i in range(n):
        m.append(list(map(int, input().split())))

    m = np.array(m)
    f = True

    for i in range(n):
        if 0 not in m[i,:]:
            f = False
            break

    if f == False:
        print('NO')
    else:
        for i in range(n):
            if 0 not in m[:, i]:
                f = False
                break
        if f == False:
            print('NO')
        else:
            print('YES')
    
    t -= 1