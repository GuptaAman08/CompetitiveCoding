# Selection sort
n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    min_arr = arr[i]
    min_ind = i
    for j in range(i, n):
        if min_arr > arr[j]:
            min_arr = arr[j]
            min_ind = j
    arr[min_ind] = arr[i]
    arr[i] = min_arr

print(arr)

# comparison of selection sort and bubble sort 
# bubble sort is stable but selection isnt
# selection is better and efficient than bubble for large number of elements
