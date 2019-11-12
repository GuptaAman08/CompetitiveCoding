# An O(n) approach 
# Link : https://www.geeksforgeeks.org/find-maximum-vertical-sum-in-binary-tree/
from collections import defaultdict

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def FindMinMax(node, d, hd):

    if node is None:
        return
    
    d[hd] += node.data
    FindMinMax(node.left, d, hd-1)
    FindMinMax(node.right, d, hd+1)


def verticalOrder(root):
    if root is None:
        return

    d = defaultdict(int)
    FindMinMax(root, d, 0)

    print(max(d.values()))


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 

print('Maximum Vertical Sum is :')
verticalOrder(root)