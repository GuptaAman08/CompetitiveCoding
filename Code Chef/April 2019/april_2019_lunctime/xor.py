import math
t = int(input())

while t != 0:
    N = int(input())
    A = [f'{int(x):032b}' for x in input().split()]

    min_sum = 0
    for i in range(32):
        count = len(list(filter(lambda x: (x[i] == '1'), A)))
        min_sum = min_sum + min(count, N - count) * math.pow(2, 31-i)
    t -= 1
    print(int(min_sum))

