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
            ''

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
                
    

def graph_reversal(graph : Graph) -> Graph:
    #pre allocating o(n)
    r_graph = [Vertex(edges=[]) for x in range(len(graph))]
    
    # interating o(n*m)
    for vertex in graph:
        for edge in vertex.edges: # need to implement add edg
            # if r_graph already has a vertex object use add , else 
            # create a new vertex obect``
            r_graph[edge].add_edge(graph.index(vertex))
    return r_graph

def main():
    
    number_0 = Vertex([2])
    number_1 = Vertex([3])
    number_2 = Vertex([4,10])
    number_3= Vertex([6])
    number_4 = Vertex([0,8,6])
    number_5 = Vertex([9])
    number_6 = Vertex([])
    number_7 = Vertex([5])
    number_8 = Vertex([1,3,7])
    number_9 = Vertex([7])
    number_10 = Vertex([5,7])
    
    g = Graph()
    g.add_vertex(number_0)
    g.add_vertex(number_1)    
    g.add_vertex(number_2)
    g.add_vertex(number_3)

    
    for vertex in g:
        print(vertex.edges)
    print("")
    print("")
    print("")
    r_graph = graph_reversal(g)
    
    for vertex in r_graph[:]:
            print(vertex.edges)
    
if __name__ == "__main__":
    main()