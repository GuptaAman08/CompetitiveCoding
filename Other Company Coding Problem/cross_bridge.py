# In python
a = list(map(int, input().split()))
n = len(a)

if n != 4:
    print('Invalid Input')
    exit(1)
else:
    min_a = min(a)
    final_time = (n-2) * 1

    for i in range(n):
        final_time += a[i]

    final_time -= min_a
    print(final_time)





