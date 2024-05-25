from Node import Vertex
from Queue import Queue
from Graph import Graph



def bfs( graph: Graph, vertex_index : int):
    graph[vertex_index].set_explored()
    graph[vertex_index].distance = 0
    q = Queue()
    q.enqueue(graph[0])
    while (not q.is_empty()):
        v = q.dequeue()
        for edge in v.edges:
            if not graph[edge].is_explored():
                graph[edge].set_explored()
                graph[edge].distance = v.distance + 1 # bug is in v.distance basically here we are doing += , need to d ref. bestway is copy node to q
                q.enqueue(graph[edge])
    
def main():
    
    s = Vertex([1,2])
    a = Vertex([0,3])
    b = Vertex([0,3])
    c = Vertex([1,2,4,5])
    d = Vertex([2,3,5])
    e = Vertex([3,4])
    
    g = Graph()
    g.add_vertex(s)
    g.add_vertex(a)    
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.add_vertex(e)
    for vertex in g:
        print(vertex.is_explored())

    vertex_index = 0
    bfs(g,vertex_index)
    for vertex in g:
        print(vertex.distance)
if __name__ == "__main__":
    main()