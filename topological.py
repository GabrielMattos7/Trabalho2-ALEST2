from graph import Graph


class Topological:
    def __init__(self, g):
        self.marked = {}
        self.verts = []
        for v in g.getVerts():
            if v not in self.marked:
                self.__dfs(g, v)

    def getTopological(self):
        return self.verts

    def __dfs(self, g, s):
        self.marked[s] = True
        for w in g.getAdj(s):
            if w not in self.marked:
                self.__dfs(g, w)
        self.verts.insert(0, s)


        # Method to find the longest path in the graph
    def longestPath(self, g):
        # Step 1: Topological Sorting
        topo_sorted = self.getTopological()
        print("\n")
        print(topo_sorted)
        print("\n")
        if topo_sorted is None:
            return "Graph is not a DAG; longest path cannot be determined."
        
        # Step 2: Initialize distances
        dist = {v: float('-inf') for v in self.verts}
        dist[topo_sorted[0]] = 0  # Assuming the first in topo sort is the start vertex
        
        # Step 3: Relax edges
        for v in topo_sorted:
            if dist[v] != float('-inf'):
                for neighbor in g.getAdj(v):
                    if dist[neighbor] < dist[v] + 1:
                        dist[neighbor] = dist[v] + 1
        """
        A-> B
        B -> C 
        C -> D
        for v
        when on A, update B, C and D to dist 1
        when on B, update C and D to dist 2
        when on C, update D to dist 3
        so to get on D you must pass throw 3 distances(A,B,C)
        """

        # Step 4: Find the maximum distance
        print(dist.values())
        max_dist = max(dist.values())
        return max_dist