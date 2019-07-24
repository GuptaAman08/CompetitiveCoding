# link : https://www.geeksforgeeks.org/greatest-contiguous-sub-array-of-size-k/
def findSubarray(a, k, n): 
    vec=[] 

    # Iterate to find all the sub-arrays 
    for i in range(n-k+1): 
        # Push the vector in the container 
        vec.append(a[i:i+k]) 

    # Sort the vector of elements
    print(vec)
    vec=sorted(vec) 
    print(vec)

    # The last sub-array in the sorted order 
    # will be the answer 
    return vec[len(vec) - 1] 

a =list(map(int, input().split())) 
k = 4
n = len(a) 

# Get the sub-array 
ans = findSubarray(a, k, n) 

print(ans) 