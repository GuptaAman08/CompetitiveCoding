
t=int(input())



for _ in range(t):
    k = int(input())
    mod = 1000000007
    ans = pow(2, (k-1), mod)
    ans = ans * 10
    ans = ans % 1000000007
    print(ans)
    