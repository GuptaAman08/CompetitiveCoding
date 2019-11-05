# Bottom view of a binary tree

from collections import defaultdict, deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def bottomView(node):
    if node is None:
        return

    # dist to node mapping
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
            else:
                d[dist-1][0] = n.left.data

            q.append([n.left, dist-1])

        if n.right:
            if d[dist+1] == []:
                d[dist+1].append(n.right.data)
            else:
                d[dist+1][0] = n.right.data

            q.append([n.right, dist+1])


    min_val, max_val = float('inf'), float('-inf') 
    for key in d.keys():
        if min_val > key:
            min_val = key

        if max_val < key:
            max_val = key

    
    for i in range(min_val, max_val+1):
        print(*d[i], end=' ')


root = Node(20); 
root.left = Node(8); 
root.right = Node(22); 
root.left.left = Node(5); 
root.left.right = Node(3); 
root.right.left = Node(4); 
root.right.right = Node(25); 
root.left.right.left = Node(10); 
root.left.right.right = Node(14); 

bottomView(root)