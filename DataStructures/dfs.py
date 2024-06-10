from Node import Vertex
from Stack import Stack
from Graph import Graph
import graphviz

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
            r_graph[edge].label= str(edge+1)
    return r_graph

def print_graph(graph: Graph):
    
    #dot = graphviz.Digraph()
    #dot.node(graph[0].label)
    dot = graphviz.Digraph(format='svg')
    for node in graph:
        dot.node(name=str(id(node)),label=node.label)
        for edge in node.edges:
            dot.edge(str(id(node)),str(id(graph[edge])))
    dot.render('graph',view=True)
def main():
    
    number_0 =  Vertex([2],label='1')
    number_1 =  Vertex([3,9],label='2')
    number_2 =  Vertex([4,10],label='3')
    number_3=   Vertex([6],label='4')
    number_4 =  Vertex([0,8,6],label='5')
    number_5 =  Vertex([9],label='6')
    number_6 =  Vertex([],label='7')
    number_7 =  Vertex([5],label='8')
    number_8 =  Vertex([1,3,7],label='9')
    number_9 =  Vertex([7],label='10')
    number_10 = Vertex([5,7],label='11')
    
    g = Graph()
    g.add_vertex(number_0)
    g.add_vertex(number_1)    
    g.add_vertex(number_2)
    g.add_vertex(number_3)
    g.add_vertex(number_4)
    g.add_vertex(number_5)    
    g.add_vertex(number_6)
    g.add_vertex(number_7)
    g.add_vertex(number_8)    
    g.add_vertex(number_9)
    g.add_vertex(number_10)
    
    
    for vertex in g:
        print(vertex.edges)
    print("")
    print("")
    print("")
    r_graph = graph_reversal(g)
    
    for vertex in r_graph[:]:
            print(vertex.edges)
    #print_graph(g)
    print_graph(r_graph)
if __name__ == "__main__":
    main()