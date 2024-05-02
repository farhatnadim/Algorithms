'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''

import random
import os

class Graph (dict):
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a a dictionary where the keys are the vertices and the values are the edges'''
    def __init__(self) -> None:
        super().__init__()
    
    def select_edge_random(self) -> tuple:
        
        keys_index = random.randint(0,len(self.keys())-1)
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
        
    def remove_self_loops(self,vertex1:str) -> None:
        #remove self loops
        new_edges = [edge for edge in self[vertex1] if edge != vertex1 ] 
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
            self.replace_vertex(v1,v2)
            self.remove_self_loops(v1)
        
    def countEdges (self): 
        count = 0
        for edges in list(self.values()):
            count += len(edges)
        return count//2
                
    
def main():
        '''read graph from file and contstruct a graph object'''
        graph = Graph()
        # read input files 
        #input_files = [file for file in os.listdir('.') if ('input' in file)]
    
        #for file in input_files:
        base_dir = os.getcwd()
        mincut_folder = 'MinimumCut'
        mincut_folder = ''
        input_file = 'input_random_40_200.txt'
        input_file = os.path.join(base_dir,mincut_folder,input_file)
        
        g = Graph()
        with open(input_file) as f:
            for line in f:
                line = line.split()
                g[line[0]] = [str(entry) for entry in  line[1:] ]  
        print("Raw graph \n", g)
        # select random vertices
        #v1,v2 = g.select_edge_random()
        #print(f"the selected edge is {v1}-{v2}\n")            
        # merge vertices
        #g.merge_vertex(v1,v2)
        #print(f"The graph after merging {v2} in to {v1}\n", g)
        # remove self loops
        #g.replace_vertex(v1,v2)
        #print(f"the graph after replacing {v2} with {v1}\n",g)
        #g.remove_self_loops(v1)
        #print("The graph after removing self loops\n",g)
        #print(g)
        # find min cut
        results = []
        for i in range(10):
            g = Graph()
            with open(input_file) as f:
                for line in f:
                    line = line.split()
                    g[line[0]] = [str(entry) for entry in  line[1:] ]
            g.min_cut()
            results.append(g.countEdges())
        result = min(results)
        # getting the actual result 
        output_file = input_file.replace("input","output")
        validated_result = 0
        with open(output_file ) as output_f:
            for line in output_f:
                validated_result = line[0]
        
        print("Min Cut\n",result)
        print("Validate Cut \n",validated_result)
                            
    
if __name__ == "__main__":
    main()



