t = int(input())


while t != 0:
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    if N == 1:
        print(max(A[0], B[0]))
    else:
        sum_b = sum(B)
        temp = []
        var_a = A[0]
        temp.append(sum_b)
        sum_b -= B[0]
        for i in range(1,len(A)):
            temp.append(var_a + sum_b)
            var_a += A[i]
            sum_b -= B[i]
        
        temp.append(var_a)
        print(max(temp))
    t -= 1
    
