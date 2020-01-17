# cook your dish here
from sys import stdin
from bisect import bisect_left
from collections import deque

t = int(stdin.readline().strip())

while t:
    n = int(stdin.readline().strip())
    s = [int(x) for x in stdin.readline().split()]
    
    
    i=n-1
    temp = deque([s[-1]])
    while (i > 0) and s[i-1]>=s[i]:
        i -= 1
        temp.append(s[i])
        
    if i == 0:
        print(''.join([str(x) for x in s]))
        print('NO NXTBIG')
    else:
        ind = bisect_left(temp, s[i-1])
        if temp[ind] == s[i-1]:
            tmp = temp[ind + temp.count(temp[ind])] 
            temp[ind + temp.count(temp[ind])] = s[i-1]
            temp.appendleft(tmp)
        else:
            tmp = temp[ind]
            temp[ind] = s[i-1]
            temp.appendleft(tmp)
        
        for j in range(i-2, -1, -1):
            temp.appendleft(s[j])
        
        print(''.join([str(x) for x in s]))
        print(''.join([str(x) for x in temp]))    
        
    t -= 1