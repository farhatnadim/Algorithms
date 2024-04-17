'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
#import networkx as nx
import matplotlib.pyplot as plt
import random

# remove edge '1' 



class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self, edges = list() , lut = list()) -> None:
        self.edges = edges
        self.lut = lut
        self.vertices = set(lut)
        
    def add_vertex_edges(self, vertex :str, edges : list):
        '''add a vertex to the graph'''
        pass
            
    def contract_edge(self,edge_index):
        lut_temp = self.lut.copy()
        edges_temp = self.edges.copy()
        node1 = lut_temp.pop(edge_index)
        node2 = edges_temp.pop(edge_index)
        for index, element in enumerate(lut_temp):
            if lut_temp[index] == node1 or lut_temp[index] == node2:
                lut_temp[index] = node1 + '-' + node2
            if edges_temp[index] == node1 or edges_temp[index] == node2:
                edges_temp[index] = node1 + '-' + node2
        for index, element in enumerate(lut_temp):
            if edges_temp[index] == lut_temp[index]:
                edges_temp.pop(index) 
                lut_temp.pop(index)  
        self.edges= edges_temp
        self.lut = lut_temp
        self.vertices = set(self.lut)
        
    def minimum_cut(self):
        '''return the minimum cut of the graph'''
        while len(self.vertices) > 2:
            edge_index = random.randint(0,len(self.edges)-1)
            self.contract_edge(edge_index)
        return len(self.edges)//2
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    read_edges = list()
    read_lut = list()   
    with open('./kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            for index, element in enumerate(line):
                   read_lut.append(element[0])
                   read_edges.append(element)
          
    #print(read_edges)
    #print(read_lut)
    #graph.print_nodes()
    lut_orignal  = ['1','1','1','2','2','3','3','4','4','4']
    edges_orignal = ['3','2','4','1','4','1','4','1','2','3']
    test_graph = Graph(edges_orignal,lut_orignal)
    print(test_graph.minimum_cut())
    #print(g.edges)
    #print(g.lut)
if __name__ == "__main__":
    main()



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
