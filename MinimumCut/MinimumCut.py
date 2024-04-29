'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''

import random
import os

class Graph (dict):
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a a dictionary where the keys are the vertices and the values are the edges'''
    def __init__(self) -> None:
        super().__init__()
    
    def add_vertex(self,vertex : str, edges = list()) -> None:
        '''add a vertex to the graph'''
        if vertex not in self:
            self[vertex] = edges
    
    def select_edge_random(self) -> tuple:
        keys_index = random.randint(1,len(self.keys()))
        edge_index = random.randint(0,len(self[str(keys_index)])-1)
        return (str(keys_index),str(edge_index+1))
    
    def merge_vertex(self, vertex1:str, vertex2:str) -> None:
        
        self[vertex1] =  self[vertex1] + self[vertex2]
        del self[vertex2]
        
    def remove_self_loops(self,vertex1:str, vertex2:str) -> list:
        #new_edges =
        pass
    def add_edge(self,vertex1,vertex2) -> None:
        '''add an edge to the graph'''
        self[vertex1].add(vertex2)
        self[vertex2].add(vertex1)
    
def main():
        '''read graph from file and contstruct a graph object'''
        graph = Graph()
        # read input files 
        #input_files = [file for file in os.listdir('.') if ('input' in file)]
    
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
        print(g)
        (v1,v2) = g.select_edge_random()
        
        g.merge_vertex(v1,v2)
        print(g)        
                            
    
if __name__ == "__main__":
    main()



