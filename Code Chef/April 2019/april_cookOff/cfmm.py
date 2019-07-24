from collections import Counter
t = int(input())
while t != 0:
    n = int(input())

    s = ''
    for i in range(n):
        s += input()

    c = Counter(s)

    # Important logic
    print(min(c['c']//2,c['e']//2,c['o'],c['d'],c['h'],c['f']))
    t -= 1