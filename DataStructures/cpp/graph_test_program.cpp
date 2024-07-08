#include <iostream>
#include <fstream>
#include <string>

#include "Graph.hpp"
std::string GRAPH_DATA_FILE ("../../data/tinyG.txt");
std::string DOT_DATA_FILE("../../data/tinyG.dot");
using namespace std;

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

    g.drawGraph(graph_dot_file);
    graph_dot_file.close();
    

    return 0;
}