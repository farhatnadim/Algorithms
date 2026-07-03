#ifndef ALGORITHMS_SELECT_HPP
#define ALGORITHMS_SELECT_HPP

#include <vector>
#include <cstddef>

namespace algorithms {

// TODO: User implements
// Randomized selection (quickselect): returns the ith order statistic
// (0-indexed) of arr. Average O(n).
// Reference: Select/Python/RSelect.py
template<typename T>
T rSelect(std::vector<T>& arr, std::size_t ith);

// TODO: User implements
// Deterministic selection (median-of-medians): returns the ith order
// statistic (0-indexed) of arr. Worst-case O(n). Uses the upper median
// for even-sized groups (see Select/Python/DSelect.py).
template<typename T>
T dSelect(std::vector<T>& arr, std::size_t ith);

} // namespace algorithms

#endif // ALGORITHMS_SELECT_HPP
