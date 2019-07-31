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
        # all negative case
        ans = max(a)
    else:
        cur_max = a[0]
        cur_sum = a[0]
        for i in range(1, n):
            if cur_sum + a[i] < 0:
                cur_sum = 0
            else:
                cur_sum += a[i]
                cur_max = max(cur_max, cur_sum)
        ans = cur_max
        
    return ans

a =list(map(int, input().split())) 
n = len(a) 
result = getMaxSubArray(a,n)
print(f"Maximum sum sub-array is {result}")