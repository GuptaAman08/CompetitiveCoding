
n = 7
i = 1
t = (f'{i:032b}').replace('1', '9')
while (int(t) % n) != 0:
    i += 1
    t = (f'{i:032b}').replace('1', '9')

print(int(t))