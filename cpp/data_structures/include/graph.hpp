#ifndef ALGORITHMS_GRAPH_HPP
#define ALGORITHMS_GRAPH_HPP

#include <vector>
#include <unordered_map>

namespace algorithms {

// TODO: User implements
class Graph {
public:
    Graph() = default;
    void addVertex(int vertex);
    void addEdge(int from, int to, double weight = 1.0);
    std::vector<int> getNeighbors(int vertex) const;
    size_t size() const;

private:
    std::unordered_map<int, std::vector<std::pair<int, double>>> adjacencyList_;
};

} // namespace algorithms

#endif // ALGORITHMS_GRAPH_HPP
