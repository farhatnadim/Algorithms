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
    def __init__(self, graph = {} ,vertices = set() , edges = list() ) -> None:
        
        self.graph = graph
        
    def add_vertex_edges(self, vertex :str, edges : list):
        '''add a vertex to the graph'''
        self.graph[vertex]  = edges
         
    def reconstruct_edges(self) -> list | list:
        '''gets the edges as list, construct them from the dictionary '''
        edges = []
        lut = [] # maps edges to their vertices
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                edges.append(edge)
                lut.append(vertex)
        return edges, lut
            
    def contract_edge(self,edge_index):
        edges , lut = self.reconstruct_edges()
        edge = edges[edge_index]
        vertex = lut[edge_index]
        new_key = vertex + '-' + str(edge)
        self.graph[new_key] = self.graph[vertex] + self.graph[str(edge)]
        print(self.graph)
        # clean up and removign self reference
        del self.graph[vertex]
        del self.graph[str(edge)]
        for edge in self.graph[new_key]:
           
            if str(edge) in new_key:
               self.graph[new_key].remove(edge)
           
        for vertices in self.graph.keys():
            pass
    def print_vertices(self):
        print(self.graph.key())

def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('./kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex_edges((line[0]),line[1:])
            
    #graph.print_nodes()
    test_graph = Graph(small_graph)
    test_graph.contract_edge(1)
    print(test_graph.graph)
if __name__ == "__main__":
    main()
