class Graph:
    def __init__(self, *args):
        self.graph = {}
        self.vertices = set()
        if len(args) == 1:
            self.__readFromFile(args[0])

    def addEdge(self, v, w):
        self.addToList(v, w)
        #self.addToList(w, v) grafo direcionado nao cria o inverso

    def getAdj(self, v):
        return self.graph[v] if v in self.graph else []

    def getVerts(self):
        return self.vertices

    def toDot(self):
        edges = set()
        NEWLINE = '\n'
        sb = "digraph {" + NEWLINE
        sb += "rankdir = LR;" + NEWLINE
        sb += "node [shape = circle];" + NEWLINE
        for v in sorted(self.getVerts()):
            for w in self.getAdj(v):
                edge = f"{v}->{w}"
                if edge not in edges:
                    sb += f"{v} -> {w}" + NEWLINE
                    edges.add(edge)
        sb += "}" + NEWLINE
        return sb
    
    def addToList(self, v, w):
        list = self.graph[v] if v in self.graph else []
        list.append(w)
        self.graph[v] = list
        self.vertices.add(v)
        self.vertices.add(w)

    def __readFromFile(self, filename):
        with open(filename) as arq:
            for line in arq:
                verts = line[:-1].split()
                self.addEdge(verts[0], verts[1])