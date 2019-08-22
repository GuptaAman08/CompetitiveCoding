from collections import Counter

n = int(input())

t = []
for i in range(1, n+1):
    temp = i
    sum_i = 0
    while temp:
        sum_i += temp % 10
        temp = temp // 10

    t.append(sum_i)

c = Counter(t)
count = 0
prev = 0
for key, value in c.items():
    prev = value
    break

for key, value in c.items():
    if prev == value:
        count += 1
        prev = value
    else:
        break

print(count)


