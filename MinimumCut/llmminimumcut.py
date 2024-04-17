'''
write a minimuct function that takes a graph object and returns the minimum cut of the graph
'''

import random

class Graph:
    ''' Implements a graph data structure using an adjacency list representation.
    The graph is represented by a dictionary where keys are vertex identifiers and values
    are sets of vertices that are adjacent to the key vertex. This ensures that there are
    no parallel edges and simplifies management of edges and vertices.
    '''
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        ''' Adds a new vertex to the graph if it doesn't already exist. '''
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()
    
    def add_edge(self, vertex1, vertex2):
        ''' Adds an edge between two vertices in the graph, and adds the vertices to the graph if they are not already present. '''
        if vertex1 != vertex2:  # This check avoids adding self-loops
            for v1, v2 in (vertex1, vertex2), (vertex2, vertex1):
                self.add_vertex(v1)
                self.adjacency_list[v1].add(v2)
    
    def contract_edge(self, vertex1, vertex2):
        ''' Merges two connected vertices into a single vertex and removes self-loops. '''
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            return  # One of the vertices does not exist
        
        # Merge vertex2 into vertex1 and update adjacency list
        new_edges = self.adjacency_list[vertex1].union(self.adjacency_list[vertex2])
        new_edges.discard(vertex1)
        new_edges.discard(vertex2)
        
        # Remove vertex2 from all connected vertices
        for vertex in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex].remove(vertex2)
            if vertex != vertex1:  # Avoid adding a self-loop
                self.adjacency_list[vertex].add(vertex1)
        
        # Finalize changes by updating the adjacency list
        self.adjacency_list[vertex1] = new_edges
        del self.adjacency_list[vertex2]
    
    def minimum_cut(self):
        ''' Attempts to compute the minimum cut of the graph using Karger's algorithm. '''
        while len(self.adjacency_list) > 2:
            vertex1 = random.choice(list(self.adjacency_list.keys()))
            vertex2 = random.choice(list(self.adjacency_list[vertex1]))
            self.contract_edge(vertex1, vertex2)
        
        # Calculate the number of edges crossing the two remaining vertices
        remaining_vertices = list(self.adjacency_list.keys())
        return len(self.adjacency_list[remaining_vertices[0]])

### Example Usage
# Initialize the graph
graph = Graph()

# Adding vertices and edges
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('A', 'D')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('F', 'D')

# Compute the minimum cut
min_cut = graph.minimum_cut()
print("Minimum cut of the graph:", min_cut)
