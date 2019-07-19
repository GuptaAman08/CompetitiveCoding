# no. of rows
m = int(input())
# no. of columns
n = int(input())

# k -> start row index
# l -> start column index
def printSpiral(mat, m, n):
    k, l = 0, 0
    while (k < m and l < n):

        for i in range(l,n):
            print(mat[k][i], end = " ")

        k += 1
        for i in range(k,m):
            print(mat[i][n-1], end = " ")

        n -= 1
        if k < m:
            for i in range(n-1,(l-1), -1):
                print(mat[m-1][i], end = " ")
            
            m -= 1
        
        if l < n:
            for i in range(m-1,(k-1), -1):
                print(mat[i][l], end = " ")
            
            l += 1
        

mat = []
for i in range(m):
    mat.append([int(x) for x in input().split()])
print(mat)
print()
printSpiral(mat,m,n)
