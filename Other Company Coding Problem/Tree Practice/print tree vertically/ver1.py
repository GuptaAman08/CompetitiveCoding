# An O(n^2) approach 
# Link : https://www.geeksforgeeks.org/print-binary-tree-vertical-order/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def FindMinMax(node, minimum, maximum, hd):

    if node is None:
        return

    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    
    FindMinMax(node.left, minimum, maximum, hd-1)
    FindMinMax(node.right, minimum, maximum, hd+1)


def printVertTree(node, line, hd):

    if node is None:
        return

    if line == hd:
        print(node.data, end=' ')
    
    printVertTree(node.left, line, hd-1)
    printVertTree(node.right, line, hd+1)

def verticalOrder(root):
    if root is None:
        return

    minimum = [0]
    maximum = [0]
    # print(minimum, maximum)
    FindMinMax(root, minimum, maximum, 0)

    for line in range(minimum[0], maximum[0]+1):
        printVertTree(root, line, 0)
        print()

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 

print('Vertical Traversal is :')
verticalOrder(root)