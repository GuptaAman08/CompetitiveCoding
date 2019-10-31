# An O(nlogn) approach 
# Link : https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
# This is correct implementation

from collections import defaultdict, deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def verticalTree(root):
    # Distance to node mapping
    dtn = defaultdict(list)

    # Node to distance mapping
    ntd = defaultdict(int)

    q = deque([])
    
    ntd[root] = 0
    dtn[0].append(root.data)

    q.append(root)

    while q:
        t = q.popleft()

        if t.left:
            q.append(t.left)

            ntd[t.left] = ntd[t] - 1
            dtn[ntd[t.left]].append(t.left.data)

        if t.right:
            q.append(t.right)

            ntd[t.right] = ntd[t] + 1
            dtn[ntd[t.right]].append(t.right.data)

    for key in sorted(dtn):
        print(*dtn[key])

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12) 

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 
# root.right.left = Node(6) 
# root.right.right = Node(7) 
# root.right.left.right = Node(8) 
# root.right.right.right = Node(9) 

verticalTree(root)