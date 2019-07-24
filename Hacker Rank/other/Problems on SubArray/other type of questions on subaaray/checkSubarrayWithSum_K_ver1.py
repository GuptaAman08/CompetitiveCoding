# To find whether there exist any subArray with a given value as sum of that subarray
# link https://www.geeksforgeeks.org/find-subarray-with-given-sum/
# First Method -> O(n^2)

# For non-negative integers only
def checkForSumEqualK(a, n, s):
    # starting point for each sub-array
    for i in range(n):
        cur_sum = a[i]
        if cur_sum == s:
            print("Founded the subArray")
            print(f"At index {i}")
            return
        for j in range(i+1,n):
            cur_sum += a[j]
            if cur_sum == s:
                print("Founded the subArray")
                print(f"Between index {i} and {j}")
                return
    
    print("No such SubArray exist")
        
a = list(map(int, input().split()))
n = len(a) 
s = int(input())

checkForSumEqualK(a, n, s)