def gcd(a, b):
    if a == 0:
        return b

    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)
    


a = list(map(int, input().split()))
ans = a[0]
for i in range(1, len(a)):
    ans = gcd(a[i], ans)
print(ans)
