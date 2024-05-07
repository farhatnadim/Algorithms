#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <iterator>
#include <algorithm>
#include <ranges>
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
    cout << vertex << " " << edge << endl;
    vector<int> tuple ={vertex,edge};
    return tuple;

}

void merge_vertex(dict & graph ) {

    auto vertex_tuple = select_random_edge(graph);
    vector<int> merged_edges;
    std::merge(graph[vertex_tuple[0]].begin(),graph[vertex_tuple[0]].end(),graph[vertex_tuple[1]].begin(),graph[vertex_tuple[1]].end(),std::back_inserter(merged_edges)); 
    graph[vertex_tuple[0]] = merged_edges;
    graph.erase(vertex_tuple[1]);
    // Replace Deleted vertex with the merged one
    for ( auto &[vertex, edges] : graph)
        {
            auto new_edges = edges| views::transform([&](int n) { 
                return n == vertex_tuple[1] ? vertex_tuple[0] : n;
             });
             /*std::transform(edges.begin(), edges.end(), std::back_inserter(new_edges),
                       [&](int n) { return n == vertex_tuple[1] ? vertex_tuple[0] : n; });
        edges = new_edges; */
            edges = vector<int> (new_edges.begin(),new_edges.end());
            

        }
    // create a temp vector
    // iterate accross the edges list for each vertex
    // replace vertex 2 with vertex 1 
    // assign temp vector at the graph[vertex1]
    

}



int main()
{
    dict example {{1,{1,2,3,4}},{2,{1,5,6,4}},{3,{1,5}},{4,{2,1,5}},{5,{2,3,4,6}},{6,{2,4}}};
    cout << "Premerge" << endl;
    print_graph(example);
    merge_vertex(example);
    cout << "PostMerge" << endl;
    print_graph(example);
    cout << "PostRemove" << endl;
    print_graph(example);
}
//1 2 3 4
//2 1 5 6 4
//3 1 5
//4 2 1 5
//5 2 3 4 6
//6 2 5