from python.data_structures.node import Vertex
from python.data_structures.graph import Graph


def main():
    
    number_0 = Vertex([2,4])
    number_1 = Vertex([3])
    number_2 = Vertex([0,4])
    number_3 = Vertex([1])
    number_4 = Vertex([0,2,6,8])
    number_5 = Vertex([7,9])
    number_6 = Vertex([4])
    number_7 = Vertex([5])
    number_8 = Vertex([4])
    number_9 = Vertex([5])
    
    g = Graph()
    g.add_vertex(number_0)
    g.add_vertex(number_1)    
    g.add_vertex(number_2)
    g.add_vertex(number_3)
    g.add_vertex(number_4)
    g.add_vertex(number_5)
    g.add_vertex(number_6)
    g.add_vertex(number_7)    
    g.add_vertex(number_8)
    g.add_vertex(number_9)
   

    g.undirected_connected_components()
    for vertex in g.get_vertices():
        print(f"Connected Components per vertex {vertex.get_connected_components()}")
        
        
if __name__ == "__main__":
    main()