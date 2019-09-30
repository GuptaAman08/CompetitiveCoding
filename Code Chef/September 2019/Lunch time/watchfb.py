t = int(input())

while t:
    n = int(input())

    prev = [0, 0]
    flag = True
    for i in range(n):
        ty, a, b = [int(x) for x in input().split()] 
        min_score = min(a, b)
        max_score = max(a, b)
        if (min_score == max_score) or (ty == 1):
        
            print('YES')
            flag = True
        else:
            if flag == True:
                if min_score < prev[1]:
                
                    print('YES')
                    flag = True
                else:
                
                    print('NO')
                    flag = False
            else:
                print('NO')
                flag = False

        prev[0], prev[1] = min_score, max_score
    
    t -= 1