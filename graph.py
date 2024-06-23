class Graph:
    def __init__(self, *args):
        self.graph = {}
        self.vertices = set()
        if len(args) == 1:
            self.__readFromFile(args[0])

    def addEdge(self, v, w):
        self.addToList(v, w)
        # self.addToList(w, v)  # Comentado para manter o grafo direcionado

    def getAdj(self, v):
        return self.graph[v] if v in self.graph else []

    def getVerts(self):
        return self.vertices

    def toDot(self):
        edges = set()
        NEWLINE = '\n'
        sb = "digraph {" + NEWLINE
        sb += "node [shape = circle];" + NEWLINE
        for v in sorted(self.getVerts()):
            for w in self.getAdj(v):
                edge = f"{v}->{w}"
                if edge not in edges:
                    sb += f'"{v}" -> "{w}"' + NEWLINE
                    edges.add(edge)
        sb += "}" + NEWLINE
        return sb

    def addToList(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)
        self.vertices.add(v)
        self.vertices.add(w)

    def __readFromFile(self, filename):
        try:
            with open(filename, 'r') as arq:
                for line in arq:
                    verts = line.strip().split()
                    if len(verts) == 2:
                        self.addEdge(verts[0], verts[1])

                    else:
                        print(f"Warning: Line in file '{filename}' does not contain exactly 2 vertices: {line.strip()}")
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")

    def longestPath(self, g):
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