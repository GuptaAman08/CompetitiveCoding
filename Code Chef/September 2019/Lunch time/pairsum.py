t = int(input())

while t:
    N, Q = [int(x) for x in input().split()]
    
    b = [int(x) for x in input().split()]

    n = [b[0]]
    c = -1
    for i in range(1, N-1):
        n.append(n[i-1] + c*b[i])
        c *= -1
    
    while Q:
        p, q = [int(x) for x in input().split()]
        if abs(p-q) % 2 == 0:
            print('UNKNOWN')
        else:
            min_ = min(p, q)
            max_ = max(p, q)
            if min_ == 1:
                print(n[max_ - 2])
            elif ((min_ % 2) == 0):
                print(n[min_ - 2] - n[max_ - 2])
            else:
                print(n[max_ - 2] - n[min_ - 2])
        Q -= 1
    
    t -= 1