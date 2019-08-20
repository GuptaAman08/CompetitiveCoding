# link https://www.hackerrank.com/challenges/sansa-and-xor/problem
# finding xor of subarrays xors
n = int(input())

arr = list(map(int, input().rstrip().split()))

res = 0
for i in range(n):
    freq = (i + 1)*(n - i)

    if freq % 2 != 0:
        res = res ^ arr[i]
print(res)
