test = int(input())

while test:
    n = int(input())
    arr = [int(x) for x in input().split()]

    if n == 1:
        ans = arr[0]
    elif n == 2:
        t1 = arr[0] + arr[1] * 2
        t2 = arr[0] * 2 + arr[1]
        if t1 > t2:
            ans = t1
        else:
            ans = t2
    else:
        ans = 0
        t = []
        proxy_arr = [1] * n
        for i in range(n-1):
            ans += arr[i]*(i+1)
            t.append(arr[i] - arr[i+1])

        ans += arr[n-1] * (n)
        
        incl = t[0]
        excl = 0

        for i in range(1, n-1):
            new_excl = max(incl, excl)
            incl = excl + t[i]
            excl = new_excl
                    
        if incl > excl:
            ans += incl
        else:
            ans += excl
        
    test -= 1
    print(ans)

