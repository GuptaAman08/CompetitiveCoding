from heapq import heapify, heappop, heappush

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

heapify(a)

count = 0
while a[0] < k:
    if len(a) >= 2:
        count += 1
        print('Before : {}'.format(a))
        x = heappop(a)
        y = heappop(a)
        new_val = x + 2*y
        heappush(a, new_val)
        print('After : {}'.format(a))
    else:
        count = -1
        break
    

print(count)
