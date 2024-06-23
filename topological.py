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
        """
        Vai e mcada vertice, pega seus adjacentes e compara se a distancia do adjacente é menor que a do vertice +1
        se for, marca a dist do adj para vertice + 1 
        serve para saber qual o maior caminho possivel a se percorrer 
        """
        for v in self.verts: #v is a node
            if self.distTo[v] == -float('inf'):
                self.distTo[v] = 0

            for w in self.g.getAdj(v): #w is a node 
                if self.distTo[w] < self.distTo[v] + 1: #procura se um outro(possível) caminho de w é menor que o atual caminho(vindo de v)
                    self.distTo[w] = self.distTo[v] + 1
                    self.edgeTo[w] = v

        max_dist = max(self.distTo.values())
        current = None
        for v in self.distTo:
            if self.distTo[v] == max_dist:
                current = v #acha o vertice mais que traz consigo a maior distancia  
                break


        path = []
        while current is not None:
            path.insert(0, current) #adiciona o ultimo ao array
            current = self.edgeTo.get(current) # pega o seu edge

        return len(path), path

