'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
import networkx as nx
import matplotlib.pyplot as plt
import random

# Define the graph
small_graph = {'1': [2, 3], '2': [1, 3, 4], '3': [1, 2, 4], '4': [2, 3]}
vertices = ['1','2','3','4']
edges = [['1','3'],['1','2'],['2','3'],['2','4'],['4','3']]

class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self, vertices = set() , edges = list() ) -> None:
        
        self.graph = {}
        
    def add_vertex_edges(self, vertex :str, edges : list):
        '''add a vertex to the graph'''
        self.graph[vertex]  = edges
         
    def contract_edge(self,edge):
        self.

def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('./kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex_edges((line[0]),line[1:])
            
    graph.print_nodes()
    #graph.print_edges()
    #print('Graph constructed')
    #graph.plot_graph('Original Graph')
    #runs = 10000
    #min_cut = []
    #min_cut_graph = Graph()
  
    #for i in range(runs):
     #   min_cut_graph.vertices = graph.vertices.copy()
      #  min_cut_graph.edges = graph.edges.copy()
       # min_cut.append(min_cut_graph.minimum_cut())
    #print(f"ran Minimum cut {len(min_cut)} times and the min cut is {min(min_cut)}")
if __name__ == "__main__":
    main()
