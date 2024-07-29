#pragma once
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory>
#include <iostream>


/* Inspired from Sedgewick Graph implmentation page 540*/


//Follows mathematical definition of a graph 
// 
using edges_t = std::set<uint> ;
using adj_list_t = std::map<uint, edges_t>; 

enum class Graph_Input_type {IMPLCIT, EXPLICIT};
class Graph
{
    public:
        /****Constructors ****/
        Graph(int) ;//create a V-vertex graph with no edges
        Graph(std::ifstream &is, Graph_Input_type input = Graph_Input_type::EXPLICIT); // read a graph from input stream is

        /**** basic functionality ****/
      
        edges_t adj(int v); // return edges for a vertex
        void addEdge(int v, int w); // add edge v-w to this graph
        std::string toString();      //String representation
        adj_list_t  adj_list();
        void reset_explored();

        // Search, path, connectivity 

        void dfs(const int &);
        bool isGraphConnected();
        std::vector<int> PathTo(int v, int s);
        inline bool hasPathTo(int v) 
        {
           return m_explored[v];
        }
        void bfs(const int &);
        void cc(); // connected componens
        bool Connected_vertices(const int & v, const int & w);
        //*getters and setters boring stuff  *// 
        const std::vector<int> & Get_edge_to () const;
        const std::vector<int> & Get_explored () const;
        const int & Get_vertices_number() const; // number of vertices
        const int & Get_edges_number() const; // number of edges 
        const int  Get_cc_Count() const;
        const uint & Get_vertex_id(const uint &v) const;


    private:
        int m_v; // number of vertices
        int m_e; // number of edges
        adj_list_t m_adj_list; // map of set
        bool m_connected;
        std::vector<bool> m_explored;
        std::vector<uint> m_id;
        uint m_cc_count ; // connected components count
        std::vector<int> edgeTo;

        
};
