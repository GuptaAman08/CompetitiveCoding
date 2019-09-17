from collections import Counter
from itertools import accumulate
import numpy as np

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
c = Counter(a)


dis_ele = c.keys()
dis_ele_count = len(dis_ele)


ans = n + 1
arr = np.zeros((dis_ele_count, k+1))

arr[:, 0] = list(dis_ele)
arr[:, 1] = list(accumulate(c.values()))


for i in range(2, k+1):
    for j in range(i-1, dis_ele_count):
        arr[j][i] = arr[j-1][i-1] * c[arr[j][0]] + arr[j-1][i]
    ans += arr[j][i]

print(int(ans) % 1000000007)