# Finding maximum XOR pair in a given range of Integer
# refer link:  https://www.geeksforgeeks.org/maximum-xor-value-of-a-pair-from-a-range/
from sys import stdin

t = int(stdin.readline())

while t:
    l, r = [int(x) for x in stdin.readline().split()]
    
    if l == r:
        print(r)
    else:
        bin_l = f'{l:064b}'
        bin_r = f'{r:064b}'

        i = 0
        max_val = ''
        while bin_l[i] == bin_r[i]:
            max_val += bin_l[i]
            i += 1
        
        temp = 64 - i
        for i in range(temp):
            max_val += '1'

        print(int(max_val, 2))
    t -= 1


