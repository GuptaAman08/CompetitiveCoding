#Code of youtube video
from sys import stdin

arr = [0]*100000

t = int(stdin.readline().strip())

while t:
    s = stdin.readline().strip()
    n = len(s)
    maxblk = 0

    for i in range(n):
        arr[i+1] = arr[i]
        if s[i] == '1':
            arr[i+1] += 1


    for i in range(n):
        for j in range(i+1,n+1):
            maxblk = max(maxblk, (arr[j]-arr[i])+(i-arr[i])+(n-j-(arr[n]-arr[j])))
            maxblk = max(maxblk, arr[i]+(arr[n]-arr[j])+(j-i-(arr[j]-arr[i])))

    print(n-maxblk)
    arr = [0]*100000

    t -= 1
