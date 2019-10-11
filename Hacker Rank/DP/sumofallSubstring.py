# link : https://www.hackerrank.com/challenges/sam-and-substrings/problem

num = input()
mod = 1000000007

n = len(num) 

temp = int(num[0])
res= int(num[0])
for i in range(1, n): 
    numi = int(num[i]) 
    
    temp = (i + 1) * numi + 10 * temp
    temp = temp % mod
    res = (res + temp)%mod 

print(res)
