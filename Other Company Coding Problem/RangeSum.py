n = int(input())
a = [int(x) for x in input().split()]

l = int(input())
r = int(input())

prefix_sum = []
prefix_sum.append(a[0])

for i in range(1, n):
    prefix_sum.append(prefix_sum[i-1] + a[i])

print(prefix_sum)
# Finding sum in a given range
if l == 0:
    print(prefix_sum[r])
else:
    print(prefix_sum[r] - prefix_sum[l-1])