from sys import stdin

t = int(stdin.readline())

while t:
    n = int(stdin.readline())
    edg = []
    count = 0

    for i in range(n-1):
        u, v, b = [int(x) for x in stdin.readline().split()]
        edg.append(b)

    ver = [int(x) for x in stdin.readline().split()]

    ver.sort()
    edg.sort()

    i, j = n-2, n-1
    if edg[i] > ver[j]:
        count += 2
        j -= 2
        i -= 1
    else:
        j -= 1

    while i >= 0:
        if edg[i] > ver[j]:
            count += 1
        
        j -= 1
        i -= 1

    print(count)
    t -= 1