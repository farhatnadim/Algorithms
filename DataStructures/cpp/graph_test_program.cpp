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

void inputValidation( int source_index, int sink_index)
{
    if (source_index < 0)
    {
        cout << "source index is negative " << endl;
        exit(1);
    }
    if (sink_index < 0)
    {
        cout << "sink is negative " << endl;
        exit(1);
    }

    cout << "User Entered source index " << source_index << endl;
    cout << "User Entered sink index " << sink_index << endl;
}
void welcomeMessage(const int & argumentCount)
{
    cout << "Welcome to the Graph test program, this program tests different functionalitis\n"
         <<  "of basic graph functionality\n"
         <<  "run ./GraphTest source_index sink_index Method\n"
         <<  "Source Index the vertex index where you want to execute the algorithm\n"
         <<  "Sink Index is the vertex index on which you want to find a path from the source index\n"
         <<  "Method : 0 for DFS or  1 BFS based method\n";

    if( argumentCount < 3 )
    {
        cout << "Usage enter source vertex index\n";
        cout << "Usage enter the sink vertex index\n";
        exit(0);
    }

}
int main (int argc , char ** argv )
{

    welcomeMessage(argc);
    
    auto source_index = stoi(argv[1]);
    auto sink_index = stoi(argv[2]);

    inputValidation(source_index,sink_index);
       
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
    g.bfs(source_index);
    string result_graph = "the graph is ";
    string connected_status = "";
    g.connected() ? connected_status ="connected\n" : connected_status = "NOT connected\n"; 
    cout << result_graph + connected_status ;
    for (auto & vertex : g.PathTo(sink_index,source_index))
        cout << vertex << " " ;
    cout << endl;
    g.reset_explored();
    
    return 0;
}