'''this class implements a graph data structure using an adjacency list representation'''
'''the graph is represented as a dictionary 
where the keys are the vertices and the values are lists of
the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
from Node import Vertex


class Graph(list):
    '''inherits the list, i am sure i am pulling the full API and some are not necessary'''
    def __init__(self, vertices)  :
        self = vertices
        
    def add_vertex(self,vertex : Vertex) -> None:
        self.append(vertex)
        
    def get_vertices(self) -> object:
       return self
    
    def set_vertices(self, vertices : list ) -> None :
        '''sets all the graph in one shot from a list of vertices'''
        self = vertices
    
    def get_vertex(self,)