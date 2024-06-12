from Node import Vertex
from Queue import Queue
from Stack import Stack
import graphviz

class Graph(list):
    def __init__(self):
        super().__init__()

    def add_vertex(self, vertex: Vertex) -> None:
        self.append(vertex)
        
    def get_vertices(self) -> list:
        return self
    
    def set_vertices(self, vertices: list) -> None:
        self.clear()
        self.extend(vertices)
    
    def get_vertex(self, vertex_index: int) -> Vertex:
        return self[vertex_index]
    
    def delete_vertex(self, vertex_index: int) -> Vertex:
        vertex = self.pop(vertex_index)
        # TODO: Clean up references to this vertex in other vertices' edges
        return vertex
    
    def merge_vertices(self, vertex_index1: int, vertex_index2: int) -> None:
        raise NotImplementedError
    
    def bfs(self, vertex_index: int, connected_components=0) -> None:
        self[vertex_index].set_explored()
        self[vertex_index].distance = 0
        q = Queue()
        q.enqueue(self[vertex_index])
        while not q.is_empty():
            v = q.dequeue()
            v.cc = connected_components
            for edge in v.edges:
                if not self[edge].is_explored():
                    self[edge].set_explored()
                    self[edge].distance = v.distance + 1
                    q.enqueue(self[edge])
    
    def undirected_connected_components(self) -> None:
        num_cc = 0
        for vertex in self:
            if not vertex.is_explored():
                num_cc += 1
                self.bfs(self.index(vertex), num_cc)
    
    def dfs(self) -> None:
        s = Stack()
        s.push(self[0])
        while not s.is_empty():
            v = s.pop()
            if not v.is_explored():
                v.set_explored()
                for edge in v.edges:
                    s.push(self[edge])
    
    def dfs_recursive(self, vertex: Vertex) -> None:
        vertex.set_explored()
        for edge in vertex.edges:
            if not self[edge].is_explored():
                self.dfs_recursive(self[edge])
    
    def topological_sort(self) -> None:
        def dfs_recursive(vertex: Vertex, current_label: list) -> None:
            vertex.set_explored()
            for edge in vertex.edges:
                if not self[edge].is_explored():
                    dfs_recursive(self[edge], current_label)
            vertex.current_label = current_label[0]
            current_label[0] -= 1
        
        current_label = [len(self)]
        for vertex in self:
            if not vertex.is_explored():
                dfs_recursive(vertex, current_label)
    
    def graph_reversal(self) -> list:
        reversed_graph = [Vertex(edges=[]) for _ in range(len(self))]
        for vertex in self:
            for edge in vertex.edges:
                reversed_graph[edge].add_edge(self.index(vertex))
                reversed_graph[edge].label = str(edge + 1)
        return reversed_graph

    def print_graph(self, graph_type='Digraph'):
        if graph_type == 'Digraph':
            dot = graphviz.Digraph(format='svg')
        else:
            dot = graphviz.Graph(format='svg')
        for node in self:
            dot.node(name=str(id(node)), label=node.label)
            for edge in node.edges:
                dot.edge(str(id(node)), str(id(self[edge])))
        dot.render('graph', view=True)
