t = int(input())
# n -> No. of Customers
# m -> No. of Flavours
while t!=0:
    n, m = list(map(int, input().split()))

    flavour_count = list(map(int, input().split()))

    waiting_cust = []
    max_profit = 0
    order = []
    x = []

    for i in range(n):
        d, f, b = list(map(int, input().split()))
        if flavour_count[d-1] > 0:
            flavour_count[d-1] -= 1
            max_profit += f
            order.append(d)
        else:
            max_profit += b
            order.append(0)

    
    for i in range(m):
        if flavour_count[i] != 0:
            x.append([i, flavour_count[i]])


    for i in range(n):
        if order[i] == 0:
            if x[-1][1] != 0:
                x[-1][1] -= 1
                order[i] = x[-1][0] + 1
            else:
                x.pop()
                x[-1][1] -= 1
                order[i] = x[-1][0] + 1
    
    print(max_profit)
    # This type of print eliminates square brackets at the end of list and prints only elements of list
    print(*order)
    t -= 1

    


