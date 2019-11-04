from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printSpiralTree(root):
    s1 = deque()
    s2 = deque()

    s1.append(root)
    while s1 or s2:
        
        while s1:
            node = s1.pop()
            print(node.data, end=' ')

            if node.right:
                s2.append(node.right)

            if node.left:
                s2.append(node.left)

        while s2:
            node = s2.pop()
            print(node.data, end=' ')

            if node.left:
                s1.append(node.left)

            if node.right:
                s1.append(node.right)



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)
root.left.left.left = Node(8) 
root.left.left.right = Node(9)

print("Spiral Order traversal of binary tree is")  
printSpiralTree(root)