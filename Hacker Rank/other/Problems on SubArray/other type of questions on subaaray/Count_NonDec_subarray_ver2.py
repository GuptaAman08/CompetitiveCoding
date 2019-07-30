# O(n) approach

t = int(input())

while t != 0:

    n = int(input())
    a = list(map(int, input().split()))

    cur_ele = a[0]
    count = 1
    track = 0
    for i in range(1,n):
        if a[i] >= cur_ele:
            count += (i-track+1)
        else:
            track = i
            count += 1
        cur_ele = a[i]
    
    print(count)
        


    # print(count)
    t -= 1
