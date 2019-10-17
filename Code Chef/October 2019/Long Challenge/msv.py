import math
from sys import stdin


def cal_multiples(n):
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(1, sqrt_n):
        if n % i == 0:
            d[i] += 1
            temp = n//i
            if temp != i:
                d[temp] += 1


t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]

    d = [0]*((10**6)+1)

    max_c = 0
    for i in range(1, n):
        cal_multiples(a[i-1])
        if d[a[i]] > max_c:
            max_c = d[a[i]]

    print(max_c)

    t -= 1
