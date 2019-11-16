# Given a Binary Tree, Print the corner nodes at each level. The node at the leftmost and the node at the rightmost.
from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printCorner(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)

    while q:
        t = len(q)

        for i in range(t):
            temp = q.popleft()
            
            if i == 0:
                print(temp.data, end=' ')
            elif i == t-1:
                print(temp.data, end=' ')

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)
        
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


printCorner(root)