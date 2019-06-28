
t=int(input())

for _ in range(t):
    k = int(input())
    mod = 1000000007
    ans = pow(2, (k-1), mod)
    print(ans * 10)

    