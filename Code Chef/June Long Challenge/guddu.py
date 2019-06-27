import math

t = int(input())
while t != 0:
    n = int(input())
    if n < 10:
        ans = str(n) + str(10 - n)
        print(int(ans))
    else:
        n_sum = 0
        temp = n
        while temp > 0:
            n_sum += (temp % 10)
            temp = int(temp / 10)
            
        if (n_sum % 10) == 0:
            print(int(str(n) + str(0)))
        else:
            ans = str(n) + str(((math.floor(n_sum / 10) + 1) * 10) - n_sum)
            print(int(ans))   
    
    t = t - 1

