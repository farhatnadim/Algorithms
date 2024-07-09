#include <iostream>
#include <fstream>
#include <string>

#include "Graph.hpp"
std::string GRAPH_DATA_FILE ("../../data/tinyG.txt");
std::string DOT_DATA_FILE("../../data/tinyG.dot");
using namespace std;

void drawGraph(ostream & out,adj_list_t list, bool digraph )
{
    string graph_type  = digraph ? "digraph" : "graph";
    
    string edge_type  = digraph ? " -> " : " -- ";

    out << graph_type << " G {" << "\n";
    for (auto [key,edges] : list)
    {
        for (auto element : edges)
            out << "\"" << key << "\"" << edge_type << "\"" << element <<"\"" << ";\n";
    }
    out << "}\n";
}


struct Data {
    int  vertices;
    int edges;
};

int main (int argc , char ** argv )
{

    if( argc < 2 )
    {
        cout << "Usage enter source vertex index\n";
        exit(0);

    }
    auto v_index = stoi(argv[1]);
    if (v_index < 0)
    {
        cout << "v_index is negative " << endl;
        exit(1);
    }
    cout << "User Entered vertex index " << v_index << endl;
    ifstream graph_data_file(GRAPH_DATA_FILE); 
    if (!graph_data_file.is_open())
    {
        cout << "Couldn't open the file \"" << GRAPH_DATA_FILE << "\"for reading" << endl;
        exit(1);// failed to open file
    }
    ofstream graph_dot_file(DOT_DATA_FILE);
    if (!graph_dot_file.is_open())
    {
        cout << "Couldn't open the file \"" << DOT_DATA_FILE  << "\"for writing" << endl;
        exit(1);// failed to open file
    }
    
    Graph g(graph_data_file);   
    graph_data_file.close();

    auto adj_list = g.adj_list();
    bool digraph = false;
    drawGraph(graph_dot_file,adj_list, digraph);
    graph_dot_file.close();
    g.dfs(v_index);
    cout << "The graph is connected " << g.connected();


    return 0;
}