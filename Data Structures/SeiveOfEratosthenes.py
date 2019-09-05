# Given a number n, print all primes smaller than or equal to n.
# The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so
# Link : https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# O(n*log(log(n)))

n = int(input())

a = [True] * (n+1)

i = 2
while i*i <= n:
    if a[i] == True:
        for j in range(i*i, n+1, i):
            a[j] = False
    i = i+1

for i in range(2, n+1):
    if a[i] == True:
        print(i, end=" ")