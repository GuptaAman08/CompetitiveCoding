t = int(input())

while t:
    n, c, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    pre_a_sum = []
    pre_a_sum.append(a[0])

    for i in range(1, n):
        pre_a_sum.append(pre_a_sum[i-1] + a[i])

    f = 0
    for i in range(n):
        s, e, ans = i, n-1, i-1
        sc = 0
        if i != 0:
            sc = pre_a_sum[i-1]

        while s<=e:
            mid = (s+e) // 2
            cost = pre_a_sum[mid] - sc

            if cost >= k and cost <= c:
                s = mid + 1
                ans = mid
            elif cost < k:
                s = mid + 1
            else:
                e = mid - 1

        ans = ans - i + 1
        f = max(ans, f)

    print(f)

    t -= 1