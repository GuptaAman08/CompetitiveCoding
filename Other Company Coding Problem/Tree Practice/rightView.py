# Right view of a tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def rightView(node, cur, max_level_reached):
    if node is None:
        return
    
    if cur > max_level_reached[0]:
        print(node.data, end=' ')
        max_level_reached[0] = cur
    
    rightView(node.right, cur+1, max_level_reached)
    rightView(node.left, cur+1, max_level_reached)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)


rightView(root, 1, [0])