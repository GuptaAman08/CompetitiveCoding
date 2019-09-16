from collections import OrderedDict
import math

t = int(input())

def binomialCoefficient(n, k): 

    if(k > n - k): 
        k = n - k 

    res = 1
    
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res 

while t:  
  
    n , k = [int(x) for x in input().split()] 
    arr = [int(x) for x in input().split()] 

    arr.sort()
    d = OrderedDict.fromkeys(arr[:k], 0)
    for i in range(k):
        d[arr[i]] += 1
    
    temp = arr.count(arr[k-1])
    if d[arr[k-1]] < temp:
        d[arr[k-1]] = temp

    count = 0
    ke = 0
    for key, val in d.items():
        count += val
        ke, v = key, val
    count -= d[ke]
    space = k - count
    ans = binomialCoefficient(d[ke], space)
    print(int(ans))

    
    t -= 1
