from sys import stdin
from heapq import heapify, heappop, heappush

t = int(stdin.readline())

while t:
    n, m = [int(x) for x in stdin.readline().split()]
    a = [(x, int(y)) for x, y in enumerate(stdin.readline().split())]

    a.sort(key=lambda x: x[1])
    
    seg_all_col = [[] for x in range(m)]

    for i in range(n):
        seg_all_col[a[i][0] % m].append(a[i][1])

    # [a, b] -> a: next element to be picked in a list and b: len of that list
    vis = [[1, len(i)] for i in seg_all_col]

    mn, mx = float('inf'), float('-inf')
    li = []
    for i in range(m):
        mx = max(mx, seg_all_col[i][0])
        li.append([seg_all_col[i][0], i])

    curMinRange = float('inf')
    heapify(li)
    
    temp = []
    while True:
        temp = heappop(li)
        mn = temp[0]

        curMinRange = min(curMinRange, mx-mn)

        if vis[temp[1]][0] == vis[temp[1]][1]:
            break
        else:
            nxt = seg_all_col[temp[1]][vis[temp[1]][0]]
            mx = max(mx, nxt)
            vis[temp[1]][0] += 1

            heappush(li, [nxt, temp[1]])
        
    print(curMinRange)
    t -= 1
