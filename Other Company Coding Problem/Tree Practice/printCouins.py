# Given a Node print all Cousins of that node.
# Link: https://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def findLevel(root, n, cur_level):
    if root is None:
        return 0

    if root.data == n:
        return cur_level
    
    l = findLevel(root.left, n, cur_level+1)
    if l != 0:
        return l

    return findLevel(root.right, n, cur_level+1)



def printAllNodesAtLevel(root, n, cur_level):
    if root is Node or cur_level < 2:
        return
    
    if cur_level == 2:
        if ((root.left and root.left.data == n) or (root.right and root.right.data == n)):
            return

        if root.left:
            print(root.left.data, end=' ')
        
        if root.right:
            print(root.right.data, end=' ')
    else:
        printAllNodesAtLevel(root.left, n, cur_level-1)
        printAllNodesAtLevel(root.right, n, cur_level-1)



def findCousins(root, n):
    if root is None:
        return
    
    # find level of given node n
    level = findLevel(root, n, 1)

    if level != 0:
        # This means node n exist in Tree
        printAllNodesAtLevel(root, n, level)
    else:
        # n dont exist
        return


root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
root.left.right.right = Node(15)  
root.right.left = Node(6)  
root.right.right = Node(7)  
root.right.left.right = Node(8) 

findCousins(root, 2)