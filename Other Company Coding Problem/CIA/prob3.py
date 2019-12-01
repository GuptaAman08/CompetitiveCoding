from sys import stdin
from collections import Counter

n = int(stdin.readline())
arr = [int(x) for x in stdin.readline().split()] 

rank = [0] * n
parent = list(range(n))


def findSet(ele, parent):
    if ele == parent[ele]:
        return ele
    parent[ele] = findSet(parent[ele], parent)
    return parent[ele]


def union(u, v, parent, rank):
    p1 = findSet(u, parent)
    p2 = findSet(v, parent)

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p2] > rank[p1]:
        parent[p1] = p2
    else:
        rank[p1] += 1
        parent[p2] = p1


def findMax(arr, start, end):
    max_v, ind = float('-inf'), -1
    for i in range(start, end):
        if max_v < arr[i]:
            max_v = arr[i]
            ind = i
    
    return max_v, ind


for i in range(n-1):
    a = arr[i]
    b, ind = findMax(arr, i+1, n)
    if arr[i] < arr[ind]:
        if findSet(i, parent) != findSet(ind, parent):
            union(i, ind, parent, rank)
        arr[ind] = a ^ b


for i in range(n):
    findSet(i, parent)


c = Counter(parent)

print(len(c.keys()))
print(*sorted(c.values()))
