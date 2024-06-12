from Node import Vertex
from Stack import Stack
from Graph import Graph
import graphviz


def main():
    number_0 = Vertex([2], label='1')
    number_1 = Vertex([3, 9], label='2')
    number_2 = Vertex([4, 10], label='3')
    number_3 = Vertex([6], label='4')
    number_4 = Vertex([0, 8, 6], label='5')
    number_5 = Vertex([9], label='6')
    number_6 = Vertex([], label='7')
    number_7 = Vertex([5], label='8')
    number_8 = Vertex([1, 3, 7], label='9')
    number_9 = Vertex([7], label='10')
    number_10 = Vertex([5, 7], label='11')

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

    for vertex in g.get_vertices():
        print(vertex.edges)
    print("")
    print("")
    print("")
    r_graph = graph_reversal(g)

    for vertex in r_graph.get_vertices():
        print(vertex.edges)
        
    r_graph.print_graph()

if __name__ == "__main__":
    main()
