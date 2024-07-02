#include "Graph.hpp"
#include <string>
using namespace std;




Graph::Graph(int V) 
{
    m_e = 0;
    m_v = V;
       for (int i = 0; i < m_v ; i++)
       {
            m_adj_ptr->insert(std::make_pair(i,edges()));
       }
}

Graph::Graph(ifstream  &f )
{

    string edges;
    string vertices;

    getline(f,vertices);
    Graph(stoi(vertices));


}; 

