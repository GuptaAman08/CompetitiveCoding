t = int(input()) 

while t != 0:
    n = int(input())

    A_even, A_odd, B_even, B_odd = 0, 0, 0, 0
    A = []
    B = []

    sum_AB = 0
    for x in input().split():
        x = int(x)
        sum_AB += x 
        A.append(x)
        if x % 2 == 0:
            A_even += 1
        else:
            A_odd += 1
        

    for x in input().split():
        x = int(x)
        sum_AB += x
        B.append(x)
        if x % 2 == 0:
            B_even += 1
        else:
            B_odd += 1
        
    ans = int(float(sum_AB/2) - float((n - min(A_even, B_even) - min(A_odd, B_odd))/2)) 
    t -= 1
    print(ans)