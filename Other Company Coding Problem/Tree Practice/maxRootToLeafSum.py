# Print maximum root to leaf sum value as well as print corresponding path
# Link: https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def findLeaf(root, max_sum, cur_sum):
    if root is None:
        return None

    cur_sum += root.data
    if root.left is None and root.right is None:
        if cur_sum > max_sum[0]:
            max_sum[0] = cur_sum

    findLeaf(root.left, max_sum, cur_sum)
    findLeaf(root.right, max_sum, cur_sum)


def printMaxSumPath(root, max_sum):
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        if root.data == max_sum:
            print(root.data, end=' ')
            return True
        else:
            return False
    
    if printMaxSumPath(root.left, max_sum - root.data):
        print(root.data, end=' ')
        return True

    if printMaxSumPath(root.right, max_sum - root.data):
        print(root.data, end=' ')
        return True
    
    return False


def findMaxRootToLeafSum(root):
    if root is None:
        return
    
    max_sum = [float('-inf')]

    # find leaf node comprising max sum
    findLeaf(root, max_sum, 0)
    print(f'Maximum sum from root to leaf:  {max_sum[0]}')

    # print the path comprising maximum sum from root to leaf 
    print(f'Maximum sum root to leaf path is: ', end=' ')
    printMaxSumPath(root, max_sum[0])


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(8)
# root.left.right = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.left.right.left = Node(10)
# root.right.left.left = Node(7)
# root.right.left.right = Node(9)
# root.right.right.right = Node(5)

root = Node(10) 
root.left = Node(-2) 
root.right = Node(7) 
root.left.left = Node(8) 
root.left.right = Node(-4) 

findMaxRootToLeafSum(root)