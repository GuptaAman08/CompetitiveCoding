t = int(input())

while t:
    n, m = [int(x) for x in input().split()]

    food = [int(x) for x in input().split()]

    cat = [0] * (n)

    j = 1
    flag = True
    for i in range(1, m+1):
        cat[food[i-1]] += 1

        if cat[food[i-1]] > j:
            flag = False
            break

        if (i % n) == 0:
            j += 1

    if flag:
        print('YES')
    else:
        print('NO')
    
    t -= 1
