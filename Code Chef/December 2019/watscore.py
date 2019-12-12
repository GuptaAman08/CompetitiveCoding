from sys import stdin


t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    a = [0] * 9
    for _ in range(n):
        p, s = [int(x) for x in stdin.readline().split()]

        if p < 9:
            a[p] = max(a[p], s)

    print(sum(a))

    t -= 1