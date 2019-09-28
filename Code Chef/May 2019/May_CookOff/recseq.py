t = int(input())

while t:

    n = int(input())
    a = [int(x) for x in input().split()]

    init_term = 0
    d = 0
    if (a[1]-a[0]) == (a[2]-a[1]):
        init_term = a[0]
        d = a[1] - a[0]
    elif (a[2]-a[1]) == (a[3]-a[2]):
        d = (a[3]-a[2])
        init_term = a[1] - d
    else:
        init_term = a[0]
        d = (a[3]-a[0])//3

    for i in range(n):
        print(init_term+(i*d), end=' ')
    
    t -= 1