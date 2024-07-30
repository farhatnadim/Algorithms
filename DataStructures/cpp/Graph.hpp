#pragma once
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory>
#include <iostream>
#include <stack>
#include <queue>

// Inspired by Sedgewick's Graph implementation (page 540)

enum class Graph_Input_type { IMPLICIT, EXPLICIT };

template <typename T>
class Graph
{
    using edges_t = std::set<T>;
    using adj_list_t = std::map<T, edges_t>;

public:
    // Constructors
    void initialize(int V, int E)
    {
        m_v = V;
        m_e = E;
        m_adj_list.clear();
        m_explored.assign(m_v, false);
        edgeTo.assign(m_v, 0);
        m_id.assign(m_v, 0);
    }

    Graph(std::ifstream& f, Graph_Input_type input) : m_cc_count{0}
    {
        std::string edges;
        std::string vertices;
        if (getline(f, vertices) && getline(f, edges))
        {
            initialize(std::stoi(vertices), std::stoi(edges));
            int u, v;
            while (f >> u >> v)
            {
                addEdge(u, v);
            }
        }
    }

    void addEdge(T v, T w)
    {
        m_adj_list[v].insert(w);
        m_adj_list[w].insert(v);
    }

    edges_t adj(T v) const
    {
        return m_adj_list.at(v);
    }

    adj_list_t adj_list() const
    {
        return m_adj_list;
    }

    const int& Get_vertices_number() const
    {
        return m_v;
    }

    const int& Get_edges_number() const
    {
        return m_e;
    }

    // Depth first search
    void dfs(const T& v)
    {
        m_explored[v] = true;
        m_id[v] = m_cc_count;
        for (const auto& edge : this->adj(v))
        {
            if (!m_explored[edge])
            {
                edgeTo[edge] = v;
                dfs(edge);
            }
        }
    }

    // Breadth first search
    void bfs(const T& v)
    {
        m_explored[v] = true;
        std::queue<T> q;
        q.push(v);

        while (!q.empty())
        {
            T vertex = q.front();
            q.pop();
            for (const auto& edge : this->adj(vertex))
            {
                if (!m_explored[edge])
                {
                    edgeTo[edge] = vertex;
                    m_explored[edge] = true;
                    q.push(edge);
                }
            }
        }
    }

    bool isGraphConnected() const
    {
        std::size_t explored_accumulator = 0;
        for (const auto& element : m_explored)
        {
            if (element)
            {
                explored_accumulator++;
            }
        }
        return explored_accumulator == m_v;
    }

    std::vector<T> PathTo(T v, T s) const
    {
        if (!hasPathTo(v))
        {
            std::cout << "Warning! Did not find a path to the vertex " << v << std::endl;
            return {};
        }
        std::vector<T> path;
        for (T x = v; x != s; x = edgeTo[x])
        {
            path.push_back(x);
        }
        path.push_back(s);
        return path;
    }

    void reset_explored()
    {
        std::fill(m_explored.begin(), m_explored.end(), false);
    }

    void cc()
    {
        for (std::size_t s = 0; s < m_v; s++)
        {
            if (!m_explored[s])
            {
                this->dfs(s);
                m_cc_count++;
            }
        }
    }

    const int& Get_cc_Count() const
    {
        return m_cc_count;
    }

    const std::size_t& Get_vertex_id(const std::size_t& v) const
    {
        return m_id[v];
    }

    bool Connected_vertices(const T& v, const T& w) const
    {
        return m_id[v] == m_id[w];
    }

    friend void drawGraph<T>(std::ostream &out, const Graph<T>& graph, bool digraph);

private:
    int m_v; // number of vertices
    int m_e; // number of edges
    adj_list_t m_adj_list; // adjacency list
    bool m_connected;
    std::vector<bool> m_explored;
    std::vector<std::size_t> m_id;
    int m_cc_count; // connected components count
    std::vector<T> edgeTo;

    bool hasPathTo(T v) const
    {
        return m_explored[v];
    }
};

template <typename T>
void drawGraph(std::ostream &out, const Graph<T>& graph, bool digraph)
{
    using adj_list_t = typename Graph<T>::adj_list_t;
    using edges_t = typename Graph<T>::edges_t;

    const adj_list_t& list = graph.m_adj_list;
    std::string graph_type = digraph ? "digraph" : "graph";
    std::string edge_type = digraph ? " -> " : " -- ";

    out << graph_type << " G {" << "\n";
    for (const auto& [key, edges] : list)
    {
        for (const auto& element : edges)
            out << "\"" << key << "\"" << edge_type << "\"" << element << "\"" << ";\n";
    }
    out << "}\n";
}
