from sys import stdin
import math

t = int(stdin.readline())

while t:
    n = stdin.readline().strip()
    
    l_n = len(n)
    
    c = 0
    i = l_n-1
    while i >= 0: 
        if n[i] == '0':
            c += 1
        else:
            break
        i -= 1
    
    

    int_n = int(n[:i+1])
    if int_n == 1:
        if c >= 1:
            print('Yes')
        else:
            print('No')
    elif (int_n & (int_n-1)) == 0:
        if int(math.log(int_n ,2)) <= c:
            print('Yes')
        else:
            print('No')
    else:
        print('No')    

    t -= 1