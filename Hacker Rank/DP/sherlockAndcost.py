# link: https://www.hackerrank.com/challenges/sherlock-and-cost/editorial

n = int(input())
arr = [int(x) for x in input().split()]

d = [[0, 0] for x in range(n)]

for i in range(n-1):
    d[i+1][0] = max(d[i][0], d[i][1]+abs(1-arr[i]))
    d[i+1][1] = max(d[i][0]+abs(arr[i+1] - 1), d[i][1]+abs(arr[i+1] - arr[i]))
    print(d[i+1][1], d[i+1][0])

print(max(d[i+1][1], d[i+1][0]))