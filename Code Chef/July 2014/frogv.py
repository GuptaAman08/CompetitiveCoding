#  link : https://www.codechef.com/problems/FROGV
from collections import defaultdict
n, k, p = [int(x) for x in input().split()]

i = 1
arr = []
for x in input().split():
    arr.append((int(x), i))
    i += 1

arr.sort()
d = defaultdict(int)

g = 0
prev = arr[0]
d[prev[1]] = g

for ele in arr:
    if (ele[0] - prev[0]) > k:
        g += 1
        
    d[ele[1]] = g
    prev = ele


for i in range(p):
    x1, x2 = [int(x) for x in input().split()]
    if d[x1] == d[x2]:
        print('yes')
    else:
        print('no')
    
