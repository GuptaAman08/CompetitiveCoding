from sys import stdin

t = int(stdin.readline())

while t:
    s = stdin.readline().split()
    if 'not' in s:
        print('Real Fancy')
    else:
        print('regularly fancy')
    t -= 1