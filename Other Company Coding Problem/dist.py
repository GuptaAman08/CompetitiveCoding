# Here we are suppose to find the sum of dist of one same element with all other same element
# for eg: in 3 4 3 4 3 ------ the sum of dist for 3 is 5((1) + (3+1))

from collections import defaultdict

dist = defaultdict(list)

i = 1
for x in input().split():
    dist[int(x)].append(i)
    i += 1

for key, value in dist.items():
    sum_key = 0
    current_len = len(value)
    for i in range(1, current_len):
        sum_key += i * (current_len - i) * (value[i] - value[i-1] - 1)
        sum_key += ((i) * (i-1))//2
    print(sum_key)
# print(dist)
