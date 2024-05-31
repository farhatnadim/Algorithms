from Node import Vertex
from Queue import Queue
from Graph import Graph



''''

def bfs( graph: Graph, vertex_index : int, connected_components = 0) -> None:
    graph[vertex_index].set_explored()
    graph[vertex_index].distance = 0
    q = Queue()
    q.enqueue(graph[vertex_index])
    while (not q.is_empty()):
        v = q.dequeue()
        v.cc = connected_components
        for edge in v.edges:
            if not graph[edge].is_explored():
                graph[edge].set_explored()
                graph[edge].distance = v.distance + 1 
                q.enqueue(graph[edge])
    
def Undirected_Connected_Components(graph : Graph) -> None :
    numCC = 0
    for vertex in graph:
        if  not vertex.is_explored():
            numCC = numCC + 1
            bfs(graph,graph.index(vertex),numCC)
            
'''

def main():
    
    number_0 = Vertex([2,4])
    number_1 = Vertex([3])
    number_2 = Vertex([0,4])
    number_3 = Vertex([1])
    number_4 = Vertex([0,2,6,8])
    number_5 = Vertex([7,9])
    number_6 = Vertex([4])
    number_7 = Vertex([5])
    number_8 = Vertex([4])
    number_9 = Vertex([5])
    
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
   

    vertex_index = 0
    g.Undirected_Connected_Components()
    for vertex in g:
        print(f"Connected Components per vertex {vertex.get_connected_components()}")
        
        
if __name__ == "__main__":
    main()