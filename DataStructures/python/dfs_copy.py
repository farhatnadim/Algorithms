class Vertex:
    def __init__(self, id):
        self.id = id
        self.explored = False
        self.edges = []
    
    def add_edge(self, vertex):
        self.edges.append(vertex)
    
    def is_explored(self):
        return self.explored
    
    def set_explored(self, value: bool):
        self.explored = value

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, id):
        self.vertices[id] = Vertex(id)
    
    def get_vertex(self, id):
        return self.vertices.get(id)
    
    def add_edge(self, from_id, to_id):
        if from_id in self.vertices and to_id in self.vertices:
            self.vertices[from_id].add_edge(to_id)

    def topological_sort(self):
        def dfs_recursive(graph: 'Graph', vertex: 'Vertex', topological_order: list) -> None:
            vertex.set_explored(True)
            for edge_id in vertex.edges:
                edge_vertex = graph.get_vertex(edge_id)
                if not edge_vertex.is_explored():
                    dfs_recursive(graph, edge_vertex, topological_order)
            topological_order.append(vertex.id)
        
        topological_order = []
        for vertex_id, vertex in self.vertices.items():
            if not vertex.is_explored():
                dfs_recursive(self, vertex, topological_order)
        
        # Reverse to get the correct topological order
        topological_order.reverse()
        print("Topological Sort Order:", topological_order)
        return topological_order

# Example usage:
graph = Graph()
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('1', '2')
graph.add_edge('1', '3')
graph.add_edge('2', '4')
graph.add_edge('3', '4')

topological_order = graph.topological_sort()
