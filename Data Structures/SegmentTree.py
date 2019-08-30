# For Update and Range Queries
# 1 - Based Indexing
# refer : https://github.com/vijay532/CompetitiveSources/blob/master/SumOfRangesSegment.cpp and https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
import math

n = int(input())
arr = [0] * (n+1)

# Size of Segment Tree stored as array 
Tree = [0] * (2 * pow(2, math.ceil(math.log(n, 2))))

for ind, val in enumerate(input().split()):
    arr[ind+1] = int(val)




# Build Segment Tree
def BuildTree(node, start, end):
    if start == end:
        Tree[node] = arr[start]
        return arr[start]
    
    mid = (start + end) // 2
    Tree[node] = BuildTree(2*node, start, mid) + BuildTree(2*node + 1, mid + 1, end)
    return Tree[node]


# Get Range Sum
def getSum(node, left, right, start, end):
    if (left>end) or (right<start) or (start>end):
        return 0
    elif (left<=start) and (right >= end):
        return Tree[node]
    mid = (start + end) // 2
    return (getSum(2*node, left, right, start, mid) + getSum(2*node + 1, left, right, mid+1, end))


# Update Segment Tree
def updateTree(node, index, value, start, end):
    if (index < start) or (index > end):
        return
    
    diff = value - arr[index]
    Tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        updateTree(2*node, index, value, start, mid)
        updateTree(2*node + 1, index, value, mid + 1, end)




# Building Segment Tree
BuildTree(1, 1, n)

TypeQ, a, b = list(map(int, input().split()))

if TypeQ == 1:
    # Range Query
    range_sum = getSum(1, a, b, 1, n)
    print(f'Range sum is {range_sum}')
else:
    # Update Query
    print(f'Before Update {Tree}')
    updateTree(1, a, b, 1, n)
    print(f'After Update {Tree}')