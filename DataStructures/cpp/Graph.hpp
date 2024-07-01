#pragma once
#include <fstream>
#include <vector>
#include <string>

/**
 * Adjacent vertices : When two vertices are connected via an edge
 * Incident edge : An edge connecting two vertices
 * Degree of Vertex : number of edges incident on a vertex
 * Subgraph : As set of edges and vertices that consitute a graph
*/




class Graph
{
    Graph(int V);   //create a V-vertex graph with no edges
    Graph(std::ifstream &is); // read a graph from input stream is

    int V(); // number of vertices
    int E(); // number of edges 

    void addEdge(int v, int w); // add edge v-w to this graph
    std::vector<int> adj(int v); // vertices adjacent to v 
    std::string toString();      //String representation

    private:
    int m_v; // number of vertices
       
};