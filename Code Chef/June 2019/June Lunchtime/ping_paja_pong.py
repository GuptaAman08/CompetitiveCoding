t = int(input())

while t != 0:
    x, y, k = list(map(int, input().split()))

    to_check = int((x + y)/k)

    if to_check % 2 == 0:
        print('Chef')
    else:
        print('Paja')

    t -= 1
