from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def isComplete(root):
    if root is None:
        return True
    
    q = deque()
    q.append(root)
    flag = False

    while q:
        temp = q.popleft()

        if flag:
            if temp.left or temp.right:
                return False
        else:
            if (temp.left is None) and (temp.right is None):
                flag = True
            elif temp.left and temp.right:
                q.append(temp.left)
                q.append(temp.right)
            elif temp.left and not temp.right:
                flag = True
                q.append(temp.left)
            else:
                return False

    return True

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


if isComplete(root):
    print('Given Tree is a complete binary tree')
else:
    print('Given Tree is not a complete binary tree')