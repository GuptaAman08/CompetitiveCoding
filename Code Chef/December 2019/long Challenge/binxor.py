from sys import stdin
from collections import Counter

mod = 1000000007

fact = [1]
for i in range(1, 100002):
    fact.append(fact[i-1]*i%mod)

def powfunc(a, b, mod):
    res = 1
    a = a % mod
    while b > 0:
        if b & 1:
            res = (((res%mod + a%mod)%mod)+m)%mod
        
        b = b >> 1
        a = (((a%mod + a%mod)%m)+m)%mod

    return res

def modInv(n, p):
    return powfunc(n, p-2, p)%mod

def calnCr(n, r, m):
    if r == 0 or r == n:
        return 1
    return (fact[n] * ((modInv(fact[r], mod)%mod + modInv(fact[n-r], mod)%mod)%mod))%mod

t = int(stdin.readline())

while t:
    n = int(stdin.readline())
    a = stdin.readline().strip()
    b = stdin.readline().strip()

    c1, c2 = Counter(a), Counter(b)

    max1 = min(c1['0']+c2['0'], c1['1']+c2['1'])
    min1 = abs(c2['1'] - c1['1'])

    
    i = max1
    ans = 0
    while i >= min1:
        ans = (ans + ((calnCr(n, i, mod)%mod))%mod
        i -= 2

    print(ans % mod)
    t -= 1

  