# Best explanation for this is https://www.youtube.com/watch?v=6w60Zi1NtL8
n = int(input())
a = [int(x) for x in input().split()]

incl = a[0]
excl = 0

for i in range(1, n):
    new_excl = max(incl, excl)
    incl = excl + a[i]
    excl = new_excl
    
if incl > excl:
    print(incl)
else:
    print(excl)