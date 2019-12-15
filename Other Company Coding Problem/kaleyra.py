from sys import stdin

n, m, x = [int(x) for x in stdin.readline().split()]

temp = []

for i in range(n):
    cur, exp = [int(x) for x in stdin.readline().split()]
    temp.append(exp-cur)

temp.sort()
a = [int(x) for x in stdin.readline().split()]

a.sort()

a.append(float('inf'))
temp.append(float('inf'))


a_1 = []
j, k = 0, 0


for i in range(n+m):
    if temp[j] < a[k]:
        a_1.append(temp[j])
        j += 1
    else:
        a_1.append(a[k])
        k += 1


count, ans = 0, 0
i = 0
while i<(n+m) and ans <= x:
    ans += a_1[i]
    count += 1
    i += 1

if ans > x:
    print(count - 1)
else:
    print(count)