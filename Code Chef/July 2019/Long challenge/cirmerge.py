t = int(input())

while t != 0:
    n = int(input())
    a = [int(x) for x in input().split()]

    ans = 0
    if n == 2:
        ans = a[0] + a[1]
    else:
        c = len(a) - 1
        while c != 0:
            min_sum = a[0] + a[1]
            min_i = 0
            l = len(a)
            for i in range(1,l):
                temp = a[i%l] + a[(i+1)%l]
                if min_sum > temp:
                    min_sum = temp
                    min_i = i%l
            
            ans += min_sum
            a[min_i % l] = min_sum
            del a[(min_i+1) % l]
            c = c - 1
    t -= 1
    print(ans)
            