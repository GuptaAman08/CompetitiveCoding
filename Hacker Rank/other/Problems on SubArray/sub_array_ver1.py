from time import time
n = int(input())
a = list(map(int, input().split()))

# The outer loop basically decides what length subarray to print now.
start = time()
for i in range(n):
    temp = i
    for j in range(n):
        temp = j+i+1
        if temp <= n:
            print(*a[j:temp])
        else:
            break
end = time()
print(end - start)