# Assumes there is atleast one positive element in Array
# to handle all negative case we can take max(array) 
# The sum_i variable here finds maximum sub-array till/ending at index i
# link : https://www.youtube.com/watch?v=ohHWQf1HDfU
# Complexity O(n)

def getMaxSubArray(a,n):
    # Max_so_far
    ans = 0
    t = list(filter(lambda x : (x<0), a))
    if len(t) == n:
        ans = max(a)
    else:
        sum_i = 0
        for i in range(n):
            if sum_i+a[i] > 0:
                sum_i += a[i]
                ans = max(ans, sum_i)
            else:
                sum_i = 0
    return ans

a =list(map(int, input().split())) 
n = len(a) 
result = getMaxSubArray(a,n)
print(f"Maximum sum sub-array is {result}")