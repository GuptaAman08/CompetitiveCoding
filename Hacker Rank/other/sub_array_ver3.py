from time import time


# Driver program 
n = int(input())
a = list(map(int, input().split()))

start = time()
# Pick starting point 
for i in range(0,n): 

    # Pick ending point 
    for j in range(i,n): 

        # Print subarray between 
        # current starting 
        # and ending points 
        for k in range(i,j+1): 
            print (a[k],end=" ") 

        print ("\n",end="") 
end = time()
print(end - start)