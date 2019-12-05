class disjointSet:
    nodeToref = {}

    # equivalent to make set 
    def __init__(self, key):
        self.parent = self
        self.data = key
        self.rank = 0
    
    @staticmethod
    def findSet(node):
        if node.parent == node:
            return node
        node.parent = disjointSet.findSet(node.parent)
        return node.parent
    
    @staticmethod
    def union(val1, val2):
        n1 = disjointSet.nodeToref[val1] 
        n2 = disjointSet.nodeToref[val2]

        p1 = disjointSet.findSet(n1)
        p2 = disjointSet.findSet(n2)

        if p1 == p2:
            return
        
        if p1.rank > p2.rank:
            p2.parent = p1
        elif p1.rank < p2.rank:
            p1.parent = p2
        else:
            # make anyone as parent and increase rank of the node who is now a parent of other
            p1.rank += 1
            p2.parent = p1

    @staticmethod
    def findRep(n):
        if n.parent == n:
            return n
        return disjointSet.findRep(n.parent)

    @staticmethod
    def addNode(node, val):
        disjointSet.nodeToref[val] = node


n = int(input('Number of elements: '))

# make set
for i in input().split():
    node = disjointSet(int(i))
    disjointSet.addNode(node, int(i))


# Union
t = 1
while t:
    a, b = [int(x) for x in input('Nodes to unite : ').split()]
    print(f'Representatives before union of {a} {b} are :{(disjointSet.findRep(disjointSet.nodeToref[a])).data} {(disjointSet.findRep(disjointSet.nodeToref[b])).data}')
    disjointSet.union(a, b)
    print(f'Representatives before union of {a} {b} are :{(disjointSet.findRep(disjointSet.nodeToref[a])).data} {(disjointSet.findRep(disjointSet.nodeToref[b])).data}')
    t = int(input('To continue press 1 else 0 : '))
    