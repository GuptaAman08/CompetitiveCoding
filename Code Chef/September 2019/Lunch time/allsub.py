from collections import Counter
t = int(input())

while t:
    s = input()
    r = input()

    c1 = Counter(s)
    c2 = Counter(r)

    flag = True
    
    for key, val in c1.items():
        if c2[key] >= val:
            c2[key] -= val
        else:
            flag = False
            break


    if flag:
        ans = ''
        for key, val in c2.items():
            if val > 0:
                ans = ans + key

        # print(ans)
        temp = sorted(ans)
        temp_len = len(temp)
        ns = ''
        i = 0
        if temp != []:
            while ( i < temp_len ) and (s[0] > temp[i]):
                ns = ns + temp[i] * c2[temp[i]]
                c2[temp[i]] = 0
                i += 1
            
            if c2[s[0]] > 0:
                if s <= s[0] * len(s):
                    ns = ns + s
                    ns = ns + c2[s[0]] * s[0]
                    c2[s[0]] = 0
                else:
                    ns = ns + c2[s[0]] * s[0]
                    ns = ns + s
                    c2[s[0]] = 0

                for j in range(i+1, temp_len):
                    ns = ns + temp[j] * c2[temp[j]]
                    c2[temp[j]] = 0
            else:
                ns = ns + s
                for j in range(i, temp_len):
                    ns = ns + temp[j] * c2[temp[j]]
                    c2[temp[j]] = 0
                
            print(ns)
        else:
            print(s)
    else:
        print('Impossible')
    
    t -= 1