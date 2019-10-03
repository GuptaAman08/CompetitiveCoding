from sys import stdin

n, q = [int(x) for x in stdin.readline().split()]
arr = [False] * n

while q:
    typ, a, b = [int(x) for x in stdin.readline().split()]  

    if typ == 0:
        if a == b:
            arr[a] = not(arr[a])
        else:
            for j in range(a, b+1):
                arr[j] = not(arr[j])
                j += 1
    else:
        print(sum(arr[a:b+1]))
    q -= 1
