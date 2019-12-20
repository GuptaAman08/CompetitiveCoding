from sys import stdin


t = int(stdin.readline())

while t:
    a = stdin.readline().strip()
    b = stdin.readline().strip()

    if b == '0':
        print(0)
    else:
        la, lb = len(a), len(b)
        # print(a, b, len(a), len(b))
    
        l = 0
        if la>lb:
            b = '0'*(la-lb) + b
            l = la
        else:
            a = '0'*(lb-la) + a
            l = lb

    
        res, i = 1, l-1

        while i >= 0:
            if a[i] == '1' and b[i] == '1':
                j = i - 1
                while j >= 0 and a[j]!=b[j]:
                    j -= 1
                res = max(res, i-j+1)
                i = j
            else:
                i-=1
        
        print(res)



    t -= 1