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
        m_explored.push_back(false);
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

adj_list_t  Graph::adj_list()
{
    return m_adj_list;
}

int Graph::V()
{
    return m_v;
}
void Graph::dfs(int v)
{
    //static auto currentLabel = V();
    m_explored[v] = true;
    for (auto &edge : this->adj(v))
    {
        if (m_explored[edge] == false)
        {
            dfs(edge);
        }
        
    }
}
bool Graph::connected()
{
    auto connected = false;
    uint explored_accumulator = 0;
    uint index = 0;
    cout << "\n" << "The subgraph vertices are\n";
    for (const auto &element : m_explored)
    {
        
        if (element == true)
            
            {   
                 
                cout << index << " ";
                explored_accumulator++;
            }
            index +=1;
        
    }
    (explored_accumulator < m_v) ? connected = false : connected = true;
    cout << endl;
    return connected;
}
