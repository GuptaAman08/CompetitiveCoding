from sys import stdin

t = int(stdin.readline())

while t:
    n = int(stdin.readline())
    a = [int(x) for x in stdin.readline().split()]

    if n == 1:
        print(1)
    else:

        a.sort()
        ans, diff = 0, a[1]-a[0]
        temp = []
        # print(a)
        if diff >= 2:
            ans = 1
            temp.append(a[0])
            temp.append(a[0]+1)
        else:
            temp.append(a[0])
        
        for i in range(1, n-1):
            if temp[-1] == a[i] - 1:
                temp.append(a[i])
                continue
            
            if a[i+1] == a[i] + 1:
                temp.append(a[i])
                continue
            else:
                temp.append(a[i])
                temp.append(a[i]+1)
                ans += 1

        if a[-1] - 1 != temp[-1]:
            ans += 1

        print(ans)

    t -= 1