from graph import Graph
from topological import Topological
class Box:
    def __init__(self, x,y,z):
        dimentions_aux = [int(x), int(y), int(z)]
        self.dimentions = sorted(dimentions_aux) #sort to check the minimum, the middle and the max dimension of the box, made to facilitate the operations

    def get_dimentions(self):
        return self.dimentions
    
    def __str__(self):
        formatted_str = f"{self.dimentions[0]}, {self.dimentions[1]}, {self.dimentions[2]}"
        return formatted_str

def check_size(Box1, Box2) -> bool:
    """
    Compare if the dimentions are less or equal to the second box
    """
    if (Box1.get_dimentions()[0] < Box2.get_dimentions()[0] and 
        Box1.get_dimentions()[1] < Box2.get_dimentions()[1] and  
        Box1.get_dimentions()[2] < Box2.get_dimentions()[2]):
        return True 
    else: return False


if __name__ == "__main__":
    box_arr = []
    g = Graph()
    with open("casosT10/teste10.txt") as arq:
        for line in arq:

            x,y,z = line.split()
            box = Box(x,y,z)
            box_arr.append(box)
                       
    for i, box1 in enumerate(box_arr):
        for j, box2 in enumerate(box_arr):
            if i!= j and check_size(box1,box2): # verificar se nao sao iguais
                g.addEdge(box1.__str__(),box2.__str__())
    
    grafo_topo = Topological(g)

    print("\n")
    with open("todot.txt", "w") as file:
        file.write((g.toDot()))
    dist, path = grafo_topo.longestPath()
    print(dist)
    print(path)