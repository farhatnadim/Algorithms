'''The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 
11𝑡ℎ row looks likes : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes).  (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.'''

from Node import Vertex
import Graph

def create_graph(file_name):
  g = Graph.Graph()
  vertex_added = []
  with open(file_name) as f:
    for line in f:
      line = line.split()
      if line[0] not in vertex_added:
        g.add_vertex(Vertex( edges = [int(line[1])-1], label = line[0]))
        vertex_added.append(line[0])
      else:
        g.get_vertex(vertex_added.index(line[0])).add_edge(int(line[1])-1)
  return g
def test_1():
  file_name_scc = "problem8.10test1.txt"
  g = create_graph(file_name_scc)
  #g.print_graph()
  k_gr = g.kosraju(g.vertices[0])
  scc = []
  for vertex in k_gr.vertices:
    scc.append(vertex.scc)
    
  print(scc.sort()) 
  
def main():
  file_name_scc = "problem8.10test4.txt"
  g = create_graph(file_name_scc)
  #g.print_graph()
  k_gr = g.kosraju(g.vertices[0])
  scc = []
  for vertex in k_gr.vertices:
    scc.append(vertex.scc)
    
  scc.sort()
  print(scc) 
    

    
if __name__ == "__main__":
    main()