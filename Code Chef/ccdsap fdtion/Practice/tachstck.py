# Link: https://www.codechef.com/problems/TACHSTCK

from sys import stdin

n, d = [int(x) for x in stdin.readline().split()]
a = []

for i in range(n):
    a.append(int(stdin.readline()))
    
a.sort()

ans = 0
i = 0

while i<n-1: 
    if a[i+1]-a[i] <= d:
        ans += 1
        i += 2
    else:
        i += 1
        
print(ans)
        

