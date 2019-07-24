# To find whether there exist any subArray with a given value as sum of that subarray
# link https://www.geeksforgeeks.org/find-subarray-with-given-sum/
# First Method -> O(n)  .....Optimized version of ver1

# For non-negative integers only
def checkForSumEqualK(a, n, s):        
    cur_sum = a[0]
    start = 0
    if cur_sum == s:
        print('SubArray Found: ', end=" ")
        print(f"At index {start}")
        return
    for i in range(1, n):
        cur_sum += a[i]

        while (cur_sum > s) and (start < i):
            cur_sum -= a[start]
            start += 1
        
        if cur_sum == s:
            print('SubArray Found: ', end=" ")
            print(f"Between index {start} and {i}")
            return
    
    print("No such SubArray Found")
        


a = list(map(int, input().split()))
n = len(a) 
s = int(input())

checkForSumEqualK(a, n, s)