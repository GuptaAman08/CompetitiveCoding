# Link : https://www.geeksforgeeks.org/number-of-larger-elements-on-right-side-in-a-string/

n = int(input('Lenght of String: '))
s = input('String: ')

# Stores count of each character(a-z) at any point in time
count = [0] * 26

# For ith index value stored denotes- number of characters greater than current in right of it   
ans = [0] * n

for i in range(n-1, -1, -1):
    temp = ord(s[i]) - ord('a') 
    count[temp] += 1
    for j in range(temp+1, 26):
        ans[i] += count[j]

for i in range(n):
    print(ans[i], end=' ')
