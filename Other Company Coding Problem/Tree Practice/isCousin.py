# To find whether two given nodes are cousins
# link: https://www.techiedelight.com/determine-two-nodes-are-cousins/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inOrder(root, parent, cur_level, a, b):
    if root is None:
        return
    
    inOrder(root.left, root, cur_level+1, a, b)

    if root.data == a[0]:
        a[1] = cur_level
        a[2] = parent
        
    if root.data == b[0]:
        b[1] = cur_level
        b[2] = parent

    inOrder(root.right, root, cur_level+1, a, b)



def isCousin(root, n1, n2):
    if root is None:
        return False

    a = [n1, 1, None]
    b = [n2, 1, None]

    inOrder(root, None, 1, a, b)
    if a[1] != b[1] or a[2] == b[2]:
        return False
    else:
        return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if isCousin(root, 1, 6):
    print(f'They are Cousin of each other')
else:
    print(f'They are not Cousin of each other')