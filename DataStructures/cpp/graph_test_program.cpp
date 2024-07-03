#include <iostream>
#include <fstream>
#include <string>
#include "Graph.hpp"
std::string GRAPH_DATA_FILE ("../../data/tinyG.txt");
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
        cout << "Couldn't open the file " << GRAPH_DATA_FILE << endl;
        exit(1);// failed to open file
    }
    
    Graph g(graph_data_file);

    return 0;
}