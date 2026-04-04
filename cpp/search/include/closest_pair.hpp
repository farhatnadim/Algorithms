#ifndef ALGORITHMS_CLOSEST_PAIR_HPP
#define ALGORITHMS_CLOSEST_PAIR_HPP

#include <vector>
#include <utility>

namespace algorithms {

struct Point {
    double x;
    double y;
};

// TODO: User implements
std::pair<Point, Point> closestPair(const std::vector<Point>& points);

} // namespace algorithms

#endif // ALGORITHMS_CLOSEST_PAIR_HPP
