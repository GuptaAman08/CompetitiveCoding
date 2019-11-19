# Link: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# An O(n^2) approach

class Graph:
    def __init__(self, ver):
        self.v = ver
        self.graph = [[0 for x in range(ver)] for x in range(ver)]
    
    def printMST(self, parent):
        print('Resultant MST tree is : ')
        print('Edge' + '\t' + 'Weight')

        for i in range(self.v):
            print(f'{parent[i]}-{i}\t{self.graph[i][parent[i]]}')


    def findMinKey(self, mstSet, dis):
        min_v, ind = float('inf'), -1

        for i in range(self.v):
            if min_v > dis[i] and mstSet[i] == False:
                min_v = dis[i]
                ind = i

        return ind


    def primMST(self):

        # Key values used to pick minimum weight edge in cut 
        dis = [float('inf')] * self.v

        # starting vertex
        dis[2] = 0

        # vertices in mstSet......initially no vertex so all false
        mstSet = [False] * self.v

        # parent array
        parent = [None] * self.v
        parent[2] = -1

        for ver in range(self.v):

            u = self.findMinKey(mstSet, dis)
            mstSet[u] = True

            for all_ng in range(self.v):
                if self.graph[u][all_ng] > 0 and mstSet[all_ng] == False and self.graph[u][all_ng] < dis[all_ng]:
                    dis[all_ng] = self.graph[u][all_ng]
                    parent[all_ng] = u
    
        self.printMST(parent)


g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

g.primMST()
