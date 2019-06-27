t = int(input())

while t != 0:
    n = int(input())
    if n == 1:
        print(1)
    else:
        prev = 1
        for i in range(2,n+1):
            temp = prev + i + prev * i 
            prev = temp
        print(prev)
    t -= 1