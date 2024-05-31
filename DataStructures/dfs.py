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
    
    


def main():
    
    number_0 = Vertex([1,2])
    number_1 = Vertex([0,3])
    number_2 = Vertex([0,3,4])
    number_3 = Vertex([1,2,4,5])
    number_4 = Vertex([2,3,5])
    number_5 = Vertex([3,4])
    
    
    g = Graph()
    g.add_vertex(number_0)
    g.add_vertex(number_1)    
    g.add_vertex(number_2)
    g.add_vertex(number_3)
    g.add_vertex(number_4)
    g.add_vertex(number_5)
    
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