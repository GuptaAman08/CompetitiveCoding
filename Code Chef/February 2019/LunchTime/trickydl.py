t = int(input())

while t:
    a = int(input())

    prev = float('-inf')
    cur = a - 1
    p = 1
    i = 2
    while cur > prev:
        prev = cur
        p += pow(2, i-1) 
        cur = abs(a * i - p)
        i += 1

    d2 = i-2

    cur = a - 1
    p = 1
    i = 2
    while cur > 0:
        p += pow(2, i-1)
        cur = a * i - p
        i += 1

    d1 = i-2
    print(d1, d2)
     
    t -= 1