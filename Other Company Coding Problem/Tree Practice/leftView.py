# Left view of a tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def leftView(node, cur, max_level_reached):
    if node is None:
        return
    
    if cur > max_level_reached[0]:
        print(node.data, end=' ')
        max_level_reached[0] = cur
    
    leftView(node.left, cur+1, max_level_reached)
    leftView(node.right, cur+1, max_level_reached)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

leftView(root, 1, [0])