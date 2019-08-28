t = int(input())

while t:
    n = int(input())

    neg_len = 0
    pos_len = 0
    for i in input().split():
        x = int(i)
        if x < 0:
            neg_len += 1
        else:
            pos_len += 1

    if (pos_len == n) or (neg_len == n):
        print(n, n)
    elif (pos_len == 0) and (neg_len == 0):
        print(0, 0)
    else:
        print( max(pos_len, neg_len), min(pos_len, neg_len))
        
    t -= 1
