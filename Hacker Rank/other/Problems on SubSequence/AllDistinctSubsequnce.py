# Counting number of distinct sunsequence.
def CountDistinctSubsequence(arr, n):
    m = max(arr)
    last_occur = [-1 for i in range(m+1)]

    dp =  [-1 for i in range(n+1)]
    dp[0] = 1
    last_occur[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i-1] * 2
        if last_occur[arr[i-1]] != -1:
            dp[i] -= dp[last_occur[arr[i-1]]]
        last_occur[arr[i-1]] = i-1
    
    print(dp[n])

        
n = int(input())
arr = list(map(int, input().split()))
CountDistinctSubsequence(arr, n)
