from sys import stdin

t = int(stdin.readline())

while t:

    n = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]

    min_i = 0
    max_i = 0

    min_val = a[0]
    max_val = a[0]

    for i in range(n):
        if min_val > a[i]:
            min_val = a[i]
            min_i = i

        if max_val < a[i]:
            max_val = a[i]
            max_i = i

    if min_i > max_i:
        print(max_val, min_val)
    else:
        print(min_val, max_val)
    t -= 1