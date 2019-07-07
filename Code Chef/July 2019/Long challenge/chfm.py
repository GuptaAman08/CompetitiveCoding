import sys
t = int(input())

while t != 0:
    n = int(input())
    a = list(map(int,input().split()))

    sum_a = sum(a)
    mean_a = sum_a/n

    min_index = sys.maxsize
    for i in range(n):
        temp = sum_a - a[i]
        if (temp/(n-1)) == mean_a:
            min_index = i+1
            break

    if min_index == sys.maxsize:
        print("Impossible")
    else:
        print(min_index)
    
    t -= 1