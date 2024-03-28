'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
small_graph = {'1': [2, 3], '2': [1, 3, 4], '3': [1, 2, 4], '4': [2, 3]}


class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self):
        self.vertices = []
        self.edges = []
    def add_vertex(self, vertex):
        '''add a vertex to the graph'''
        if vertex not in self.vertices:
            self.vertices.append(vertex)
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if [vertex1, vertex2] not in self.edges and [vertex2, vertex1] not in self.edges:
                self.edges.append([vertex1, vertex2])
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
    def contract_edge(self, edge):
        '''contract an edge in the graph'''
        '''remove the edge from the list of edges and merge the two vertices into one'''
        '''remove the self loop'''
        '''update the list of edges'''
        '''update the list of vertices'''
        # pop the edge from the list of edges
        removed_edge = self.edges.pop(self.edges.index(edge))
        for edge in self.edges:
            if removed_edge[1] in edge: 
                edge[edge.index(edge[1])] = edge[0]
        
def small_test():
    small_graph = Graph()
    small_graph.add_vertex('1')
    small_graph.add_vertex('2')
    small_graph.add_vertex('3')
    small_graph.add_vertex('4')
    small_graph.add_edge('1', '2')
    small_graph.add_edge('1', '3')
    small_graph.add_edge('2', '3')
    small_graph.add_edge('2', '4')
    small_graph.add_edge('3', '4')
    #small_graph.plot_graph('Small Graph')
    small_graph.print_edges()
    small_graph.contract_edge(['1','3'])
    small_graph.print_edges()
    
    
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex((line[0]))
            for vertex in line[1:]:
                graph.connect((line[0]), int(vertex))
    print('Graph constructed')
    
#if __name__ == "__main__":
#    main()

small_test()    