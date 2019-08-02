test = int(input())

while test:

    n = int(input())
    arr = [int(x) for x in input().split()]
    
    dynamic_p = [0] * (n+1)
    dynamic_p[1] = arr[0]
    for i in range(2, n+1):
        # Two comma sepearated cases 
        # 1-> swap
        # 2-> Not swap
        dynamic_p[i] = max(dynamic_p[i-2]+i*arr[i-2]+(i-1)*arr[i-1], dynamic_p[i-1] + arr[i-1]*i)
    test -= 1
    print(dynamic_p[n])