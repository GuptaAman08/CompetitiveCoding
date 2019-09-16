# given n find gray code arrangement of first 0,1,2.....2^n-1
def graycode(n):
    if n <= 0:
        print(0)

    a = list()

    a.append('0')
    a.append('1')

    i = 2
    j = 0

    while True:

        if i >= (1 << n):
            break

        for j in range(i-1, -1 , -1):
            a.append(a[j])

        for j in range(i):
            a[j] = '0' + a[j]
        
        for j in range(i, 2*i):
            a[j] = '1' + a[j]
        
        i = i << 1

    for i in a:
        print(int(i, 2), end=' ') 

n = int(input())
graycode(n)