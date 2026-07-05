'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''

import random
import os

class Graph (dict):
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a a dictionary where the keys are the vertices and the values are the edges'''
    def __init__(self) -> None:
        super().__init__()
    
    def select_edge_random(self) -> tuple:
        '''pick a uniformly random vertex, then a uniformly random incident edge'''
        # we assume no keys are the same , it is a hashtable after all
        vertex1 = random.choice(list(self.keys()))
        vertex2 = random.choice(self[vertex1])
        return (vertex1,vertex2)
    
    def merge_vertex(self, vertex1:str, vertex2:str) -> None:
        
        self[vertex1] =  self[vertex1] + self[vertex2]
        del self[vertex2]
        
    def replace_vertex(self,vertex1:str, vertex2:str) -> None:
        '''replace vertex2 with vertex1 in the graph'''
        for vertex in self:
            if vertex2 in self[vertex]:
                self[vertex] = [vertex1 if edge == vertex2 else edge for edge in self[vertex]]
                
    def remove_self_loops(self,vertex1:str) -> None:
        #remove self loops
        new_edges = [edge for edge in self[vertex1] if edge != vertex1 ] 
        self[vertex1] = new_edges
                  
    def min_cut(self) -> int:
        '''contract the graph down to 2 vertices (one Karger trial) and
        return the number of crossing edges of the resulting cut'''
        while len(self) > 2:
            (v1,v2) = self.select_edge_random()
            self.merge_vertex(v1,v2)
            self.replace_vertex(v1,v2)
            self.remove_self_loops(v1)
        return self.countEdges()

    def countEdges (self): 
        count = 0
        for edges in list(self.values()):
            count += len(edges)
        return count//2
                
    
def load_graph(path: str) -> Graph:
    '''read an adjacency-list file (vertex followed by its neighbors per line)
    and construct a Graph object'''
    g = Graph()
    with open(path) as f:
        for line in f:
            line = line.split()
            g[line[0]] = [str(entry) for entry in line[1:]]
    return g


def main(input_file: str | None = None, trials: int = 100) -> int:
    '''run Karger's algorithm `trials` times and return the best (smallest) cut found'''
    if input_file is None:
        input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'data', 'kargerMinCut.txt')

    results = []
    for _ in range(trials):
        g = load_graph(input_file)
        results.append(g.min_cut())
    result = min(results)
    print("Min Cut\n", result)
    return result


if __name__ == "__main__":
    main()



