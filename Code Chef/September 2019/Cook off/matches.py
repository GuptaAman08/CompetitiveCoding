c = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

t = int(input())

while t:
    a, b = [int(x) for x in input().split()]

    ans = str(a + b)
    count = 0

    for i in ans:
        count += c[int(i)]

    print(count)
    t -= 1