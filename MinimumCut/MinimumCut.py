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
    def __init__(self):
        self.vertices = set()
        self.edges = []
    # copy contructor
   
    def add_vertex(self, vertex :str):
        '''add a vertex to the graph'''
        self.vertices.add(vertex)   
    def add_edge(self, vertex1 : str, vertex2 :str):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            edge = [vertex1, vertex2]
            if edge != all({v1, v2} != edge for v1, v2 in self.edges):
                self.edges.append((vertex1, vertex2))
    def plot_graph(self, title : str) -> None : 
        # Create a new graph
        G = nx.Graph()
    # Add nodes and edges
        for node in self.vertices:
            G.add_node(node)
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])
        plt.figure(figsize=(5, 4))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)
        plt.title(title, fontsize=20)
        plt.show()
        
    def print_nodes(self) -> None:
        print('Vertices: ', self.vertices)
    def print_edges(self) -> None:
        print('Edges: ', self.edges)
    def contract_edge(self, edge : str):
        '''contract an edge in the graph'''
        '''remove the edge from the list of edges and merge the two vertices into one'''
        '''remove the self loop'''
        '''update the list of edge5.s'''
        '''update the list of vertices'''
        # pop the edge from the list of edges
        
        removed_edge = self.edges.pop(self.edges.index(edge))
        node = self.vertices.pop(self.vertices.index(removed_edge[1]))
        for edge in self.edges:
            if removed_edge[1] in edge: 
                edge[edge.index(removed_edge[1])] = removed_edge[0]
        for edge in self.edges :
            if edge[0] == edge[1]:
                self.edges.pop(self.edges.index(edge))
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

  