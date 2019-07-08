t = int(input())

while t != 0:
    n = int(input())
    k = int(input())

    sum_max = 0
    if ((n < k) and (k%n) == 0) or (n==k):
        sum_max = 0
    elif n > k: 
        if k > (n-k):
            sum_max = 2 * (n-k)
        elif k==(n-k):
            sum_max = (n//2) + ((n//2) - 1)
        else:
            sum_max = 2 * k
    else:
        b = k%n
        
        if b > (n-b):
            sum_max = 2 * (n-b)
        elif (b==(n-b)):
            sum_max = (n//2) + ((n//2) - 1)
        else:
            sum_max = 2 * b
    t -= 1
    print(sum_max)
    
