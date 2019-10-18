from sys import stdin
import math
from collections import defaultdict

# another approach

def cal_mul(n, i):
    sqrt_n = int(math.sqrt(n))+1
    for j in range(1, sqrt_n):
        if n%j == 0:
            other_mul = n//j
            if d[other_mul] > i+1:
                c[other_mul] += 1
            if d[j] > i+1 and other_mul != j:
                c[j] += 1

t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]

    d = defaultdict(int)
    c = defaultdict(int)
    for i in range(n):
        d[a[i]] = i+1

    
    for i in range(n):
        cal_mul(a[i], i)
        # print(c)

    if c.values():
        print(max(c.values()))
    else:
        print(0)
    t -= 1