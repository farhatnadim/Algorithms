#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <iterator>
#include <algorithm>
#include <ranges>
#include <sstream>
#include <fstream>


// making my life easier !
using dict = std::map< int, std::vector<int> >; 

// prints the graph by iterating over the map
void print_graph (const dict & graph  ) {
    for (const auto &[ vertex, edges ] : graph){
        std::cout << "Vertex " << vertex << " Edges " ;
        for ( auto element : edges )
            std::cout << " " << element;
        std::cout << std::endl; 
    }
}


std::vector<int> select_random_edge ( const dict & graph){
    // select random key from map
    // from that key select random value in the edge vector
     
    std::random_device rd; // for seed
    std::mt19937 generator(rd());
    std::uniform_int_distribution<> vertices_distrib(0,graph.size()-1);
    int randomVertexIndex = vertices_distrib(generator);
    auto it = std::begin(graph);
    std::advance(it, randomVertexIndex);
    std::uniform_int_distribution<> edges_distrib(0,it->second.size()-1);
    int randomEdgeIndex = edges_distrib(generator);
    auto vit = std::begin(it->second);
    std::advance(vit, randomEdgeIndex);
    int vertex2 = *vit;
    int vertex1 = it->first;
    std::vector<int> edge = {vertex1, vertex2};
    return edge;
}

// Merges two vertices in the graph according to the Karger's algorithm
void merge_vertex(dict & graph ) {

    auto edge = select_random_edge(graph);
    std::vector<int> merged_edges;
    std::merge(graph[edge[0]].begin(),graph[edge[0]].end(),
               graph[edge[1]].begin(),graph[edge[1]].end(),
               std::back_inserter(merged_edges)); 
    graph[edge[0]] = merged_edges;
    graph.erase(edge[1]);
    // Replace Deleted vertex with the merged one
    for ( auto &[vertex, edges] : graph){
            auto new_edges = edges | std::views::transform([&](int n) { 
                return n == edge[1] ? edge[0] : n;
             });
            
            edges = std::vector<int> (new_edges.begin(),new_edges.end());
        }
    //removing self loops
    auto new_edges = graph[edge[0]] | std::views::filter([&] (int n){
            return  n == edge[0] ? false : true;
    });

    graph[edge[0]] = std::vector<int> (new_edges.begin(),new_edges.end());

}

int min_cut(dict graph){
    // returns the minimum cut of the graph
    constexpr auto MIN_VERTEX{2};
    int count {0};
    while( graph.size() > MIN_VERTEX)
        merge_vertex(graph);
    for (auto & [key, edges] : graph){
        count += edges.size();
    }
    return static_cast<int> (count / 2);
}


// create a function that reads the file and returns the graph

dict read_file(std::ifstream & file){
    dict graph;
    std::string line;
    // the file has several rows. each row starts with the vertex and then followed by a vector for edges
    // we will read the file line by line, we read the first value of each line and create the key in the map
    // then read the rest of the line and create a vector of edges
    while (std::getline(file, line)){
        std::vector<int> edges;
        std::istringstream iss(line);
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
    std::ifstream file(argv[1]);
    // check if file is open
    if (!file.is_open()){
        std::cout << "File not found" << std::endl;
        return 1;
    }
    // run the algorithm for multiple trials

    constexpr int TRIALS{100};

    std::vector<int> trials;
    auto min_cut_value = 0;
    const auto graph = read_file(file);

    for (int i = TRIALS; i > 0; i--)
    {   
        dict example (graph);
        trials.push_back(min_cut(example));
    }
    std::cout << "Minimum Cut " << *std::min_element(trials.begin(), trials.end()) << std::endl;
    return 0;
}
