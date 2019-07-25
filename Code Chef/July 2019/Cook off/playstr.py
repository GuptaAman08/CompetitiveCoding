from collections import Counter
t = int(input())

while t != 0:
    n = int(input())

    s = input()
    r = input()

    c1 = Counter(s)
    c2 = Counter(r)

    if (c1['1'] == c2['1']):
        print('YES')
    else:
        print('NO')
    t -= 1