class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def CheckBST(root, minVal, maxVal):
    if root is None:
        return True

    # Check if root's data is out of range 
    if root.data < minVal or root.data > maxVal:
        return False

    return CheckBST(root.left, minVal, root.data) and CheckBST(root.right, root.data, maxVal)

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 

if CheckBST(root, float('-inf'), float('inf')):
    print('Given tree is binary search tree')
else:
    print('Given tree is not binary search tree')