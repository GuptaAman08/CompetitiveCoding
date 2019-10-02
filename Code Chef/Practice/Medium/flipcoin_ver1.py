import numpy as np
from sys import stdin

n, q = [int(x) for x in stdin.readline().split()]
arr = np.zeros(n, dtype=np.bool)

while q:
    typ, a, b = [int(x) for x in stdin.readline().split()]  

    if typ == 0:
        arr[a:b+1] = ~arr[a:b+1]
    else:
        print(arr[a:b+1].sum())
    q -= 1