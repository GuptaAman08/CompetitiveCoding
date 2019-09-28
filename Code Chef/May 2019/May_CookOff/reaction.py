t = int(input())

while t:
    r, c = [int(x) for x in input().split()]

    grid = []

    for i in range(r):
        grid.append([int(x) for x in input().split()])

    flag = True
    count = 0


    for i in range(r):
        j = 0
        while j < c and flag == True:
            if i+1 < r and i+1 >= 0:
                count += 1

            if i-1 < r and i-1 >= 0:
                count += 1

            if 0 <= j-1 and j-1 < c:
                count += 1

            if 0 <= j+1 and j+1 < c:
                count += 1
            
            if count <= grid[i][j]:
                flag = False
                
            j += 1
            count = 0
        
    if flag:
        print('Stable')
    else:
        print('Unstable')
    
    t -= 1
        