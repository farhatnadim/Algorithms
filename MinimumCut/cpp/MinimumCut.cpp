#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <iterator>

using namespace std;

// making my life easier !
using dict = map< int, vector<int> >; 


void print_graph (const dict & graph  ) {
    for (const auto &[key,value ] : graph)
    {
        cout << "Vertex " <<  key << " Edges " ;
        for ( auto element : value)
            cout << " " << element;
        cout << endl; 
    }

}

map<int, int> select_random_edge (const dict & graph){
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
    cout << vertex << " " << edge << endl;
    map<int,int> tuple;
    tuple[vertex] = edge;
    return tuple;

}


int main()
{
    dict example {{1,{1,2,3,4}},{2,{1,5,6,4}},{3,{1,5}},{4,{2,1,5}},{5,{2,3,4,6}},{6,{2,4}}};   
    select_random_edge(example);
}
//1 2 3 4
//2 1 5 6 4
//3 1 5
//4 2 1 5
//5 2 3 4 6
//6 2 5