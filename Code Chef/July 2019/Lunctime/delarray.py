test = int(input())

while test:
    n = int(input())
    arr = [int(x) for x in input().split()]

    count = 0
    for i in range(n):
        for j in range(i, n):
            temp = float('-inf')
            var = 0
            a = []
            for k in range(n):
                if k<i or k>j:
                    if arr[k] > temp:
                        var += 1
                        temp = arr[k]
            if var != 0:
                if var == (n-(j-i+1)):
                    count += 1
            
    print(count)
    test -= 1