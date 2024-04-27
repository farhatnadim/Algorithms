'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''

import random
import os

class Graph (dict):
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a a dictionary where the keys are the vertices and the values are the edges'''
    def __init__(self) -> None:
        super().__init__()
    def add_vertex(self,vertex : str, edges = set()) -> None:
        '''add a vertex to the graph'''
        if vertex not in self:
            self[vertex] = edges
    def add_edge(self,vertex1,vertex2) -> None:
        '''add an edge to the graph'''
        self[vertex1].add(vertex2)
        self[vertex2].add(vertex1)
    
    def contract_edge(self,edge_index : int) -> int:
        pass
    def minimum_cut(self):
        '''return the minimum cut of the graph'''
        len_vertices = len(self.vertices)
        len_edges = len(self.edges)
        while (len_vertices) > 2:
            edge_index = random.randint(0,(len_edges)-1)
            self_loops = self.contract_edge(edge_index) 
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    
    
    # read input files 
    input_files = [file for file in os.listdir('.') if ('input' in file)]
    
    #for file in input_files:
    base_dir = os.getcwd()
    mincut_folder = 'MinimumCut'
    mincut_folder = ''
    file = 'input_random_1_6.txt'
    file = os.path.join(base_dir,mincut_folder,file)
    print("input ",file)
    g = Graph()
    
    with open(file) as f:
            for line in f:
                line = line.split()
                g[line[0]] = line[1:]
    print(len(g.keys()))
    
                       
    for run in range(2):
        test_graph = Graph()
        
    result = ''    
    with open(file.replace('input','output')) as f:
        for line in f:
            result = line[0]
    print(result)   
    keys_index = random.randint(0,len(g.keys())-1)
    edge_index = random.randint(0,len(g[str(keys_index)])-1)
    print(g[str(keys_index)][edge_index])    
        
        
       
    
if __name__ == "__main__":
    main()



