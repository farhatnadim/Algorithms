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
    currentLabel = len(graph)
    def dfs_recursive ( graph : Graph, vertex) ->None:
        vertex.set_explored(True)
        for edge in vertex.edges:
            if (not graph[edge].is_explored()):
                dfs_recursive(graph,graph[edge])
        graph[edge].currentLabel = currentLabel
        currentLabel = currentLabel - 1    
    for vertex in graph:
        if (not vertex.is_explored()):
            dfs_recursive(graph, vertex)    
                
    


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
    
    
    for vertex in g:
        print(vertex.is_explored())

    dfs(g)
    for vertex in g:
        print(vertex.is_explored())
    for vertex in g:
        vertex.set_explored(False)
    
    for vertex in g:
        print(vertex.is_explored())
    
    dfs_recursive(g,g[0])
    
    for vertex in g:
        print(vertex.is_explored())
    
if __name__ == "__main__":
    main()