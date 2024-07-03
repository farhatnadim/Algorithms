#pragma once
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory>
/* Inspired from Sedgewick Graph implmentation page 540*/



using edges_t = std::set<uint> ;
using adj_list_t = std::map<uint, edges_t>; 
class Graph
{
    public:
        Graph(int) ;//create a V-vertex graph with no edges
        Graph(std::ifstream &is); // read a graph from input stream is

        int V(); // number of vertices
        int E(); // number of edges 
        int degree( int ); //Compute the degree of a vertex
        int maxDegree(); // Compute Max degree in a graph
        int avgDegree();
        int numberOfSelfLoop();
    

        void addEdge(int v, int w); // add edge v-w to this graph
        edges_t adj(int v); // vertices adjacent to v 
        std::string toString();      //String representation

    private:
        int m_v; // number of vertices
        int m_e; // number of edges
        std::shared_ptr<adj_list_t>  m_adj_t_ptr; // map of set    
};
