# Finding a number which is a power of 2 just less than given number.
# eg if given number is 132 nearest power of 2 just less than n is 128
# The worst case time is O(n),in that case the given number will be of type 2^x - 1

n = int(input())
res = 0
for i in range(n,0,-1):
    if ((i & (i-1)) == 0):
       res = i
       break

print(res) 