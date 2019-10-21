from sys import stdin
from collections import defaultdict

n, m = [int(x) for x in stdin.readline().split()]

a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]

dis_sp = defaultdict(int)
c = n

if n > m:
    temp = b[0]
    for i in range(n):
        print(i, 0)
        dis_sp[temp+a[i]] = 1

    f = 0
    for i in range(1, m):
        for j in range(n):
            if dis_sp[b[i] + a[j]] == 0:
                print(j, i)
                dis_sp[b[i] + a[j]] = 1
                c += 1
            
            if c == (n+m-1):
                f = 1
                break
        
        if f == 1:
            break

    
else:
    temp = a[0]
    for i in range(m):
        print(0, i)
        dis_sp[temp+b[i]] = 1
        

    f = 0
    for i in range(1, n):
        for j in range(m):
            if dis_sp[a[i] + b[j]] == 0:
                print(i, j)
                dis_sp[a[i]+b[j]] = 1
                c += 1
            
            if c == (n+m-1):
                f = 1
                break
        
        if f == 1:
            break

    