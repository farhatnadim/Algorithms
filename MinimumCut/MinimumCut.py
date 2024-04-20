'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
#import networkx as nx
import matplotlib.pyplot as plt
import random
import os
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
    
    # read input files 
    input_files = [file for file in os.listdir('.') if ('input' in file)]
    output_files = [file.replace('input','output') for file in input_files ]
    results_valid = list()
    results_min_cut = list()
    #for file in input_files:
    file = 'input_random_7_10.txt'
    print("input ",file)
    with open(file) as f:
            for line in f:
                line = line.split()
                for index, element in enumerate(line):
                    if index == 0:
                        for edge in range(0,len(line[1:])): 
                            read_lut.append(element)
                    else:
                        read_edges.append(element)
                        
    cuts = list()
    for run in range(1000000):
            test_graph = Graph(read_edges,read_lut)
            cuts.append((test_graph.minimum_cut()))
    with open(file.replace('input','output')) as f:
        for line in f:
            results_valid.append(line[0])
            print("Validation Results: ",line[0])
    print("My results: ",min(cuts))
    results_min_cut.append(min(cuts))
        
        
        
       
    
if __name__ == "__main__":
    main()



