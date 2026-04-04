#ifndef ALGORITHMS_KARGERS_ALGORITHM_HPP
#define ALGORITHMS_KARGERS_ALGORITHM_HPP

#include <vector>
#include <utility>

namespace algorithms {

// TODO: User implements
// Returns the minimum cut of an undirected graph
// Graph represented as edge list: vector of (from, to) pairs
int kargersMinCut(const std::vector<std::pair<int, int>>& edges, int numVertices);

} // namespace algorithms

#endif // ALGORITHMS_KARGERS_ALGORITHM_HPP
