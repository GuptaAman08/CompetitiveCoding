from sys import stdin
from collections import defaultdict

t = int(stdin.readline())

while t:
    n, m = [int(x) for x in stdin.readline().split()]
    vertices_deg = defaultdict(int)

    adj_1, adj_2 = 0, 0
    for i in range(m):
        u, v = [int(x) for x in stdin.readline().split()]
        vertices_deg[u] += 1
        vertices_deg[v] += 1
        adj_1, adj_2 = u, v

    if m%2 == 0:
        print(1)
        for i in range(n):
            print(1, end=' ')
    else:
        temp = 0
        flag = 0
        for i in range(1, n+1):
            if vertices_deg[i] % 2 != 0:
                temp = i
                flag = 1
                break
        
        if flag == 1:
            print(2)
            for i in range(1, n+1):
                if i == temp:
                    print(2, end=' ')
                else:
                    print(1, end = ' ')
        else:
            print(3)
            for i in range(1, n+1):
                if i == adj_1:
                    print(3, end = ' ')
                elif i == adj_2:
                    print(2, end = ' ')
                else:
                    print(1, end = ' ')
    
    t -= 1