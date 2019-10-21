from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]

a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]


if n > m:
    min_b = b[0]
    min_i = 0
    for i in range(m):
        if min_b > b[i]:
            min_b = b[i]
            min_i = i

    max_a = a[0]
    max_i = 0
    for i in range(n):
        if max_a < a[i]:
            max_a = a[i]
            max_i = i

    for i in range(n):
        print(i, min_i)

    for i in range(m):
        if i != min_i:
            print(max_i, i)    
else:
    min_a = a[0]
    min_i = 0
    for i in range(n):
        if min_a > a[i]:
            min_a = a[i]
            min_i = i

    max_b = b[0]
    max_i = 0
    for i in range(m):
        if max_b < b[i]:
            max_b = b[i]
            max_i = i

    for i in range(m):
        print(min_i, i)

    for i in range(n):
        if i != min_i:
            print(i, max_i)    

    