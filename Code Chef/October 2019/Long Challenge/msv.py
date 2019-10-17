from sys import stdin
import math

t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]
    d = defaultdict(int)
    
    max_c = 0
    for i in range(1, n):
        sqrt_n = int(math.sqrt(a[i-1]))+1
        for j in range(1, sqrt_n):
            if a[i-1] % j == 0:
                d[j] += 1
                temp = a[i-1]//j
                if temp != j:
                    d[temp] += 1
        
        if d[a[i]] > max_c:
            max_c = d[a[i]]
        
    
    print(max_c)
    
    t -= 1