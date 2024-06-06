'''this class implements a graph data structure using an adjacency list representation'''
'''the graph is represented as a dictionary 
where the keys are the vertices and the values are lists of
the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
from Node import Vertex
from Queue import Queue


class Graph(list):
    '''inherits the list, i am sure i am pulling the full API and some are not necessary'''
    def __init__(self):
        super().__init__()
        
        
    def add_vertex(self,vertex : Vertex) -> None:
        self.append(vertex)
        
    def get_vertices(self) -> object:
       return self
    
    def set_vertices(self, vertices : list ) -> None :
        '''sets all the graph in one shot from a list of vertices'''
        self = vertices
    
    def get_vertex(self,vertex_index : int ) -> Vertex:
        return self[vertex_index]
    
    def delete_vertex(self, vertex_index: int ) ->Vertex:
        vertex = self.pop(vertex_index)
        #Todo : clean up
        
    def merge_vertices(self,vertex_index1 : int , vertex_index_2 :int ) -> None :
        raise NotImplementedError
    
    def bfs( self, vertex_index : int, connected_components = 0) -> None:
        self[vertex_index].set_explored()
        self.distance = 0
        q = Queue()
        q.enqueue(self[vertex_index])
        while (not q.is_empty()):
            v = q.dequeue()
            v.cc = connected_components
            for edge in v.edges:
                if not self[edge].is_explored():
                    self[edge].set_explored()
                    self[edge].distance = v.distance + 1 
                    q.enqueue(self[edge])
    
    def Undirected_Connected_Components(self) -> None :
        numCC = 0
        for vertex in self:
            if  not vertex.is_explored():
                numCC = numCC + 1
                self.bfs(self.index(vertex),numCC)
            