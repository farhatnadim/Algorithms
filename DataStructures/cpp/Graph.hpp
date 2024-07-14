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
        // basic functionality
        int V(); // number of vertices
        int E(); // number of edges 
        int degree( int ); //Compute the degree of a vertex
        int maxDegree(); // Compute Max degree in a graph
        int avgDegree();
        int numberOfSelfLoop();
        edges_t adj(int v); // return edges for a vertex
        void addEdge(int v, int w); // add edge v-w to this graph
        std::string toString();      //String representation
        adj_list_t  adj_list();
        void reset_explored();

        // Search, path, connectivity  
        void dfs(const int &);
        bool connected();
        std::vector<int> PathTo(int v, int s);
        bool hasPathTo(int v) 
        {
           return m_explored[v];
        }
        void bfs(const int &);

    private:
        int m_v; // number of vertices
        int m_e; // number of edges
        adj_list_t m_adj_list; // map of set
        bool m_connected;
        std::vector<bool> m_explored;
        std::vector<uint> connected_component;
        std::vector<int> edgeTo;
        
};
