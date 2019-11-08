# The following code creates a tree from a given array 
# Link : https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inOrder(root): 

    if root != None: 
        inOrder(root.left) 
        print(root.data,end=" ") 
        inOrder(root.right)  



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
inOrder(root)
