#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <memory>
#include <stack>
#include <queue>
#include "Graph.hpp"

using namespace std;

std::vector<std::string> graph_filenames {"tinyG.txt","tinyCG.txt"};
std::vector<std::string> drawing_filenames {"tinyG.dot","tinyCG.dot"}; // me being lazy, need to change it
const std::string GRAPH_DATA_FILE("../../data/" + graph_filenames[0]);
const std::string DOT_DATA_FILE("../../data/" + drawing_filenames[0]);

void inputValidation(int source_index, int sink_index)
{
    if (source_index < 0)
    {
        cout << "Source index is negative" << endl;
        exit(1);
    }
    if (sink_index < 0)
    {
        cout << "Sink index is negative" << endl;
        exit(1);
    }

    cout << "User Entered source index " << source_index << endl;
    cout << "User Entered sink index " << sink_index << endl;
}

void welcomeMessage(const int &argumentCount)
{
    cout << "Welcome to the Graph test program, this program tests different functionalities\n"
         << "of basic graph functionality\n"
         << "Run ./GraphTest source_index sink_index Method\n"
         << "Source Index: the vertex index where you want to execute the algorithm\n"
         << "Sink Index: the vertex index on which you want to find a path from the source index\n"
         << "Method: 0 for DFS or 1 for BFS based method\n";

    if (argumentCount < 4)
    {
        cout << "Usage: enter source vertex index\n";
        cout << "Usage: enter the sink vertex index\n";
        exit(0);
    }
}

int main(int argc, char **argv)
{
    welcomeMessage(argc);

    auto source_index = stoi(argv[1]);
    auto sink_index = stoi(argv[2]);
    auto method = stoi(argv[3]);

    inputValidation(source_index, sink_index);

    ifstream graph_data_file(GRAPH_DATA_FILE);
    cout << "Reading the graph data from the file " << GRAPH_DATA_FILE << endl;
    if (!graph_data_file.is_open())
    {
        cout << "Couldn't open the file \"" << GRAPH_DATA_FILE << "\" for reading" << endl;
        exit(1); // failed to open file
    }

    ofstream graph_dot_file(DOT_DATA_FILE);
    if (!graph_dot_file.is_open())
    {
        cout << "Couldn't open the file \"" << DOT_DATA_FILE << "\" for writing" << endl;
        exit(1); // failed to open file
    }

    Graph<int> g(graph_data_file, Graph_Input_type::EXPLICIT);

    bool digraph = false;
    cout << "Drawing the graph to the file " << DOT_DATA_FILE << endl;
    drawGraph(graph_dot_file, g, digraph);

    g.cc();

    cout << "Are the source and sink vertices connected? " << (g.Connected_vertices(source_index, sink_index) ? "Yes" : "No") << endl;

    graph_data_file.close();
    graph_dot_file.close();
    return 0;
}
