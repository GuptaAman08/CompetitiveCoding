from sys import stdin
# from string import ascii_lowercase
from collections import defaultdict

t = int(stdin.readline())

while t:
    n = int(stdin.readline())
    s = stdin.readline().strip()

    d = defaultdict(int)

    md = float('inf')
    for i in range(n):
        if d[s[i]] == 0:
            d[s[i]] = i+1
        else:
            md = min(md, i+1 - d[s[i]])
            d[s[i]] = i+1

    if md == float('inf'):
        print(0)
    else:
        print(n-md)

    t -= 1



