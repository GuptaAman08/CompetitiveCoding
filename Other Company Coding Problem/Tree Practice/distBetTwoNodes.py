# find distance betweem two nodes in binary tree

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def findLCA(root, n1, n2):
    if root is None:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    left = findLCA(root.left, n1, n2)
    right = findLCA(root.right, n1, n2)

    if left is not None and right is not None:
        return root
    else:
        return left if left else right

# finds distance between lca and node with value n
def findDist(lca, n, d, cur_level):
    if lca is None:
        return

    if lca.data == n:
        d.append(cur_level)
        return
    
    findDist(lca.left, n, d, cur_level+1)
    findDist(lca.right, n, d, cur_level+1)


root = Node(20); 
root.left = Node(8); 
root.right = Node(22); 
root.left.left = Node(5); 
root.left.right = Node(3); 
root.right.left = Node(4); 
root.right.right = Node(25); 
root.left.right.left = Node(10); 
root.left.right.right = Node(14); 


lca = findLCA(root, 10, 8) 
if lca:
    d1 = []
    d2 = []

    findDist(lca, 10, d1, 0)
    findDist(lca, 8, d2, 0)
    print(f'Distance between nodes is: {d1[0] + d2[0]}')
else:
    print('There exist no lowest common ancestor')