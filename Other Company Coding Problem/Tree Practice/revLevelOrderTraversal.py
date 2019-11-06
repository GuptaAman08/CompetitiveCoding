from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def rev_level_order_traversal(root):
    if root is None:
        return

    s = deque()
    q = deque()

    q.append(root)

    while q:
        node = q.popleft()
        s.append(node.data)

        # Right first because we need to print all levels from left to right 
        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    while s:
        print(s.pop(), end = ' ')


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(5) 
root.left.right = Node(6) 
root.right.left = Node(4) 
root.right.right = Node(7) 

rev_level_order_traversal(root)