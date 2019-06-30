t = int(input())
while t != 0:
    n = int(input())

    s = input()
    u = input()

    i = 0
    points = 0
    while True:
        if i >= n:
            break

        if s[i] == u[i]:
            points += 1
            i = i + 1
        else:
            if u[i] != 'N':
                i = i + 2
            else:
                i = i + 1
        
    t = t - 1
    print(points)