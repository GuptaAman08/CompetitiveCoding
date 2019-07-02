from collections import Counter
t = int(input())

while t != 0:
    n = int(input())
    s = list(input())

    c = Counter(s)
    ans = int((c['P'] * 100)/ n)

    proxy = 0
    if ans >= 75:
        print(0)
    else:
        flag = 0
        for i in range(2,n-2):
            if (s[i-1] == 'P' or s[i-2] == 'P') and (s[i+1] == 'P' or s[i+2] == 'P') and (s[i] == 'A'):
                proxy += 1
                c['P'] += 1
                ans = int((c['P'] * 100) / n)
                if ans >= 75:
                    flag = 1
                    print(proxy)
                    break
        if flag == 0:
            print(-1)
        

    t -= 1
