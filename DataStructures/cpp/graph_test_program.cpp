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

int main ()
{


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