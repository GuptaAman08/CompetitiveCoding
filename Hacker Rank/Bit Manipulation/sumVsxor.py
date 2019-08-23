# link https://www.hackerrank.com/challenges/sum-vs-xor/problem

from collections import Counter

n = int(input())

c = Counter(bin(n)[2:])

if n == 0:
    print(1)
else:
    print(pow(2, c['0']))

    

    