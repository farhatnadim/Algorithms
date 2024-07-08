#include "Graph.hpp"

using namespace std;

Graph::Graph(int V) : m_v{V}, m_e{0}
{
}

Graph::Graph(ifstream  &f ) : m_adj_list()
{
    string edges;
    string vertices;
    getline(f,vertices);
    getline(f,edges);
    m_v = std::stoi(vertices);
    m_e = std::stoi(edges);
    for (int i {0}; i < m_v; i++)
    {   
        m_adj_list.insert(make_pair(i,edges_t()));
    }
    while(f)
    {
        int u,v;
        if (f >> u >> v)
        {
            addEdge(u,v);
        } 
    }
};

void Graph::addEdge(int v, int w)
{
    m_adj_list[v].insert(w);
    m_adj_list[w].insert(v);
}

edges_t Graph::adj(int v)
{
    return m_adj_list[v];
}

void Graph::drawGraph(ostream & out)
{
    out <<"graph G {" << "\n";
    for (auto [key,edges] : m_adj_list)
    {
        for (auto element : edges)
            out << "\"" << key << "\"" << " -- " << "\"" << element <<"\"" << ";\n";
    }
    out << "}\n";
}