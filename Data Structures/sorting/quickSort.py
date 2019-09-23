# QuickSort Algorithm
def partition(arr, start, end):
    j = start - 1
    for i in range(start, end):
        if arr[end] > arr[i]:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[j+1], arr[end] = arr[end], arr[j+1]
    print(arr)
    return (j+1)
    

def QuickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        QuickSort(arr, start, p-1)
        QuickSort(arr, p+1, end)
        

n = int(input())
arr = list(map(int, input().split()))

QuickSort(arr, 0, n-1)