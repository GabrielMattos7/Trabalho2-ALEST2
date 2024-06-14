from graph import Graph
class Box:
    def __init__(self, x,y,z):
        dimentions_aux = [int(x), int(y), int(z)]
        self.dimentions = sorted(dimentions_aux) #sort to check the minimum, the middle and the max dimension of the box, made to facilitate the operations

    def get_dimentions(self):
        return self.dimentions
    
    def __str__(self):
        return f"x: {self.dimentions[0]};  y: {self.dimentions[1]};  z: {self.dimentions[2]}\n"

def check_size(Box1, Box2) -> bool:
    """
    Compare if the dimentions are less or equal to the second box
    """
    if (Box1.get_dimentions()[0] <= Box2.get_dimentions()[0] and 
        Box1.get_dimentions()[1] <= Box2.get_dimentions()[1] and  
        Box1.get_dimentions()[2] <= Box2.get_dimentions()[2]):
        return True 
    else: return False


if __name__ == "__main__":
    box_arr = []
    g = Graph()
    with open("casosT10/exemplo.txt") as arq:
        for line in arq:
            x,y,z = line.split()
            box = Box(x,y,z)
            box_arr.append(box)
            # box.print_Box()
                            
        for i, box1 in enumerate(box_arr):
            for j, box2 in enumerate(box_arr):
                # print(str(box1))
                # print(str(box))
                if(check_size(box1,box2)):
                    g.addEdge(i,j) # Vini da uma olhada nisso depois 
                # print(str(box2))