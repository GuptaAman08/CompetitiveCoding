from time import time
n = int(input())
a = list(map(int, input().split()))

# This is based on combinatoric link:https://www.quora.com/What-is-the-most-efficient-way-of-finding-all-the-subarrays-from-an-array-of-integers

# Here we make selection for start(i) and end(j) indices such that i<=j
start = time()
for i in range(n):
    for j in range(i,n):
        print(*a[i:j+1])
end = time()
print(end - start)