# Link: https://www.codechef.com/FLPAST01/problems/POLMUL

# cook your dish here
from sys import stdin


t = int(stdin.readline())

while t:
    n, m = [int(x) for x in stdin.readline().split()]
    p = [int(x) for x in stdin.readline().split()]
    q = [int(x) for x in stdin.readline().split()]
    
    ans = [0] * (n+m-1)
    
    for i in range(n):
        for j in range(m):
            ans[i+j] += p[i]*q[j]
            
    print(*ans)
        
    t -= 1