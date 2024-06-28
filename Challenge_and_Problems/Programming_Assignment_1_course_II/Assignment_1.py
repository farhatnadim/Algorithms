'''The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 
11𝑡ℎ row looks likes : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes).  (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.'''

from Node import Vertex
import Graph
import os
os.environ["PATH"] += os.pathsep + r'D:\Program Files\Graphviz-11.0.0-win64\bin'

numSCC = [None]
numSCC[0] = 0
def dfs_recursive(graph :'Graph', vertex: Vertex) -> None:
            vertex.set_explored(True)
            vertex.scc = numSCC[0]
            for edge in vertex.edges:
                if not graph.get_vertex(edge).is_explored():
                    dfs_recursive(graph, graph.get_vertex(edge))
                    
                    
                    
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
  full_path= os.getcwd()
  
  file_name_scc = os.path.join(full_path,'problem8.10test1.txt')
  
  g = create_graph(file_name_scc)
  '''
  r_g = g.reversal()
  r_g.topological_sort()
  r_g.print_graph()

  temp_graph = Graph.Graph()
  temp_graph.vertices = [None]*len(r_g.vertices)
  for v1,v2 in zip(r_g.vertices,g.vertices):
    temp_graph.vertices[v1.currentLabel-1] = v2
  for vertex in temp_graph.vertices:
    print(vertex.edges, vertex.label)
  
  for vertex in (temp_graph.vertices): 
    if not vertex.is_explored():
      numSCC[0] += 1
      dfs_recursive(g, vertex)
      
      
  scc = []
  for vertex in temp_graph.vertices:
    scc.append(vertex.scc)
  scc.sort()
  print(scc)   
  
'''
  g.kosraju(g.vertices[0])
  scc = [0]*len(g.vertices)
  for vertex in g.vertices:
    scc[vertex.scc] += 1
    
  scc.sort()
  print(scc[::-1])
 
def main():

  test_1() 
    

    
if __name__ == "__main__":
    main()