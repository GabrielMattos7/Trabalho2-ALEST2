from graph import Graph

class Topological:
    def __init__(self, g):
        self.g = g
        self.marked = {}
        self.verts = []
        self.distTo = {}
        self.edgeTo = {}

        # Initialize distTo to negative infinity
        for v in self.g.getVerts():
            self.distTo[v] = -float('inf')

        for v in g.getVerts():
            if v not in self.marked:
                self.__dfs(v)

    def getTopological(self):
        return self.verts

    def __dfs(self, s):
        self.marked[s] = True
        for w in self.g.getAdj(s):
            if w not in self.marked:
                self.__dfs(w)
        self.verts.insert(0, s)

    def longestPath(self):
        for v in self.verts:
            if self.distTo[v] == -float('inf'):
                self.distTo[v] = 0

            for w in self.g.getAdj(v):
                if self.distTo[w] < self.distTo[v] + 1:
                    self.distTo[w] = self.distTo[v] + 1
                    self.edgeTo[w] = v

        max_dist = max(self.distTo.values())
        max_vertex = None
        for v in self.distTo:
            if self.distTo[v] == max_dist:
                max_vertex = v
                break

        if max_vertex is None:
            return None, None

        path = []
        current = max_vertex
        while current is not None:
            path.insert(0, current)
            current = self.edgeTo.get(current)

        return max_dist, path

