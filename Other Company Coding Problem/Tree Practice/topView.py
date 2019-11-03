# Top view of a tree
# IN O(n) time
from collections import defaultdict, deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def topView(node):
    if node is None:
        return

    d = defaultdict(list)
    q = deque()

    # node and horizontal distance
    q.append([node, 0])
    d[0].append(node.data)
    while q:
        temp = q.popleft()
        n, dist = temp
        if n.left:
            if d[dist-1] == []:
                d[dist-1].append(n.left.data)

            q.append([n.left, dist-1])

        if n.right:
            if d[dist+1] == []:
                d[dist+1].append(n.right.data)

            q.append([n.right, dist+1])


    min_val, max_val = float('inf'), float('-inf') 
    for key in d.keys():
        if min_val > key:
            min_val = key

        if max_val < key:
            max_val = key

    
    for i in range(min_val, max_val+1):
        print(*d[i], end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

topView(root)