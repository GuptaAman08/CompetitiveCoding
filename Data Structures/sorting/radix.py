def counting_sort(arr, exp):
    n = len(arr)

    # To store counts of each 0-9 digits
    c = [0] * 10
    # To store sorted output
    b = [0] * n

    for i in range(n):
        index = int(arr[i] / exp)
        c[index % 10] += 1
    
    for i in range(1, 10):
        c[i] += c[i-1]

    for i in range(n-1,-1,-1):
        index = int(arr[i] / exp)
        b[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1

    for i in range(n):
        arr[i] = b[i]

    print(arr)

def radix_sort(arr):
    # Finding maximum in a list to determine the number of digits
    d = max(arr)

    exp = 1
    while d/exp > 0:
        counting_sort(arr, exp)
        exp *= 10

arr = [int(x) for x in input().split()]
radix_sort(arr)

