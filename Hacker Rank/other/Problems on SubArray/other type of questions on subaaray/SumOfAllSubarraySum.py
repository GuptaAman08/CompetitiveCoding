# Over here we are finding the occurence of each elements in all sub arrays

n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    res += a[i] * (i + 1) * (n - i)

print(res)


