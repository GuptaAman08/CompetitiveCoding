# Link: https://www.youtube.com/watch?v=Mwl6ng4jbn0
from sys import stdin
import math

def glr(x):
    sum_n = (x*(x+1))//2
    init = x
    sum_a = 0
    power = 0

    while x >= 1:
        temp = (x+1)//2
        sum_a += temp * (2**power)
        x = x - temp
        power += 1

    sum_b = sum_n - sum_a
    sum_b -= (int(math.log(init, 2))+1)

    return sum_b



t = int(stdin.readline())

while t:
    l, r = [int(x) for x in stdin.readline().split()]

    ans = 0
    if l == 1:
        ans = glr(r)
    else:
        ans = glr(r) - glr(l-1)

    print(ans)

    t -= 1

