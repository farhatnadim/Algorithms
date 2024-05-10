#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <iterator>
#include <algorithm>
#include <ranges>
#include <sstream>
#include <fstream>
using namespace std;

// making my life easier !
using dict = map< int, vector<int> >; 

// prints the graph by iterating over the map
void print_graph (const dict & graph  ) {
    for (const auto &[ key, value ] : graph){
        cout << "Vertex " <<  key << " Edges " ;
        for ( auto element : value)
            cout << " " << element;
        cout << endl; 
    }
}


vector<int> select_random_edge ( dict & graph){
    // select random key from map
    // from that key select random value in the edge vector
     
    random_device rd; // for seed
    std::mt19937 generator(rd());
    std::uniform_int_distribution<> vertices_distrib(0,graph.size()-1);
    int randomVertexIndex = vertices_distrib(generator);
    auto it = std::begin(graph);
    std::advance(it, randomVertexIndex);
    int vertex = it->first;
    std::uniform_int_distribution<> edges_distrib(0,it->second.size()-1);
    int randomEdgeIndex = edges_distrib(generator);
    auto vit = std::begin(it->second);
    std::advance(vit, randomEdgeIndex);
    int edge = *vit;
    vector<int> tuple = {vertex,edge};
    return tuple;

}

// Merges two vertices in the graph according to the Karger's algorithm
void merge_vertex(dict & graph ) {

    auto vertex_tuple = select_random_edge(graph);
    vector<int> merged_edges;
    std::merge(graph[vertex_tuple[0]].begin(),graph[vertex_tuple[0]].end(),graph[vertex_tuple[1]].begin(),graph[vertex_tuple[1]].end(),std::back_inserter(merged_edges)); 
    graph[vertex_tuple[0]] = merged_edges;
    graph.erase(vertex_tuple[1]);
    // Replace Deleted vertex with the merged one
    for ( auto &[vertex, edges] : graph){
            auto new_edges = edges | views::transform([&](int n) { 
                return n == vertex_tuple[1] ? vertex_tuple[0] : n;
             });
             /*std::transform(edges.begin(), edges.end(), std::back_inserter(new_edges),
                       [&](int n) { return n == vertex_tuple[1] ? vertex_tuple[0] : n; });
        edges = new_edges; */
            edges = vector<int> (new_edges.begin(),new_edges.end());
        }
    //removing self loops
    auto new_edges = graph[vertex_tuple[0]] | views::filter([&] (int n){
            return  n == vertex_tuple[0] ? false : true;
    });

    graph[vertex_tuple[0]] = vector<int> (new_edges.begin(),new_edges.end());

}

int min_cut(dict graph){
    // returns the minimum cut of the graph
    constexpr auto MIN_VERTEX{2};
    int count {0};
    while( graph.size() > 2)
        merge_vertex(graph);
    for (auto & [key, edges] : graph){
        count += edges.size();
    }
    return static_cast<int> (count / 2);
}


// create a function that reads the file and returns the graph

dict read_file(ifstream & file){
    dict graph;
    string line;
    // the file has several rows. each row starts with the vertex and then followed by a vector for edges
    // we will read the file line by line, we read the first value of each line and create the key in the map
    // then read the rest of the line and create a vector of edges
    while (getline(file, line)){
        vector<int> edges;
        istringstream iss(line);
        int vertex;
        iss >> vertex;
        int edge;
        while (iss >> edge){
            edges.push_back(edge);
        }
        graph[vertex] = edges;
    }
    return graph;
}

int main(int argc, char *argv[])
{
    // read file 
    ifstream file(argv[1]);
    // check if file is open
    if (!file.is_open()){
        cout << "File not found" << endl;
        return 1;
    }
    // run the algorithm for multiple trials

    constexpr int TRIALS{100};

    vector<int> trials;
    auto min_cut_value = 0;
    const auto graph = read_file(file);

    for (int i = TRIALS; i > 0; i--)
    {   
        dict example (graph);
        trials.push_back(min_cut(example));
    }
    cout << "Minimum Cut " << *min_element(trials.begin(), trials.end()) << endl;
    return 0;
}
