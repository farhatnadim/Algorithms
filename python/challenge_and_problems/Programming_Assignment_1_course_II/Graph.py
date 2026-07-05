from Node import Vertex
import graphviz
import Queue
import Stack
class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices.append(vertex)
        
    def get_vertices(self) -> list:
        return self.vertices
    
    def set_vertices(self, vertices: list) -> None:
        self.vertices = vertices
    
    def get_vertex(self, vertex_index: int) -> Vertex:
        return self.vertices[vertex_index]
    
    def delete_vertex(self, vertex_index: int) -> Vertex:
        vertex = self.vertices.pop(vertex_index)
        # TODO: Clean up references to this vertex in other vertices' edges
        return vertex
    
    def merge_vertices(self, vertex_index1: int, vertex_index2: int) -> None:
        raise NotImplementedError
    
    def bfs(self, vertex_index: int, connected_components=0) -> None:
        self.vertices[vertex_index].set_explored()
        self.vertices[vertex_index].distance = 0
        q = Queue()
        q.enqueue(self.vertices[vertex_index])
        while not q.is_empty():
            v = q.dequeue()
            v.cc = connected_components
            for edge in v.edges:
                if not self.vertices[edge].is_explored():
                    self.vertices[edge].set_explored()
                    self.vertices[edge].distance = v.distance + 1
                    q.enqueue(self.vertices[edge])
    
    def undirected_connected_components(self) -> None:
        num_cc = 0
        for vertex in self.vertices:
            if not vertex.is_explored():
                num_cc += 1
                self.bfs(self.vertices.index(vertex), num_cc)
    
    def dfs(self) -> None:
        s = Stack()
        s.push(self.vertices[0])
        while not s.is_empty():
            v = s.pop()
            if not v.is_explored():
                v.set_explored()
                for edge in v.edges:
                    s.push(self.vertices[edge])
    
    def dfs_recursive(self, vertex: Vertex) -> None:
        vertex.set_explored()
        for edge in vertex.edges:
            if not self.vertices[edge].is_explored():
                self.dfs_recursive(self.vertices[edge])
    
    def topological_sort(self) -> None:
        def dfs_recursive(graph: Graph, vertex: Vertex, current_label: list) -> None:
            vertex.set_explored(True)
            for edge in vertex.edges:
                if not graph.get_vertex(edge).is_explored():
                    dfs_recursive(graph, graph.get_vertex(edge), current_label)
            vertex.currentLabel = current_label[0]
            current_label[0] -= 1

        current_label = [len(self.vertices)]
        for vertex in (self.vertices): #reversed(self.vertices)
            if not vertex.is_explored():
                dfs_recursive(self, vertex, current_label)

        # Reset exploration status for future operations
        for vertex in self.vertices:
            vertex.set_explored(False)
    
    def reversal(self) -> 'Graph':
        reversed_graph = Graph()
        for _ in range(len(self.vertices)):
            reversed_graph.add_vertex(Vertex(edges=[]))

        for vertex in self.vertices:
            for edge in vertex.edges:
                reversed_graph.get_vertex(edge).add_edge(self.vertices.index(vertex))
                reversed_graph.get_vertex(edge).label = str(edge + 1)

        return reversed_graph

    
    def kosraju(self, vertex: Vertex) -> None:
           '''Limitations : Assumes that vertices are sorted in the descending order
                     Assumes no missing vertex'''
        def dfs_recursive(graph :'Graph', vertex: Vertex) -> None:
            vertex.set_explored(True)
            vertex.scc = numSCC[0]
            for edge in vertex.edges:
                if not graph.get_vertex(edge).is_explored():
                    dfs_recursive(graph, graph.get_vertex(edge))
        
        r_g = self.reversal()
        r_g.topological_sort()
        
        temp_graph = Graph()
        temp_graph.vertices = [None]*len(r_g.vertices)
        for v1,v2 in zip(r_g.vertices,self.vertices):
            temp_graph.vertices[v1.currentLabel-1] = v2
            
        numSCC = [0]
        for vertex in (temp_graph.vertices): 
            if not vertex.is_explored():
                numSCC[0] = numSCC[0] + 1
                dfs_recursive(self, vertex)

        # Reset exploration status for future operations
        for vertex in self.vertices:
            vertex.set_explored(False)
    
        
    
    def print_graph(self, graph_type='Digraph'):
        if graph_type == 'Digraph':
            dot = graphviz.Digraph(format='svg')
        else:
            dot = graphviz.Graph(format='svg')
        for node in self.vertices:
            dot.node(name=str(id(node)), label=node.label + "-" + str(node.currentLabel))
            for edge in node.edges:
                dot.edge(str(id(node)), str(id(self.vertices[edge])))
        dot.render('graph', view=True)
        
        
    