# Merge Sort 
import sys

def merge(arr, start, mid, end):
    l1 = mid - start + 1
    l2 = end - mid 
    a1, a2 = [], []

    for i in range(l1):
        a1.append(arr[start+i])

    for i in range(l2):
        a2.append(arr[mid+i+1])

    a1.append(sys.maxsize)
    a2.append(sys.maxsize)
    j, k = 0, 0
    for i in range(start, end+1):
        if a1[k] > a2[j]:
            arr[i] = a2[j]
            j += 1
        else:
            arr[i] = a1[k]
            k += 1
    
    

def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merge(arr, start, mid, end)
        print(arr)

n = int(input())
arr = list(map(int, input().split()))

mergesort(arr,0, n-1)