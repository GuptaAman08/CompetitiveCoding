class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def findPath(root, n1, p):
    if root is None:
        return False

    if root.data == n1:
        p.append(root.data)
        return True

    if findPath(root.left, n1, p):
        p.append(root.data)
        return True
    
    if findPath(root.right, n1, p):
        p.append(root.data)
        return True
    
    return False

def LCA(root, n1, n2):
    p1 = []
    p2 = []

    if not findPath(root, n1, p1) or not findPath(root, n2, p2):
        return 'No Common Ancestor'

    p1.reverse()
    p2.reverse()

    i = 0
    a = len(p1)
    b = len(p2)
    while i < a and i < b:
        if p1[i] != p2[i]:
            break
        i += 1
    
    return p1[i-1]

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

n1, n2 = [int(x) for x in input().split()]
print(f'LCA of {n1} and {n2} is {LCA(root, n1, n2)}')