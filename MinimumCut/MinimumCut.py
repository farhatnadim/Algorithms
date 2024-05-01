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
        # we assume no keys are the same , it is a hastable after all
        vertex1 = list(self.keys())[keys_index] 
        # check if key_index exist
        edge_index = random.randint(0,len(self[vertex1])-1)
        try:
            vertex2 = self[vertex1][edge_index]
        except :
            print(f"Unexpected error while fetching vertex2")
        return (vertex1,vertex2)
    
    def merge_vertex(self, vertex1:str, vertex2:str) -> None:
        
        self[vertex1] =  self[vertex1] + self[vertex2]
        del self[vertex2]
        
    def remove_self_loops(self,vertex1:str, vertex2:str) -> None:
        #remove self loops
        new_edges = [edge for edge in self[vertex1] ] 
        self[vertex1] = new_edges
    
    def replace_vertex(self,vertex1:str, vertex2:str) -> None:
        '''replace vertex2 with vertex1 in the graph'''
        for vertex in self:
            if vertex2 in self[vertex]:
                self[vertex] = [vertex1 if edge == vertex2 else edge for edge in self[vertex]]
                
    def min_cut(self) -> int:
        '''return the minimum cut of the graph'''
        while len(self) > 2:
            (v1,v2) = self.select_edge_random()
            if v1 == None:
                return None
            if v2 == None:
                return None
            self.merge_vertex(v1,v2)
            self.remove_self_loops(v1,v2)
            self.replace_vertex(v1,v2)
        
        
    def countVeritces (): 
        for edges in list(self.values()):
            count += len(edges)
        return count//2
                
        
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
        
        g = Graph()
        with open(file) as f:
            for line in f:
                line = line.split()
                g[line[0]] = [str(entry) for entry in  line[1:] ]  
        print("Raw graph \n", g)
        # select random vertices
        v1,v2 = g.select_edge_random()
        print(f"the selected edge is {v1}-{v2}\n")            
        # merge vertices
        g.merge_vertex(v1,v2)
        print(f"The graph after merging {v2} in to {v1}\n", g)
        # remove self loops
        g.replace_vertex(v1,v2)
        print(f"the graph after replacing {v2} with {v1}\n",g)
        #g.remove_self_loops(v1,v2)
        #print(g)
        # find min cut
        
        
                            
    
if __name__ == "__main__":
    main()



