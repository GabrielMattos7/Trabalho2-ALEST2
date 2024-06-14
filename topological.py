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