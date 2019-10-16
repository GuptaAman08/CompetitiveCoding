from sys import stdin

t = int(stdin.readline())

while t:
    n, m, q = [int(x) for x in stdin.readline().split()]

    r = [0]*n
    c = [0]*m
    while q:
        x, y = [int(x) for x in stdin.readline().split()]
        r[x-1] += 1
        c[y-1] += 1        
        q -= 1

    od_r, od_c, ev_r, ev_c = 0, 0, 0, 0
    for i in range(n):
        if r[i] % 2 == 0:
            ev_r += 1
        else:
            od_r += 1    
    
    for i in range(m):
        if c[i] % 2 == 0:
            ev_c += 1
        else:
            od_c += 1

    ans = od_r * ev_c + ev_r * od_c
    print(ans)
    t -= 1