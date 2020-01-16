# Link: https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# n should be less than 10 million
n = int(input('Enter n below which all primes are required : '))

prime = [True for i in range(n+1)]
p = 2

while p*p <= n:
    if prime[p] == True:
        for i in range(p*p, n+1, p):
            prime[i] = False

    p += 1

for i in range(2, n+1):
    if prime[i]:
        print(i)


