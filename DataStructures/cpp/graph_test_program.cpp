#include <iostream>
#include <fstream>
#include <string>
#include "Graph.hpp"


std::vector<std::string> graph_filenames {"tinyG.txt","tinyCG.txt"};
std::vector<std::string> drawing_filenames {"tinyG.dot","tinyCG.dot"}; // me being lazy , need to change it 
const std::string GRAPH_DATA_FILE ("../../data/" + graph_filenames[1]);
const std::string DOT_DATA_FILE("../../data/" + drawing_filenames[1] );
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

    if( argc < 3 )
    {
        cout << "Usage enter source vertex index\n";
        cout << "Usage enter the sink vertex index\n";
        exit(0);
    }
    auto v_index = stoi(argv[1]);
    if (v_index < 0)
    {
        cout << "v_index is negative " << endl;
        exit(1);
    }
    auto s_index = stoi(argv[2]);
    if (s_index < 0)
    {
        cout << "s_index is negative " << endl;
        exit(1);
    }
    cout << "User Entered source index " << v_index << endl;
    cout << "User Entered sink index " << s_index << endl;
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
    string result_graph = "the graph is ";
    string connected_status = "";
    g.connected() ? connected_status ="connected\n" : connected_status = "NOT connected\n"; 
    cout << result_graph + connected_status ;
    for (auto & vertex : g.PathTo(s_index,v_index))
        cout << vertex << " " ;
    cout << endl;
    return 0;
}