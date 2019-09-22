# Bubble sort
# optimized version

n = int(input())
arr = list(map(int, input().split()))

flag = 1

for i in range(n-1):
    flag = 0
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = 1

    if flag == 0:
        break

print(arr)
