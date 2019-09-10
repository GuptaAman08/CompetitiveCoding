# https://www.geeksforgeeks.org/binomial-coefficient-dp-9
# In time O(n*k) and space O(k)

def BinomialCoff(n, k):
    C = [0 for i in range(k+1)]
    C[0] = 1
    for i in range(1, n+1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j-1]
            j -= 1

    return C[k]

n, k  = [int(x) for x in input().split()]
print(BinomialCoff(n, k))