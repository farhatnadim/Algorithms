#pragma once
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory>
#include <iostream>
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
        edges_t adj(int v); // return edges for a vertex
        void addEdge(int v, int w); // add edge v-w to this graph
        std::string toString();      //String representation
        void drawGraph(std::ostream & out);
    private:
        int m_v; // number of vertices
        int m_e; // number of edges
        adj_list_t m_adj_list; // map of set    
};
