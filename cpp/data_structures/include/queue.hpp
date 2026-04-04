#ifndef ALGORITHMS_QUEUE_HPP
#define ALGORITHMS_QUEUE_HPP

#include <optional>

namespace algorithms {

// TODO: User implements
template<typename T>
class Queue {
public:
    Queue() = default;
    ~Queue() = default;

    void enqueue(const T& value);
    std::optional<T> dequeue();
    std::optional<T> front() const;
    size_t size() const;
    bool empty() const;
};

} // namespace algorithms

#endif // ALGORITHMS_QUEUE_HPP
