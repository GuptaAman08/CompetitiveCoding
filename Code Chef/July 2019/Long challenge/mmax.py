t = int(input())

while t != 0:
    try:
        n = int(input())
        k = int(input())

        permut = []
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
            a = int(k/n)
            b = k%n
            
            if b > (n-b):
                sum_max = 2 * (n-b)
            elif (b==(n-b)):
                sum_max = (n//2) + ((n//2) - 1)
            else:
                sum_max = 2 * b
        t -= 1
        print(sum_max)
    except Exception as e:
        print(e)
