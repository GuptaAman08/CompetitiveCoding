# Print all nodes of a perfect binary tree in specific order
# Link : https://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/

from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printSpecificOrder(root):
    if root is None:
        return
    
    print(root.data, end=' ')

    if root.left:
        print(root.left.data,end=' ')
        print(root.right.data, end=' ')

    if root.left.left is None:
        return

    q = deque()
    q.append(root.left)
    q.append(root.right)

    f = None
    s = None
    while q:
        f = q.popleft()
        s = q.popleft()

        print(f.left.data, end=' ')
        print(s.right.data, end=' ')
        print(f.right.data, end=' ')
        print(s.left.data, end=' ')

        if f.left.left:
            q.append(f.left)
            q.append(s.right)
            q.append(f.right)
            q.append(s.left)




root = Node(1) 
   
root.left= Node(2) 
root.right   = Node(3) 
   
root.left.left  = Node(4) 
root.left.right = Node(5) 
root.right.left  = Node(6) 
root.right.right = Node(7) 
   
root.left.left.left  = Node(8) 
root.left.left.right  = Node(9) 
root.left.right.left  = Node(10) 
root.left.right.right  = Node(11) 
root.right.left.left  = Node(12) 
root.right.left.right  = Node(13) 
root.right.right.left  = Node(14) 
root.right.right.right  = Node(15) 

printSpecificOrder(root)