'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
#import networkx as nx
import matplotlib.pyplot as plt
import random

# Define the graph
lut  = ['1','1','1','2','2','3','3','4','4','4']
edges = ['3','2','4','1','4','1','4','1','2','3']

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
        lut_temp = lut.copy()
        edges_temp = edges.copy()
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
        return edges_temp,lut_temp
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('./kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex_edges((line[0]),line[1:])
            
    #graph.print_nodes()
    lut_orignal  = ['1','1','1','2','2','3','3','4','4','4']
    edges_orignal = ['3','2','4','1','4','1','4','1','2','3']
    test_graph = Graph(edges_orignal,lut_orignal)
    edges, lut = test_graph.contract_edge(0)
    g = Graph(edges,lut)
    edges, lut = g.contract_edge(0)
    g = Graph(edges,lut)
    print(g.edges)
    print(g.lut)
if __name__ == "__main__":
    main()
