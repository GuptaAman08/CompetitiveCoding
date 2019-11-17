# Detect Cycle in Graph using DisJoint Set DS.

class Graph:
    def __init__(self, V):
        self.v = V
        self.graph = []


    def addEdge(self, u, v):
        self.graph.append([u, v])

    # uses path compression
    def findSet(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.findSet(parent, parent[i])
        return parent[i]

    # Union by Rank 
    def union(self, u, v, parent, rank):
        p1 = self.findSet(parent, u)
        p2 = self.findSet(parent, v)

        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p2] > rank[p1]:
            parent[p1] = p2
        else:
            rank[p1] += 1
            parent[p2] = p1


    def DetectCycle(self):
        cur_ind = 0
        l = len(self.graph)

        # initialize rank and parent sets
        rank = [0] * self.v
        parent = list(range(self.v))

        # edges in mst are less than V-1 do following
        flag = True
        while flag and cur_ind < l:
            u, v = self.graph[cur_ind]
            if self.findSet(parent, u) != self.findSet(parent, v):
                self.union(u, v, parent, rank)
            else:
                flag = False
            cur_ind += 1

        if flag:
            print('Graph has no cycles')
        else:
            print('Graph has a cycle')


g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
g1.DetectCycle()
