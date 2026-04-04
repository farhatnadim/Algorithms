#ifndef ALGORITHMS_STACK_HPP
#define ALGORITHMS_STACK_HPP

#include <optional>

namespace algorithms {

// TODO: User implements
template<typename T>
class Stack {
public:
    Stack() = default;
    ~Stack() = default;

    void push(const T& value);
    std::optional<T> pop();
    std::optional<T> top() const;
    size_t size() const;
    bool empty() const;
};

} // namespace algorithms

#endif // ALGORITHMS_STACK_HPP
