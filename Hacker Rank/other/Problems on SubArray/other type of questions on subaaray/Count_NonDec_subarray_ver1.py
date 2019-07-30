# O(n^2) approach

t = int(input())

while t != 0:

    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        temp = 0
        for j in range(i,n):
            if a[j] >= temp:
                count += 1
                temp = a[j]
            else:
                break
    print(count)
    t -= 1