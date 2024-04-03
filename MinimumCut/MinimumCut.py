'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
import networkx as nx
import matplotlib.pyplot as plt
import random

# Define the graph
small_graph = {'1': [2, 3], '2': [1, 3, 4], '3': [1, 2, 4], '4': [2, 3]}


class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self, vertices = set() , edges = set() ) -> None:
        
        self.vertices = vertices
        self.edges = edges
    
    def add_vertex(self, vertex :str):
        '''add a vertex to the graph'''
        self.vertices.add(vertex)  
         
    def add_edge(self, vertex1 : str, vertex2 :str):
        '''add an edge to the graph'''
        '''an edge is represented by a tuple of two vertices'''
        '''no parallel edges are allowed'''
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if (vertex1, vertex2) not in self.edges and (vertex2, vertex1) not in self.edges:
                self.edges.append((vertex1, vertex2))
            
    def plot_graph(self, title : str) -> None:
        '''plot the graph using Andrey Karpathy's code'''
        pass
    
        
    def print_nodes(self) -> None:
        print('Vertices: ', self.vertices)
    def print_edges(self) -> None:
        print('Edges: ', self.edges)
    def contract_edge(self, edge_to_remove : list):
        '''contract an edge in the graph'''
        '''remove the edge from the list of edges and merge the two vertices into one'''
        '''remove the self loop'''
        '''update the list of edges'''
        '''update the list of vertices'''
        # pop the edge from the list of edges
        edges_copy = self.edges.copy()
        vertices_copy = self.vertices.copy()
        edges_copy.remove(edge)
        for edge in self.edges:
            if any([ vertice for vertice in edge if vertice == edge_to_remove[1]]):
                edge = [edge_to_remove[0] if vertice == edge_to_remove[1] else vertice for vertice in edge]
                
    def minimum_cut(self) -> int :
        '''randomly contract edges in the graph'''
        while (len(self.vertices) > 2):
            self.contract_edge(self.edges[random.randint(0, len(self.edges)-1)])
        return len(self.edges)


def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex((line[0]))
            for vertex in line[1:]:
                graph.add_edge((line[0]), vertex)
    graph.print_nodes()
    graph.print_edges()
    print('Graph constructed')
    graph.plot_graph('Original Graph')
    print(graph.minimum_cut())
    
if __name__ == "__main__":
    main()

  