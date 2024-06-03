from Node import Vertex
from Stack import Stack
from Graph import Graph

def dfs( graph: Graph) -> None:    
    s = Stack()
    s.push(graph[0])
    while (not s.is_empty()):
        v = s.pop()
        if (not v.is_explored()):
            v.set_explored()
            for edge in v.edges:
                s.push(graph[edge])
                
def dfs_recursive ( graph : Graph, vertex) ->None:
    vertex.set_explored(True)
    for edge in vertex.edges:
        if (not graph[edge].is_explored()):
            dfs_recursive(graph,graph[edge])

def topological(graph: Graph , vertex: Vertex) ->None:
    
    def dfs_recursive( graph : Graph, vertex :Vertex, currentLabel: list ) ->None:
        vertex.set_explored(True)
        for edge in vertex.edges:
            if (not graph[edge].is_explored()):
                dfs_recursive(graph,graph[edge],currentLabel)
        vertex.currentLabel = currentLabel[0]
        currentLabel[0] = currentLabel[0] - 1
        
    currentLabel = [len(graph)]
    for vertex in graph:
        if (not vertex.is_explored()):
            dfs_recursive(graph, vertex, currentLabel)    
                
    


def main():
    
    number_0 = Vertex([1,2])
    number_1 = Vertex([3])
    number_2 = Vertex([3])
    number_3 = Vertex([])
    
    
    g = Graph()
    g.add_vertex(number_0)
    g.add_vertex(number_1)    
    g.add_vertex(number_2)
    g.add_vertex(number_3)
    
    topological(g,number_0)
    
    for vertex in g:
        print(vertex.currentLabel)
  
    
if __name__ == "__main__":
    main()