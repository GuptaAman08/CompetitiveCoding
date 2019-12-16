from sys import stdin

def binomialCoefficient(n, k): 

    if(k > n - k): 
        k = n - k 

    res = 1
    
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res


t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]

    c0, c2 = 0, 0

    for x in a:
        if x == 2:
            c2 += 1
        elif x == 0:
            c0 += 1
    
    ans = 0

    if c2 >= 2:
        ans += binomialCoefficient(c2 , 2)

    if c0 >= 2:
        ans += binomialCoefficient(c0 , 2)

    print(int(ans))

    t -= 1