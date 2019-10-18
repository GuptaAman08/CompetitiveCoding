t = int(input())

while t:
    n, k = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    div = k//n
    rem = k % n

    num = div % 3
    if num == 0:
        pass
    elif num == 1:
        for i in range(n):
            a = A[i%n]
            b = A[n-(i%n)-1]
            A[i%n] = a ^ b
    else:
        for i in range(n):
            a = A[i%n]
            b = A[n-(i%n)-1]
            A[i%n] = a ^ b
        
        for i in range(n):
            a = A[i%n]
            b = A[n-(i%n)-1]
            A[i%n] = a ^ b
    
    if k > n//2 and n%2 != 0:
            A[n//2] = 0

    if rem != 0:
        for i in range(rem):
            a = A[i%n]
            b = A[n-(i%n)-1]
            A[i%n] = a ^ b
    print(*A)
    t -= 1