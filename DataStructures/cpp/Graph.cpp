#include "Graph.hpp"
#include <string>
#include <iostream>

using namespace std;

Graph::Graph(int V) 
{

}

Graph::Graph(ifstream  &f )
{

    string edges;
    string vertices;

    getline(f,vertices);
    getline(f,edges);
    m_v = std::stoi(vertices);
    m_e = std::stoi(edges);
    for (int i {0}; i < m_v; i++)
    {
        m_adj_t_ptr->insert(make_pair(i,edges_t()));
    }
    while(f)
    {
        //getline(f,vertices);
        //cout << vertices[0] << "\n";
        //m_adj_ptr->insert(make_pair(vertices[0],))
    }
}; 

