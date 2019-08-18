# This approach has a constant time complexity 
import math

def nearestPow2(n):
    res = int(math.log(n, 2))
    return pow(2, res)

n = int(input())
res = nearestPow2(n)
print(res)