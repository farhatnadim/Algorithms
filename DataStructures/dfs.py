from Node import Vertex
import Graph

numcc = 0
def main():
    number_0 = Vertex([2], label='1')
    number_1 = Vertex([3, 9], label='2')
    number_2 = Vertex([4, 10], label='3')
    number_3 = Vertex([6], label='4')
    number_4 = Vertex([0, 6, 8], label='5')
    number_5 = Vertex([9], label='6')
    number_6 = Vertex([8], label='7')
    number_7 = Vertex([5], label='8')
    number_8 = Vertex([3, 1, 7], label='9')
    number_9 = Vertex([7], label='10')
    number_10 = Vertex([5, 7], label='11')

    g = Graph.Graph()
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

    g.topological_sort()
    r_g  = g.reversal()

    t_graph=r_g.kosraju(number_0)
    for vertex in t_graph.vertices:
        print(vertex.label, vertex.scc)
    
if __name__ == "__main__":
    main()