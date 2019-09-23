# Heap Sort
heap_size = [0]

def maxHeapify(arr, i):
    left = 2*i
    right = 2*i + 1

    largest = i
    if left <= heap_size[0] and arr[left] > arr[largest]:
        largest = left

    if right <= heap_size[0] and arr[right] > arr[largest]:
        largest = right

    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, largest)


def buildmaxheap(arr, n):
    heap_size[0] = n
    t = (n // 2)

    for i in range(t, 0, -1):
        maxHeapify(arr, i)


def heapsort(arr, n):
    buildmaxheap(arr, n)
    # print(arr)
    for i in range(n, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heap_size[0] = heap_size[0] - 1
        maxHeapify(arr, 1)


n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

heapsort(arr, n)

print(arr[1:])
