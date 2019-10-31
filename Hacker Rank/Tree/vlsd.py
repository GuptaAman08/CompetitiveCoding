# Vertical level sum difference
# Link : https://www.hackerrank.com/contests/rtech-april-18-01/challenges/vertical-level-sum-differences/problem

from collections import defaultdict

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Find minimum and maximum horizontal distance from root 
def FindMinMax(node, d, hd):

    if node is None:
        return
    
    if hd % 2 == 0:
        d['even'] += node.data
    else:
        d['odd'] += node.data
        
    FindMinMax(node.left, d, hd-1)
    FindMinMax(node.right, d, hd+1)


def verticalOrder(root):
    if root is None:
        return

    d = defaultdict(int)
    d['odd'] = 0
    d['even'] = 0
    FindMinMax(root, d, 0)
    # print(d)

    print(d['even'] - d['odd'])


def createTree(a, root, i, n):
    
    if i < n and a[i] != -1:
        temp = Node(a[i])
        root = temp
        
        root.left = createTree(a, root.left, 2*i + 1, n)
        root.right = createTree(a, root.right, 2*i + 2, n)
    return root
    
    
n = int(input())
a = [int(x) for x in input().split()]

root = None
root = createTree(a, root, 0, n)

verticalOrder(root)
