from sys import stdin


t = int(stdin.readline())

while t:
    n = int(stdin.readline())

    array = []
    for i in range(n):
        array.append(stdin.readline().strip())

    ans = 0
    for i in range(10):
        temp = 0
        for j in range(n):
            if int(array[j][i]) % 2 != 0:
                temp += 1
        
        if temp % 2 != 0:
            ans += 1
    
    print(ans)
    t -= 1
