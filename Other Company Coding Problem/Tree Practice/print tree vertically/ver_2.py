# An O(nlogn) approach 
# Link : https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
# This solution has a bug, since there is a posibility that a node in same vertical level is not printed in proper order
# see this case in above link at end

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
    
    FindMinMax(node.left, d, hd-1)
    d[hd].append(node.data)
    FindMinMax(node.right, d, hd+1)


def verticalOrder(root):
    if root is None:
        return

    d = defaultdict(list)
    FindMinMax(root, d, 0)


    for key in sorted(d):
        print(key ,*d[key])

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12) 

print('Vertical Traversal is :')
verticalOrder(root)