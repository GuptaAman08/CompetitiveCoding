# Not for negative integers
n = int(input())
arr = list(map(int, input().split()))

k = max(arr)
temp = [0] * (k + 1)
final = [0] * (n)

for i in range(n):
    temp[arr[i]] += 1


for i in range(1, k+1):
    temp[i] += temp[i-1]


for i in range(n-1, -1, -1):
    final[temp[arr[i]] - 1] = arr[i]
    temp[arr[i]] -= 1

print(final)

