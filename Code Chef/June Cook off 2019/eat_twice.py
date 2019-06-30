from collections import defaultdict

t = int(input())
while t != 0:

    n, m = [int(x) for x in input().split()]
    c = defaultdict(int)

    # Using here techniques to find first and second minimum in single traversal ....refer geeksforgeeks

    first, second = 0, 0
    for i in range(n):
        day, taste = [int(x) for x in input().split()]
        if c[day] < taste:
            c[day] = taste
        

    for value in c.values():
        if first < value:
            second = first
            first = value
        elif (second < value) and (value != first):
            second = value

    print(first+second)

    t = t - 1