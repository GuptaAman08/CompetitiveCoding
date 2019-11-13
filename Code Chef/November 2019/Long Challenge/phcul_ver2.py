# cook your dish here
# For 100 mks
from sys import stdin
import math


t = int(stdin.readline())

while t:
    x, y = [int(x) for x in stdin.readline().split()]
    n, m, k = [int(x) for x in stdin.readline().split()]

    s1 = [int(x) for x in stdin.readline().split()]
    s2 = [int(x) for x in stdin.readline().split()]
    s3 = [int(x) for x in stdin.readline().split()]

    
    ans1 = float('inf')
    for i in range(0, 2*n, 2):
        d1 = math.sqrt((x-s1[i])**2 + (y-s1[i+1])**2)
        if d1 < ans1:
            for j in range(0, 2*m, 2):
                d2 = d1 + math.sqrt((s2[j]-s1[i])**2 + (s2[j+1]-s1[i+1])**2)
                if d2 < ans1:
                    for l in range(0, 2*k, 2):
                        d3 = d2 + math.sqrt((s2[j]-s3[l])**2 + (s2[j+1]-s3[l+1])**2)
                        if d3 < ans1:
                            ans1 = d3


    ans2 = float('inf')
    for i in range(0, 2*m, 2):
        d1 = math.sqrt((x-s2[i])**2 + (y-s2[i+1])**2)
        if d1 < ans2:
            for j in range(0, 2*n, 2):
                d2 = d1 + math.sqrt((s2[i]-s1[j])**2 + (s2[i+1]-s1[j+1])**2)
                if d2 < ans2:
                    for l in range(0, 2*k, 2):
                        d3 = d2 + math.sqrt((s1[j]-s3[l])**2 + (s1[j+1]-s3[l+1])**2)
                        if d3 < ans2:
                            ans2 = d3
    print(min(ans1, ans2))
    t -= 1