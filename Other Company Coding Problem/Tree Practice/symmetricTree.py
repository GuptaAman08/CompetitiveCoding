# Finding whether given tree is symmetric (mirror image at vertical line passing through root)
# Link : https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def isSymmetric(n1, n2):
    if not n1 and not n2:
        return True

    if (n1 and n2) and (n1.data == n2.data):
        return (isSymmetric(n1.left, n2.right) and isSymmetric(n1.right, n2.left))
    
    return False


root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 

if isSymmetric(root, root):
    print('Yes')
else:
    print('No')