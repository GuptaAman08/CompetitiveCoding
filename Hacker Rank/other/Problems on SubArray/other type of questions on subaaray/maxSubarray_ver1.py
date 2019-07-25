# Maximum sub-array sum
# O(n^2) approach

def getMaxSubArray(a,n):
    ans = float('-inf')
    for i in range(n):
        sum_i = 0
        # Iterate over all length of subarrays starting at index i
        for j in range(n):
            if (i+j) >= n:
                break
            sum_i += a[i+j]
            ans = max(ans, sum_i)
    return ans

a =list(map(int, input().split())) 
n = len(a) 
result = getMaxSubArray(a,n)
print(f"Maximum sum sub-array is {result}")