# Link :  https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

class Graph:
    def __init__(self, V):
        self.v = V
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # uses path compression
    def findSet(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.findSet(parent, parent[i])
        return parent[i]


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


    def kruskalMST(self):
        res = []
        cur_ind, mst_edg = 0, 0

        self.graph.sort(key = lambda x: x[2])

        # initialize rank and parent sets
        rank = [0] * self.v
        parent = list(range(self.v))

        # edges in mst are less than V-1 do following
        while mst_edg < self.v - 1:
            u, v, w = self.graph[cur_ind]

            if self.findSet(parent ,u) != self.findSet(parent ,v):
                mst_edg += 1
                self.union(u, v, parent, rank)
                res.append([u,v,w])

            cur_ind += 1

        print('Minimum spanning tree is : ')
        for u, v, w in res:
            print(str(u) + '-->' + str(v) + ' by wt ' + str(w))


g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.kruskalMST()
