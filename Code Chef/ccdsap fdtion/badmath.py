# cook your dish here
from sys import stdin

all_com = ['1']
for i in range(16383):
    all_com.append(all_com[i] + '0')
    all_com.append(all_com[i] + '1')


t = int(stdin.readline())

while t:
    n, m = [int(x) for x in stdin.readline().split()]
    s = stdin.readline().strip()
    
    t1 = list(s.replace('_', '0'))
    pos = [i for i in range(n-1,-1,-1) if s[i] == '_']
    
    temp = t1
    ans = 0
    if ((int(''.join(temp), 2)) % m) == 0:
        ans += 1
    
    br = 2**(s.count('_'))
    
    for it in range(br-1):
        st = all_com[it]
        j = 0
        l = len(st)
        
        for k in range(l-1, -1,-1):
            
            temp[pos[j]] = st[k]
            j += 1
            
        if ((int(''.join(temp), 2)) % m) == 0:
            ans += 1
        
        temp = t1
        
        
    print(ans)
    t -= 1