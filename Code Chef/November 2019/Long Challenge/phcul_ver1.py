# cook your dish here
# Gives just 50Marks
from sys import stdin
import math

def giveMin(s1, s2, n, m):
    ans1 = float('inf')
    for i in range(n):
        temp, a, b = s1[i]
        min_v = float('inf')
        for j in range(m):
            dis = temp+math.sqrt((a-s2[j][1])**2 + (b-s2[j][2])**2) + s2[j][0]
            if dis < min_v:
                min_v = dis

        if min_v < ans1:
            ans1 = min_v
    return ans1
    

def cal_Mindist(t1, t2, n, m, s):

    for i in range(0, 2*n, 2):
        temp = float('inf')
        for j in range(0, 2*m, 2):
            t = math.sqrt((t2[j]-t1[i])**2 + (t2[j+1]-t1[i+1])**2)
            if t < temp:
                temp = t

        s.append([temp, t1[i], t1[i+1]])


t = int(stdin.readline())

while t:
    x, y = [int(x) for x in stdin.readline().split()]
    n, m, k = [int(x) for x in stdin.readline().split()]

    s1 = [int(x) for x in stdin.readline().split()]
    s2 = [int(x) for x in stdin.readline().split()]
    s3 = [int(x) for x in stdin.readline().split()]

    sx1, sx2, s13, s23 = [], [], [], []

    for i in range(0, 2*n, 2):
        sx1.append([math.sqrt((x-s1[i])**2 + (y-s1[i+1])**2), s1[i], s1[i+1]])
    
    for i in range(0, 2*m, 2):
        sx2.append([math.sqrt((x-s2[i])**2 + (y-s2[i+1])**2), s2[i], s2[i+1]])

    cal_Mindist(s1, s3, n, k, s13)
    cal_Mindist(s2, s3, m, k, s23)
    
    print(min(giveMin(sx1, s23, n, m), giveMin(sx2, s13, m, n)))

    t -= 1