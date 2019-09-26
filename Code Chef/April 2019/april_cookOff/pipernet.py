# https://www.codechef.com/problems/PEWDSVTS
import math
import heapq


t = int(input())

while t:
    n, a, b, x, y, z = [int(x) for x in input().split()]
    c = [-int(x) for x in input().split()]

    hooli = math.ceil((z-b)/y)
    
    heapq.heapify(c)

    count = 0
    temp_sum = a + (hooli-1)*x
    
    while temp_sum < z and c[0] != 0:
        temp = heapq.heappop(c)
        temp_sum += -1 * temp
        heapq.heappush(c, math.ceil(temp/2))
        count += 1
    
    
    if temp_sum < z:
        print('RIP')
    else:
        print(count)
    
    t -= 1
