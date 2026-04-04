#ifndef ALGORITHMS_COUNT_INVERSIONS_HPP
#define ALGORITHMS_COUNT_INVERSIONS_HPP

#include <vector>
#include <cstdint>

namespace algorithms {

// TODO: User implements
// Counts the number of inversions in an array
// An inversion is a pair (i, j) where i < j but arr[i] > arr[j]
template<typename T>
int64_t countInversions(std::vector<T>& arr);

} // namespace algorithms

#endif // ALGORITHMS_COUNT_INVERSIONS_HPP
