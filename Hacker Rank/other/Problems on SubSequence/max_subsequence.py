n = int(input())
arr = [int(x) for x in input().split()]

# This var is to track whether all elements are negative in seqeunce
max_so_far = arr[0]
t = 0
for i in range(n):
    max_so_far = max(max_so_far, arr[i])
    if arr[i] >= 0:
        t += arr[i]

if max_so_far >= 0:
    print(t)
else:
    print(max_so_far)
