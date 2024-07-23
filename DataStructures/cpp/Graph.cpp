#include "Graph.hpp"
#include <stack>
#include <queue>
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
        edgeTo.push_back(0);
        m_id.push_back(0);
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

const int & Graph::Get_vertices_number() const
{
    return m_v;
}


const int  & Graph::Get_edges_number() const
{
    return m_e;
}

/*Depth first search*/
void Graph::dfs(const int &v)
{
    m_explored[v] = true;
    for (auto &edge : this->adj(v))
    {
        if (m_explored[edge] == false)
        {
            edgeTo[edge] = v;
            m_id[v] = m_cc_count;
            dfs(edge);
        }

    }
}
/*Breadth first search*/
void Graph::bfs(const int &v)
{
    m_explored[v] = true;
    queue<int> q;
    q.push(v);

    while (!q.empty())
    {
        auto vertex  = q.front();
        q.pop();
        //cout << vertex << " ";
        for (auto edge : this->adj(vertex))
          if (m_explored[edge] == false)
          {
            edgeTo[edge] = vertex;
            m_explored[edge]= true;
            q.push(edge);
          }

    }
}
bool Graph::isGraphConnected()
{
    auto connected = false;
    uint explored_accumulator = 0;
    uint index = 0;
    cout << "\n" << "The subgraph vertices are\n";
    for (const auto &element : m_explored)
    {
        if (element == true)
            {
                explored_accumulator++;
            }
        index +=1;
    }
    (explored_accumulator < m_v) ? connected = false : connected = true;
    return connected;
}

vector<int> Graph::PathTo(int v, int s)
{
  if ( !hasPathTo(v))
    {
        cout << "Warning ! did not find a path to the vertex " << v << endl;
        return vector<int> ();
    }
  vector<int> path;
  for (int x = v; x != s; x = edgeTo[x])
    path.push_back(x);
  path.push_back(s);
  return path;
}


void Graph::reset_explored()
{
    if (m_explored.size() != 0)
      for (auto element : m_explored)
        element = false;
}

void Graph::cc()
{
    
}