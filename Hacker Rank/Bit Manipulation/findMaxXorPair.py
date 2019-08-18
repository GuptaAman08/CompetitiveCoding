# Finding maximum XOR pair in a given range of Integer
# refer link:  https://www.geeksforgeeks.org/maximum-xor-value-of-a-pair-from-a-range/

l = int(input())
r = int(input())

if l == r:
    print(0)
else:
    xor = l ^ r
    bin_xor = bin(xor)
    ch = bin_xor[2]
    track = 2
    while ch == '0':
        track += 1
        ch = bin_xor[track]
    
    if track == (len(bin_xor) - 1):
        print(1)
    else:
        t_str = '1'
        for i in range(track+1, len(bin_xor)):
            t_str += '1'

        print(int(t_str, 2))



